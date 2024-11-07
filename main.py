buyprice=100
soldprice=120

if (soldprice>buyprice):
    profit = soldprice - buyprice
    print("profit is:",profit)
else:
    loss=buyprice - soldprice
    print("Loss is",loss)