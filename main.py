from src.bot import Bot
from src.constants import server_default_config

if __name__ == '__main__':
    for bot_num in range(int(server_default_config["BOT_LOOP_COUNT"])):
        print(f"run {bot_num + 1}'s bot...")
        bot = Bot()
        bot.run()
        print(f"complete {bot_num + 1}'s bot - {bot.event_data.user_id}\n")

