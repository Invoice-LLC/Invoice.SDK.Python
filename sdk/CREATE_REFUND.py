class CREATE_REFUND:
    def __init__(self):
        self.id = None
        self.refund = None
        self.receipt = None

    def setReceipt(self, items):
        array = []

        for item in items:
            array.append(item.__dict__)
        self.receipt = array

    def setRefund(self, refund):
        self.refund = refund.__dict__


