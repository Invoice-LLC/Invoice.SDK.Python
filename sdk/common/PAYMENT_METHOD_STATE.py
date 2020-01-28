from enum import Enum


class PAYMENT_STATE(Enum):
    created = "created"
    init = "init"
    process = "process"
    successful = "successful"
    error = "error"

