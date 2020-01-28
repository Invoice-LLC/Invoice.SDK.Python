from PseudoProcessing import PseudoProcessing
import argparse

from sdk.common.ITEM import ITEM


def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument("-a", "--action", dest='action', nargs='+', required=False, help="action parameter")
    parser.add_argument("-i", "--id", dest='id', nargs='+', required=False, help="id parameter")
    return parser.parse_args()


arguments = parse_args()
args = arguments.__dict__

action = args["action"][0]

processing = PseudoProcessing("demo", "1526fec01b5d11f4df4f2160627ce351", "1:2237")

item1 = ITEM()
item1.name = "Soup"
item1.price = 10
item1.discount = 0
item1.quantity = 2
item1.resultPrice = 20

item2 = ITEM()
item2.name = "Kefir"
item2.price = 1000
item2.discount = 10
item2.quantity = 1
item2.resultPrice = 990

items = {
    item1,
    item2
}


if action == "pay":
    pay = processing.on_pay(items)
    if pay :
        print("Платеж оформлен"+processing.payment_info.id)
    else:
        print("Ошибка платежа")
