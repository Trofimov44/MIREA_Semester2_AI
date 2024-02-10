x = int(input("Введите число: "))
if x <= -5:
    print ("Принадлежит  (-infinity, -5)")
elif x >= 5:
    print("Принадлежит (5, +infinity)")
else:
    print("Принадлежит [-5, 5]")
