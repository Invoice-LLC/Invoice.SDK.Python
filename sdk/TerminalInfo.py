from sdk.common import TERMINAL_TYPE


class TerminalInfo:

    def __init__(self):
        self.id = None
        self.link = None
        self.name = None
        self.alias = None
        self.description = None
        self.type = None
        self.defaultPrice = None
        self.error = None

    def setParams(self, response):
        if "error" in response:
            self.error = response["error"]
        if "defaultPrice" in response:
            self.defaultPrice = response["defaultPrice"]
        if "type" in response:
            self.type = response["type"]
        if "description" in response:
            self.description = response["description"]
        if "name" in response:
            self.name = response["name"]
        if "alias" in response:
            self.alias = response["alias"]
        if "id" in response:
            self.id = response["id"]
        if "link" in response:
            self.link = response["link"]

