from src.bot import Bot

if __name__ == '__main__':
    for bot_num in range(10):
        print(f"{bot_num+1}'s bot")
        bot = Bot()
        bot.run()

