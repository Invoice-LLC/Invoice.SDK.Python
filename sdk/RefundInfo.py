from sdk.common.ORDER import ORDER
from sdk.common.REFUND_INFO import REFUND_INFO


class RefundInfo:
    def __init__(self):
        self.id = None
        self.order = None
        self.refund = None
        self.status = None
        self.payment_id = None
        self.payment_method = None
        self.create_date = None
        self.update_date = None
        self.custom_parameters = None
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
        if "refund" in response:
            refund = REFUND_INFO()
            refund.currency = response["refund"]["currency"]
            refund.amount = response["refund"]["amount"]
            refund.reason = response["refund"]["reason"]
        if "status" in response:
            self.status = response["status"]
        if "payment_id" in response:
            self.payment_id = response["payment_id"]
        if "payment_method" in response:
            self.payment_method = response["payment_method"]
        if "create_date" in response:
            self.create_date = response["create_date"]
        if "update_date" in response:
            self.update_date = response["update_date"]
        if "custom_parameters" in response:
            self.custom_parameters = response["custom_parameters"]
        if "error" in response:
            self.error = response["error"]
        if "description" in response:
            self.create_date = response["description"]

