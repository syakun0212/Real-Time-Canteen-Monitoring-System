import csv

#function to extract the information of menu items in the csv file into lists
def getitems(store_name):#(Yakun & Shannon)
    with open('foodcourt.csv', mode='r') as csv_file:
        foodcourt = csv.DictReader(csv_file)
        items = []
        if store_name == "MiniWok":
            for row in foodcourt:
                items.append(row["mini_wok_items"])
            return items
        elif store_name == "ChickenRice":
            for row in foodcourt:
                items.append(row["chicken_rice_items"])
            return items
        elif store_name == "Viet":
            for row in foodcourt:
                items.append(row["viet_items"])
            return items
        elif store_name == "Noodles":
            for row in foodcourt:
                items.append(row["noodles_items"])
            return items
        elif store_name == "Western":
            for row in foodcourt:
                items.append(row["western_items"])
            return items
        elif store_name == "Malay":
            for row in foodcourt:
                items.append(row["malay_items"])
            return items
        elif store_name == "Indian":
            for row in foodcourt:
                items.append(row["indian_items"])
            return items
        elif store_name == "Salad":
            for row in foodcourt:
                items.append(row["salad_items"])
            return items
        elif store_name == "Chinese":
            for row in foodcourt:
                items.append(row["chinese_items"])
            return items
        elif store_name == "Claypot":
            for row in foodcourt:
                items.append(row["claypot_items"])
            return items
        elif store_name == "ClaypotMon":
            for row in foodcourt:
                items.append(row["claypot_monitems"])
            return items
        elif store_name == "ClaypotTues":
            for row in foodcourt:
                items.append(row["claypot_tuesitems"])
            return items
        elif store_name == "ClaypotWed":
            for row in foodcourt:
                items.append(row["claypot_weditems"])
            return items
        elif store_name == "ClaypotThurs":
            for row in foodcourt:
                items.append(row["claypot_thursitems"])
            return items
        elif store_name == "ClaypotFri":
            for row in foodcourt:
                items.append(row["claypot_friitems"])
            return items
        elif store_name == "ClaypotSat":
            for row in foodcourt:
                items.append(row["claypot_satitems"])
            return items




#function to extract the information of menu prices in the csv file into lists
def getprice(store_name):#(Yakun & Shannon)
    with open('foodcourt.csv', mode='r') as csv_file:
        foodcourt = csv.DictReader(csv_file)
        price = []
        if store_name == "MiniWok":
            for row in foodcourt:
                price.append(row["mini_wok_price"])
            return price
        elif store_name == "ChickenRice":
            for row in foodcourt:
                price.append(row["chicken_rice_price"])
            return price
        elif store_name == "Viet":
            for row in foodcourt:
                price.append(row["viet_price"])
            return price
        elif store_name == "Noodles":
            for row in foodcourt:
                price.append(row["noodles_price"])
            return price
        elif store_name == "Western":
            for row in foodcourt:
                price.append(row["western_price"])
            return price
        elif store_name == "Malay":
            for row in foodcourt:
                price.append(row["malay_price"])
            return price
        elif store_name == "Indian":
            for row in foodcourt:
                price.append(row["indian_price"])
            return price
        elif store_name == "Salad":
            for row in foodcourt:
                price.append(row["salad_price"])
            return price
        elif store_name == "Chinese":
            for row in foodcourt:
                price.append(row["chinese_price"])
            return price
        elif store_name == "Claypot":
            for row in foodcourt:
                price.append(row["claypot_price"])
            return price
        elif store_name == "ClaypotMon":
            for row in foodcourt:
                price.append(row["claypot_monprice"])
            return price
        elif store_name == "ClaypotTues":
            for row in foodcourt:
                price.append(row["claypot_tuesprice"])
            return price
        elif store_name == "ClaypotWed":
            for row in foodcourt:
                price.append(row["claypot_wedprice"])
            return price
        elif store_name == "ClaypotThurs":
            for row in foodcourt:
                price.append(row["claypot_thursprice"])
            return price
        elif store_name == "ClaypotFri":
            for row in foodcourt:
                price.append(row["claypot_friprice"])
            return price
        elif store_name == "ClaypotSat":
            for row in foodcourt:
                price.append(row["claypot_satprice"])
            return price