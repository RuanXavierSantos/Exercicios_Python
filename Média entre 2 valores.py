a=float(input("Informe a primeira nota: "))
b=float(input("Informe a segunda nota: "))
b=(b+a)/2
if b>7:
    print("Passou suave")
elif b==7:
    print("Passou por pouco")
else:
    print("Reprovou, patético!")

