import os
from pprint import pprint
import sale_service


filename = "sales.txt"

while True:
    try:
        os.system("cls")
        action = input("choose:\n1 - show report\n2 - add sale\n3 - exit\n")
        os.system("cls")
        match (action):
            case "1":
                print("___daily sale report___")
                sales = sale_service.get(filename)
                report = sale_service.get_report(sales)
                for key, value in report.items():
                    print(f"{key:<15} : {value}")
                input("press anything to continue")
            case "2":
                print("___add sale___")
                sale = {}
                sale["product"] = input("product name: ")
                sale["price"] = input("unit price: ")
                sale["quantity"] = input("quantity: ")
                sale_service.save_sale(sale, filename)
            case "3":
                break
    except:
        continue
