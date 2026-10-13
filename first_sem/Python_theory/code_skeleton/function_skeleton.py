def get_price(item):
    if item == "idli":
        return 30
    elif item == "dosa":
        return 50
    elif item=="coffee":
        return 20
    elif item=="vada":
        return 10
    else:
        return 0


def item_cost(item, qty):
    global price
    price=get_price(item)
    return price*qty
    
def calculate_gst(amount, rate=0.05):
    gst=amount*rate
    return round(gst,2)


def generate_bill(subtotal, discount_percent=0):
    discount =subtotal*discount_percent
    amount_after_discount =subtotal-discount
    gst = calculate_gst(amount_after_discount)
    total =amount_after_discount +gst
    return discount, gst ,total


def split_bill(total, people):
    each_pays = total/people
    left_over = total % people
    return each_pays,round (left_over,2)


# ---------------- Main program ----------------
# A group of 3 friends orders 2 dosa and 3 coffee, with a 10% coupon.

subtotal1= item_cost('dosa',2) 
discount, gst, total1 = generate_bill(subtotal1,0.1)
subtotal2= item_cost('coffee',2) 
discount, gst, total2 = generate_bill(subtotal2,0.1)
each, extra = split_bill(total1,total2) 

print("Subtotal :", subtotal1)
print("Discount :", discount)
print("GST      :", gst)
print("Total    :", total1)
print("Subtotal :", subtotal2)
print("Discount :", discount)
print("GST      :", gst)
print("Total    :", total2)
print("Each pays:", each, "| Left over:", extra)