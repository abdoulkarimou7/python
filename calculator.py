import random
print(f"Bienvenue dans Python 3 ! voici un nombre aléatoire entre 1 et 10 : {random.randint(1, 10)}")
def saluer(nom): return f"Bonjour, {nom} ! Bienvenue dans Pycharm."
print(saluer("Yarima"))

import logging

# Configuration de base du logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def add(a: float, b: float) -> float:
    result = a + b
    logging.info(f"Addition : {a} + {b} = {result}")
    return result
