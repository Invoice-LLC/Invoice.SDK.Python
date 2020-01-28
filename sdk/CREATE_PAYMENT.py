import json

from sdk.JsonSerializable import JsonSerializable
from sdk.common.ORDER import ORDER
from sdk.common.SETTINGS import SETTINGS


class CREATE_PAYMENT(JsonSerializable):
    def __init__(self):
        self.__order = None
        self.__settings = None
        self.custom_parameters = None
        self.__receipt = None

    def setOrder(self, order: ORDER):
        self.__order = order.toJSON()

    def setSettings(self, settings: SETTINGS):
        self.__settings = settings.toJSON()

    def setReceipt(self, items):
        array = []

        for item in items:
            array.append(item.toJSON())
        self.__receipt = json.dumps(array)