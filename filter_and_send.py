import os
import sys
import time

from telethon import TelegramClient, events, utils


def get_env(name, message, cast=str):
    if name in os.environ:
        return os.environ[name]
    while True:
        value = input(message)
        try:
            return cast(value)
        except ValueError as e:
            print(e, file=sys.stderr)
            time.sleep(1)


session = os.environ.get('TG_SESSION', 'printer')
api_id = get_env('TG_API_ID', 'Enter your API ID: ', int)
api_hash = get_env('TG_API_HASH', 'Enter your API hash: ')
bot_token = get_env('TG_BOT_TOKEN', 'Enter your bot token: ')


client = TelegramClient(session, api_id, api_hash, proxy=None).start()
bot = TelegramClient('H1BSlotFinderBot', api_id, api_hash)

@client.on(events.NewMessage(chats='Regular_H1B_H4_VisaSlotsChecking', pattern=r'^(?i)((?!na).)*$'))
async def handler(event):
    await bot.start(bot_token=bot_token)
    entity = await bot.get_entity('kunwar11singh')
    await bot.send_message(entity, event.message)

try:
    print('(Press Ctrl+C to stop this)')
    client.run_until_disconnected()
finally:
    client.disconnect()
    bot.disconnect()