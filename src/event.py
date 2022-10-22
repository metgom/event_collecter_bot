from abc import ABCMeta, abstractmethod
import random
import uuid
import requests
from typing import Union
from constants import (EVENT_NONE,
                       EVENT_LOGIN,
                       EVENT_LOGOUT,
                       EVENT_PRODUCTS,
                       EVENT_PRODUCT_DETAILS,
                       EVENT_PURCHASE,
                       EVENT_PURCHASE_SUCCESS,
                       EVENT_PURCHASE_FAIL,
                       EVENT_END,
                       get_event_name)


def get_random_event(*events: int, **kwargs):
    # random.choice is can use weight per event.
    return random.choices(events, k=1, **kwargs)[0]


def get_guid():
    return str(uuid.uuid1())


class Data(metaclass=ABCMeta):
    def __init__(self):
        pass

    @abstractmethod
    def set_random_data(self, *args, **kwargs):
        raise NotImplementedError("Should have implemented this.")

    def to_dict(self) -> dict:
        return self.__dict__


class OrderData(Data):
    def __init__(self,
                 order_id: Union[str, None] = None,
                 currency: Union[str, None] = None,
                 price: Union[float, None] = None,
                 ):
        self.order_id = order_id
        self.currency = currency
        self.price = price

    def set_random_data(self):
        self.order_id = get_guid(),
        self.currency = "krw",
        self.price = (random.randint(0, 99) * 100)


class EventData(Data):
    def __init__(self,
                 event_id: Union[str, None] = None,
                 user_id: Union[str, None] = None,
                 event: Union[str, None] = None,
                 order: Union[OrderData, None] = None):
        self.event_id = event_id
        self.user_id = user_id
        self.event = event
        self.order = order

    def create_random_user_id(self, base_name: Union[str, None] = "user"):
        # create user id - "base_name1", "base_name2", ... , "base_name9"
        self.user_id = base_name+str(random.randint(1, 10))
        return

    def set_random_data(self, event_flag: int = EVENT_NONE, create_order: bool = False):
        if self.user_id is None:
            self.create_random_user_id()

        if event_flag != EVENT_NONE:
            self.event_id = get_guid()
        self.event = get_event_name(event_flag)

        if create_order is True:
            if self.order is None:
                self.order = OrderData()
            self.order.set_random_data()

    def set_new_event(self, event_flag: int):
        event_name = get_event_name(event_flag)
        if self.event == event_name:
            raise Exception(f"Same Event - {event_name}")
        if event_flag == EVENT_PURCHASE:
            # need order
            self.set_random_data(event_flag=event_flag, create_order=True)
        else:
            self.set_random_data(event_flag=event_flag, create_order=False)

    def to_dict(self):
        event_data = {
            "event_id": self.event_id,
            "user_id": self.user_id,
            "event": self.event,
        }
        if self.order is not None:
            event_data.update({"parameters": self.order.to_dict()})
        return event_data


class EventRunner(metaclass=ABCMeta):
    def __int__(self):
        self._event = None

    def get_event(self):
        return self._event

    # for test
    def event_info(self):
        print(f"current event : {self._event}\t{get_event_name(self._event)}")

    @abstractmethod
    def run_event(self, data: dict, *args, **kwargs):
        raise NotImplementedError("Should have implemented this.")


class LocalRunner(EventRunner):
    def run_event(self, data: dict, *args, **kwargs):
        response = requests.post(json=data, *args, **kwargs)
        return response


class EC2Runner(EventRunner):
    def run_event(self, data: dict, *args, **kwargs):
        response = requests.request(json=data, *args, **kwargs)
        return response


class Login(EventRunner):
    def __init__(self):
        self._event = EVENT_LOGIN

    def run_event(self, data: dict, *args, **kwargs):
        # response = requests.request(method='GET', url='', params=self.current_state, json='')
        pass


class Logout(EventRunner):
    def __init__(self):
        self._event = EVENT_LOGOUT

    def run_event(self, data: dict, *args, **kwargs):
        # response = requests.request(method='GET', url='', params=self.current_state, json='')
        pass


class Products(EventRunner):
    def __init__(self):
        self._event = EVENT_PRODUCTS

    def run_event(self, data: dict, *args, **kwargs):
        # response = requests.request(method='GET', url='', params=self.current_state, json='')
        pass


class ProductDetails(EventRunner):
    def __init__(self):
        self._event = EVENT_PRODUCT_DETAILS

    def run_event(self, data: dict, *args, **kwargs):
        # response = requests.request(method='GET', url='', params=self.current_state, json='')
        pass


class Purchase(EventRunner):
    def __init__(self):
        self._event = EVENT_PURCHASE

    def run_event(self, data: dict, *args, **kwargs):
        # response = requests.request(method='GET', url='', params=self.current_state, json='')
        pass


class PurchaseSuccess(EventRunner):
    def __init__(self):
        self._event = EVENT_PURCHASE_SUCCESS

    def run_event(self, data: dict, *args, **kwargs):
        # response = requests.request(method='GET', url='', params=self.current_state, json='')
        pass


class PurchaseFail(EventRunner):
    def __init__(self):
        self._event = EVENT_PURCHASE_FAIL

    def run_event(self, data: dict, *args, **kwargs):
        # response = requests.request(method='GET', url='', params=self.current_state, json='')
        pass
