import os
import uuid
import subprocess
import shutil
import discord
from dotenv import load_dotenv

load_dotenv()

intents = discord.Intents.default()
intents.message_content = True

bot = discord.Client(intents=intents)

TOKEN = os.getenv("DISCORD_TOKEN")


@bot.event
async def on_ready():
    print(f"✅ Logged in as {bot.user}")


@bot.event
async def on_message(message):
    if message.author.bot:
        return

    if bot.user not in message.mentions:
        return

    target_message = message
    if message.reference:
        try:
            target_message = await message.channel.fetch_message(message.reference.message_id)
        except Exception as e:
            print(f"Error fetching referenced message: {e}")
            await message.reply(f"❌ Не удалось получить сообщение, {message.author.mention}", mention_author=True)
            return

    for attachment in target_message.attachments:
        if attachment.filename.lower().endswith(".webm"):
            status_msg = await message.channel.send("🎬 Начинаю конвертацию `.webm`...")

            input_filename = f"{uuid.uuid4()}.webm"
            output_filename = f"{uuid.uuid4()}.mp4"

            try:
                await attachment.save(input_filename)

                if not shutil.which("ffmpeg"):
                    print("ffmpeg не найден в PATH")
                    await message.reply(f"❌ Произошла ошибка, {message.author.mention}. Попробуйте позже.", mention_author=True)
                    await status_msg.delete()
                    return

                cmd = [
                    "ffmpeg",
                    "-i", input_filename,
                    "-c:v", "libx264",
                    "-preset", "fast",
                    "-pix_fmt", "yuv420p",
                    output_filename
                ]
                subprocess.run(cmd, check=True)

                await message.reply(
                    f"✅ Готово, {message.author.mention}!",
                    file=discord.File(output_filename),
                    mention_author=True
                )

            except subprocess.CalledProcessError as e:
                print(f"ffmpeg error: {e}")
                await message.reply(f"❌ Ошибка конвертации видео, {message.author.mention}. Попробуйте позже.", mention_author=True)
            except Exception as e:
                print(f"Unexpected error: {e}")
                await message.reply(f"❌ Произошла ошибка, {message.author.mention}. Попробуйте позже.", mention_author=True)
            finally:
                for f in [input_filename, output_filename]:
                    if os.path.exists(f):
                        os.remove(f)
                await status_msg.delete()
            return

    await message.reply(f"⚠️ В сообщении нет `.webm` файла, {message.author.mention}", mention_author=True)


if __name__ == "__main__":
    bot.run(TOKEN)
