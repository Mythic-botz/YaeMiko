# SOURCE https://github.com/Mythic-botz/YaeMiko
# CREATED BY https://t.me/O_okarma
# PROVIDED BY https://t.me/ProjectCodeX
# NEKOS

# <============================================== IMPORTS =========================================================>
import aiohttp
from nekosbest import Client, Result
from telethon import events
from typing import Union, List

from Database.mongodb.toggle_mongo import is_nekomode_on, nekomode_off, nekomode_on
from Mikobot import tbot
from Mikobot.state import state  # Import the state function

# <=======================================================================================================>

url_sfw = "https://api.waifu.pics/sfw/"

# Supported by nekos.best (subset of your original commands)
nekosbest_commands = [
    "neko",
    "waifu",
    "hug",
    "kiss",
    "pat",
    "cuddle",
    "handhold",
    "tickle",
    "poke",
    "bite",
    "slap",
]

# Commands only supported by api.waifu.pics
waifu_pics_commands = [
    "shinobu",
    "megumin",
    "bully",
    "cry",
    "awoo",
    "smug",
    "bonk",
    "yeet",
    "blush",
    "smile",
    "spank",
    "wave",
    "highfive",
    "nom",
    "glomp",
    "hTojiy",
    "wink",
    "dance",
    "cringe",
]

# Initialize nekos.best client
neko_client = Client()

# <================================================ FUNCTIONS =======================================================>
@tbot.on(events.NewMessage(pattern="/wallpaper"))
async def wallpaper(event):
    chat_id = event.chat_id
    nekomode_status = await is_nekomode_on(chat_id)
    if nekomode_status:
        # wallpaper not supported by nekos.best, use api.waifu.pics
        url = f"{url_sfw}wallpaper"
        try:
            async with aiohttp.ClientSession() as session:
                async with session.get(url) as response:
                    result = await response.json()
                    img_url = result["url"]
                    await event.reply(file=img_url)
        except Exception as e:
            await event.reply(f"Error fetching wallpaper: {str(e)}")


@tbot.on(events.NewMessage(pattern="/nekomode on"))
async def enable_nekomode(event):
    chat_id = event.chat_id
    await nekomode_on(chat_id)
    await event.reply("Nekomode has been enabled.")


@tbot.on(events.NewMessage(pattern="/nekomode off"))
async def disable_nekomode(event):
    chat_id = event.chat_id
    await nekomode_off(chat_id)
    await event.reply("Nekomode has been disabled.")


@tbot.on(events.NewMessage(pattern=r"/(?:{})".format("|".join(nekosbest_commands + waifu_pics_commands))))
async def nekomode_commands(event):
    chat_id = event.chat_id
    nekomode_status = await is_nekomode_on(chat_id)
    if nekomode_status:
        target = event.raw_text[1:].lower()  # Remove the slash before the command
        try:
            if target in nekosbest_commands:
                # Use nekos.best for supported categories
                result: Result = await neko_client.get_image(target)
                await event.respond(file=result.url)
            elif target in waifu_pics_commands:
                # Fall back to api.waifu.pics for unsupported categories
                url = f"{url_sfw}{target}"
                async with aiohttp.ClientSession() as session:
                    async with session.get(url) as response:
                        result = await response.json()
                        animation_url = result["url"]
                        await event.respond(file=animation_url)
            else:
                await event.respond("Invalid command.")
        except Exception as e:
            await event.respond(f"Error fetching {target}: {str(e)}")


__help__ = """
*✨ Sends fun Gifs/Images*

➥ /nekomode on : Enables fun neko mode.
➥ /nekomode off : Disables fun neko mode

» /bully: sends random bully gifs.
» /neko: sends random neko gifs.
» /wallpaper: sends random wallpapers.
» /highfive: sends random highfive gifs.
» /tickle: sends random tickle GIFs.
» /wave: sends random wave GIFs.
» /smile: sends random smile GIFs.
» /blush: sends random blush GIFs.
» /waifu: sends random waifu stickers.
» /kiss: sends random kissing GIFs.
» /cuddle: sends random cuddle GIFs.
» /cry: sends random cry GIFs.
» /bonk: sends random bonk GIFs.
» /smug: sends random smug GIFs.
» /slap: sends random slap GIFs.
» /hug: get hugged or hug a user.
» /pat: pats a user or get patted.
» /spank: sends a random spank gif.
» /dance: sends a random dance gif.
» /poke: sends a random poke gif.
» /wink: sends a random wink gif.
» /bite: sends random bite GIFs.
» /handhold: sends random handhold GIFs.
"""

__mod_name__ = "NEKO"
# <================================================ END =======================================================>