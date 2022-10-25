from src.event import get_event_name, EventData
from src.bot import Bot


class EventDataForTest(EventData):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def run_event(self, *args, **kwargs):
        pass


# for scenario flow test in local or debug - only show text by event step, not request
class TestBot(Bot):
    def __init__(self):
        super().__init__()
        self.event_runner = EventDataForTest()

    def run_event_step(self, state: int):
        # run event by step
        self.event_data.set_new_event(state)
        self.set_event_state(state)
        print(f"current event : {state}\t{get_event_name(state)}")
        print(self.event_data.to_dict())


if __name__ == '__main__':
    for bot_num in range(5):
        print(f"{bot_num+1}'s bot")
        bot = TestBot()
        bot.run()
