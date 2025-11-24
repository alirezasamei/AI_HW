def get(filename):
    sales = []
    with open(filename, "r") as f:
        for sale in f.readlines():
            try:
                sale = sale.split(",")
                product = sale[0].strip()
                price = float(sale[1])
                quantity = float(sale[2])
                sales.append({"product": product, "price": price, "quantity": quantity})
            except:
                continue
    return sales


def get_report(sales):
    sale_count = len(sales)
    total_amount = 0
    grouped_sales = {}
    for sale in sales:
        total_amount += sale["price"] * sale["quantity"]
        product = sale["product"]
        quantity = sale["quantity"]
        grouped_sales[product] = grouped_sales.get(product, 0) + quantity
    max_saled = max(grouped_sales, key=grouped_sales.get)
    mean_amount = total_amount / sale_count
    return {
        "total_amount": total_amount,
        "sale_count": sale_count,
        "max_saled": max_saled,
        "mean_amount": round(mean_amount, 3),
    }


def save_sale(sale, filename):
    with open(filename, "a") as f:
        f.write(f"\n{sale["product"]}, {sale["price"]}, {sale["quantity"]}")
