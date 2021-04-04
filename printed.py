vek = int (input ("Kolik ti je let?"))

if vek > 65:
    print ("Jsi v důchodu.")
elif vek > 19:
    print ("Jsi dospělý.")
elif vek > 15:
    print ("Jsi středoškolák.")
else:
    if vek > 0:
        print ("Jsi mladiství.")
    elif vek < 0:
        print ("Ještě ses nenarodil")
    else:
        print ("Jsi novorozeně.")
