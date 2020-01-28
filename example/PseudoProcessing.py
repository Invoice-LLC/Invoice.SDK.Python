from sdk.CLOSE_PAYMENT import CLOSE_PAYMENT
from sdk.CREATE_PAYMENT import CREATE_PAYMENT
from sdk.CREATE_REFUND import CREATE_REFUND
from sdk.CREATE_TERMINAL import CREATE_TERMINAL
from sdk.GET_PAYMENT import GET_PAYMENT
from sdk.GET_TERMINAL import GET_TERMINAL
from sdk.RefundInfo import RefundInfo
from sdk.RestClient import RestClient
from sdk.common.REFUND_INFO import REFUND_INFO
from sdk.common.SETTINGS import SETTINGS
from sdk.common.TERMINAL_TYPE import TERMINAL_TYPE


class PseudoProcessing:

    shop_name = "Магазин"
    shop_description = "Описание магазина"
    terminal_type = TERMINAL_TYPE.DYNAMICAL.value
    default_price = 0

    def __init__(self, login, api_key, alias):
        self.login = login
        self.api_key = api_key
        self.rest_client = None
        self.payment_info = None
        self.terminal_info = None
        self.refund_info = RefundInfo()

        if self.terminal_info is None:
            self.rest_client = RestClient(self.login, self.api_key)

            get_terminal = GET_TERMINAL(alias)

            self.terminal_info = self.rest_client.GetTerminal(get_terminal)

            if self.terminal_info is None or self.terminal_info.id is None:
                create_terminal = CREATE_TERMINAL()
                create_terminal.alias = alias
                create_terminal.description = self.shop_description
                create_terminal.name = self.shop_name
                create_terminal.type = self.terminal_type
                create_terminal.defaultPrice = self.default_price

                self.terminal_info = self.rest_client.CreateTerminal(create_terminal)
        print(self.terminal_info.__dict__)

    def on_pay(self, items):
        create_payment = CREATE_PAYMENT()

        create_payment.setReceipt(items)

        settings = SETTINGS()
        settings.terminal_id = self.terminal_info.id

        create_payment.setSettings(settings)

        print(create_payment.__dict__)
        self.payment_info = self.rest_client.CreatePayment(create_payment)
        if self.payment_info is None or self.payment_info.id is None:
            return False
        else:
            return True

    def on_cancel(self, orderId):
        close_payment = CLOSE_PAYMENT(orderId)
        self.rest_client.ClosePayment(close_payment)

    def on_refund(self, orderId, items, reason, amount):
        create_refund = CREATE_REFUND()
        create_refund.setReceipt(items)
        create_refund.id = orderId

        refund_info = REFUND_INFO()
        refund_info.reason = reason
        refund_info.amount = amount

        create_refund.setRefund(refund_info)

        self.refund_info = self.rest_client.CreateRefund(create_refund)
        print(self.refund_info.__dict__)
        if refund_info is None:
            return False

        if self.refund_info.error is None:
            return True
        else:
            return False

    def get_status(self, orderId):
        get_payment = GET_PAYMENT(orderId)
        self.payment_info = self.rest_client.GetPayment(get_payment)

        if self.payment_info is None:
            return None

        return self.payment_info.status


