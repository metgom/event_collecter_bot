import time
from src.constants import (EVENT_NONE,
                           EVENT_LOGIN,
                           EVENT_LOGOUT,
                           EVENT_PRODUCTS,
                           EVENT_PRODUCT_DETAILS,
                           EVENT_PURCHASE,
                           EVENT_PURCHASE_SUCCESS,
                           EVENT_PURCHASE_FAIL,
                           get_event_name,
                           server_default_config)
from src.event import (EventRunner,
                       get_random_event,
                       EventData)


class Bot:
    def __init__(self):
        self.current_state = EVENT_NONE
        self.event_data = None
        self.event_runner = EventRunner()

    def set_event_state(self, state: int):
        self.current_state = state

    def run_event_step(self, state: int):
        # run event by step
        self.event_data.set_new_event(state)
        self.set_event_state(state)
        print(f"current event : {state}\t{get_event_name(state)}")
        resp = self.event_runner.run_event(data=self.event_data.to_dict())
        print(resp.json())
        time.sleep(0.01)

    def bot_init(self):
        # data set None + create user id
        if self.event_data is None:
            self.event_data = EventData()
        else:
            self.event_data.event_reset()
        self.event_data.create_random_user_id(server_default_config["BOT_BASE_ID"],
                                              int(server_default_config["BOT_NAME_SUFFIX_MAX_NUMBER"]))

    def run(self):
        """
        시나리오
        0 데이터 폼 생성 + 초기화
        1 로그인
        2 상품목록
        3 상품상세 or 로그아웃
        4 상품목록(뒤로가기) or 구매 or 로그아웃
        5 성공 or 실패
        6-1 성공 : 3 or 로그아웃(낮음)
        6-2 실패 : 3 or 로그아웃(높음)
        """
        # 0: initialize event data
        self.bot_init()
        # 1
        self.run_event_step(EVENT_LOGIN)
        # 2
        self.run_event_step(EVENT_PRODUCTS)

        while self.current_state != EVENT_LOGOUT:
            if self.current_state == EVENT_PRODUCTS:
                # 3
                self.run_event_step(get_random_event(EVENT_LOGOUT,
                                                     EVENT_PRODUCT_DETAILS,
                                                     weights=[30, 70]))
            elif self.current_state == EVENT_PRODUCT_DETAILS:
                # 4
                self.run_event_step(get_random_event(EVENT_LOGOUT,
                                                     EVENT_PRODUCTS,
                                                     EVENT_PURCHASE,
                                                     weights=[20, 20, 60]))
            elif self.current_state == EVENT_PURCHASE:
                # 5
                self.run_event_step(get_random_event(EVENT_PURCHASE_SUCCESS,
                                                     EVENT_PURCHASE_FAIL,
                                                     weights=[60, 40]))
            elif self.current_state == EVENT_PURCHASE_SUCCESS:
                # 6-1
                self.run_event_step(get_random_event(EVENT_LOGOUT,
                                                     EVENT_PRODUCTS,
                                                     weights=[20, 80]))
            elif self.current_state == EVENT_PURCHASE_FAIL:
                # 6-2
                self.run_event_step(get_random_event(EVENT_LOGOUT,
                                                     EVENT_PRODUCTS,
                                                     weights=[90, 10]))
