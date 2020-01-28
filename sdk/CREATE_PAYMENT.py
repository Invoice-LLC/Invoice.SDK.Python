
class CREATE_PAYMENT:
    def __init__(self):
        self.order = None
        self.settings = None
        self.custom_parameters = None
        self.receipt = None

    def setReceipt(self, items):
        array = []

        for item in items:
            array.append(item.__dict__)
        self.receipt = array

    def setOrder(self, order):
        self.order = order.__dict__

    def setSettings(self, settings):
        self.settings = settings.__dict__
