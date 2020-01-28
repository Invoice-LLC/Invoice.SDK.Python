from sdk.common.ORDER import ORDER
from sdk.common.REFUND_INFO import REFUND_INFO


class PaymentInfo:
    def __init__(self):
        self.id = None
        self.order = None
        self.status = None
        self.status_description = None
        self.ip = None
        self.payment_method = None
        self.create_date = None
        self.update_date = None
        self.custom_parameters = None
        self.payment_url = None
        self.error = None
        self.description = None

    def setParams(self, response):
        if "id" in response:
            self.id = response["id"]
        if "order" in response:
            order = ORDER()
            if "id" in response["order"]:
                order.id = response["order"]["id"]
                order.description = response["order"]["description"]
                order.amount = response["order"]["amount"]
                order.currency = response["order"]["currency"]
            self.order = order
        if "status" in response:
            self.status = response["status"]
        if "status_description" in response:
            self.status_description = response["status_description"]
        if "ip" in response:
            self.ip = response["ip"]
        if "payment_method" in response:
            self.payment_method = response["payment_method"]
        if "create_date" in response:
            self.create_date = response["create_date"]
        if "update_date" in response:
            self.update_date = response["update_date"]
        if "custom_parameters" in response:
            self.custom_parameters = response["custom_parameters"]
        if "payment_url" in response:
            self.payment_url = response["payment_url"]
        if "error" in response:
            self.error = response["error"]
        if "description" in response:
            self.create_date = response["description"]