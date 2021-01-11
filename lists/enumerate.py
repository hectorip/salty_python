# Cuando iteres una lista y necesites tanto el elemento como el índice
# usa la función enumerate


lista = ["Alex", "Héctor", "TheDojoMX"]

for (i, el) in enumerate(lista):
    print(f"{i} - {el}")
