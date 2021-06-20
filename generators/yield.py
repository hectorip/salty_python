import random

"""
Usando generadores y yield
"""


def random_string():
    """
    Genera una cadena aleatoria en cada iteración
    """
    r = random.randint(0, 100)
    while True:
        yield f"hola{r}"
        r = random.randint(0, 100)


s = random_string()

for i in s:
    print(i)