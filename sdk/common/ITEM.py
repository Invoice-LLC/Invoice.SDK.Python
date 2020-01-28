from sdk.JsonSerializable import JsonSerializable


class ITEM(JsonSerializable):
    def __init__(self):
        self.name = None
        self.price = None
        self.resultPrice = None
        self.discount = None
        self.quantity = None