from sdk.JsonSerializable import JsonSerializable


class ORDER(JsonSerializable):

    def __init__(self):
        self.currency = None
        self.amount = None
        self.description = None
        self.id = None


