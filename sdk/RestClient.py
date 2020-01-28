import json

import requests
import base64

from sdk.GET_TERMINAL import GET_TERMINAL
from sdk.CLOSE_PAYMENT import CLOSE_PAYMENT
from sdk.CREATE_PAYMENT import CREATE_PAYMENT
from sdk.CREATE_REFUND import CREATE_REFUND
from sdk.CREATE_TERMINAL import CREATE_TERMINAL
from sdk.GET_PAYMENT import GET_PAYMENT
from sdk.GET_PAYMENT_BY_ORDER import GET_PAYMENT_BY_ORDER
from sdk.GET_REFUND import GET_REFUND
from sdk.PaymentInfo import PaymentInfo
from sdk.RefundInfo import RefundInfo
from sdk.TerminalInfo import TerminalInfo


class RestClient:
    __url = "https://api.invoice.su/api/v2/"

    def __init__(self, login, apiKey):
        self.login = login
        self.apiKey = apiKey

    def __send(self, requestType, jsonObject):
        url = self.__url + requestType

        auth = self.login + ":" + self.apiKey
        auth = base64.b64encode(bytes(auth, "ascii"))
        auth = str(auth).replace("b'", "").replace("'", "")

        headers = {
            "Host": "pay.invoice.su",
            "content-type": "application/json",
            "Authorization": "Basic " + auth,
            "User-Agent": "curl/7.55.1",
            "Accept": "*/*"
        }

        response = requests.post(url, jsonObject, headers=headers)

        return response.content

    def GetTerminal(self, request: GET_TERMINAL):
        response = self.__send("GetTerminal", json.dumps(request.__dict__))
        response = json.loads(response)

        terminal_info = TerminalInfo()
        terminal_info.setParams(response)
        return terminal_info

    def CreateTerminal(self, request: CREATE_TERMINAL):
        response = self.__send("CreateTerminal", json.dumps(request.__dict__))
        response = json.loads(response)

        terminal_info = TerminalInfo()
        terminal_info.setParams(response)
        return terminal_info

    def GetRefund(self, request: GET_REFUND):
        response = self.__send("GetRefund", json.dumps(request.__dict__))
        response = json.loads(response)

        refund_info = RefundInfo()
        refund_info.setParams(response)
        return refund_info

    def CreateRefund(self, request: CREATE_REFUND):
        response = self.__send("CreateRefund", json.dumps(request.__dict__))
        response = json.loads(response)

        refund_info = RefundInfo()
        refund_info.setParams(response)
        return refund_info

    def ClosePayment(self, request: CLOSE_PAYMENT):
        response = self.__send("ClosePayment", json.dumps(request.__dict__))
        response = json.loads(response)

        payment_info = PaymentInfo()
        payment_info.setParams(response)
        return payment_info

    def GetPaymentByOrder(self, request: GET_PAYMENT_BY_ORDER):
        response = self.__send("GetPaymentByOrder", json.dumps(request.__dict__))
        response = json.loads(response)

        payment_info = PaymentInfo()
        payment_info.setParams(response)
        return payment_info

    def GetPayment(self, request: GET_PAYMENT):
        response = self.__send("GetPayment", json.dumps(request.__dict__))
        response = json.loads(response)

        payment_info = PaymentInfo()
        payment_info.setParams(response)
        return payment_info

    def CreatePayment(self, request: CREATE_PAYMENT):
        response = self.__send("CreatePayment", json.dumps(request.__dict__))
        response = json.loads(response)

        payment_info = PaymentInfo()
        payment_info.setParams(response)
        return payment_info
