# 1. Créez des variables pour stocker votre nom, votre âge, et votre taille en mètres.

# 2. Calculez votre année de naissance approximative (sans tenir compte du mois).
# 3. Créez une chaîne de caractères qui dit "Je m'appelle [votre nom], j'ai [votre âge] ans et je mesure [votre taille] mètres."

# 4. Convertissez votre taille en centimètres et stockez le résultat dans une nouvelle variable.

# 5. Vérifiez si vous êtes majeur (18 ans ou plus) et stockez le résultat dans une variable booléenne.*/
nom = "karim"
age = 17
taille = 1.85
annee_naissance = 2025 - 23
print(annee_naissance)
chain = "je m'appelle " + nom + ", j'ai " + str(age) + " ans et je mesure " + str(taille) + " metre ."
if age < 18:
    var_bool = False
else:
    var_bool = True
if var_bool:
    print(chain)
    print("je suis majeur")
else:
    print(chain)
    print("je pas majeur mais mineur ")
i = 0
while i < 10:
    print("merci")
    i += 1
for i in range(10):
    print(i)
a = 0



