from sdk.JsonSerializable import JsonSerializable


class SETTINGS(JsonSerializable):
    def __init__(self):
        self.terminal_id = None
        self.payment_method = None
        self.success_url = None
        self.fail_url = None


