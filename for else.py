cart=[10,20,30,40,50]
for item in cart:
    if item>=500:
        print("We cannot processs this order")
        break
    print(item)
else:print("congrats .... all items are processed successfully")
