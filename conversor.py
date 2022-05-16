def conversor(tipoPesos, valor_dolar):
    pesos = float(input("How many pesos "+tipoPesos+" have you got?:"))
    dolares = round(pesos/valor_dolar, 1)
    dolares = str(dolares)
    print("You have $"+dolares+" dollars")


menu = """
Welcome to exchage to coins 🤑
1-Pesos colombianos
2-Pesos argentinos
3-Pesos mexicanos

Select a option:
"""
opcion = input(menu)
if opcion == "1":
    valor_dolar = 3875
    conversor("colombianos", valor_dolar)
elif opcion == "2":
    valor_dolar = 65
    conversor("Argentinos", valor_dolar)
elif opcion == "3":
    valor_dolar = 20.11
    conversor("Mexicanos", valor_dolar)
else:
    print("Enter a correct option,  please")
