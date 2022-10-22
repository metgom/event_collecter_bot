from src.bot import TestBot

if __name__ == '__main__':
    for bot_num in range(10):
        print(f"{bot_num+1}'s bot")
        bot = TestBot()
        bot.run()
