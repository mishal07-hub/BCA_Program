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
    price=get_price(item)
    return price*qty
    
def calculate_gst(amount, rate=0.05):
    gst=amount*rate
    return round(gst,2)


def generate_bill(subtotal, discount_percent=0):
    discount =subtotal*(discount_percent)
    amount_after_discount =subtotal-discount
    gst = calculate_gst(amount_after_discount)
    total =amount_after_discount +gst
    return discount, gst ,total


def split_bill(total, people):
    each_pays = total/people
    left_over = total % people
    return each_pays,round (left_over,2)


# ---------------- Main program ----------------
#order items
cost1=item_cost('dosa',2) 
cost2=item_cost('coffee',1) 
cost3=item_cost('vada',2) 
subtotal= cost1+cost2+cost3
discount, gst, total = generate_bill(subtotal,0.1)
each_pays,left_over = split_bill(total,3) 

print("Subtotal :", subtotal)
print("Discount :", discount)
print("GST      :", gst)
print("Total    :", total)
print("--------------------")
print("each pays:",each_pays)
print("leftover:",left_over)
