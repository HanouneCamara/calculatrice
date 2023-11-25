premier_nombre = int(input("Entrez un premier nombre : "))

deuxieme_nombre = int(input("Entrez un deuxième nombre : "))

operateur = input("Choisissez un opérateur(+ - * /) : ")

if operateur == "+":
    print(f"Le résultat de l'addition de {premier_nombre} avec {deuxieme_nombre} est égal à {premier_nombre + deuxieme_nombre} ")
elif operateur == "-":
    print(f"Le résultat de la soustraction de {premier_nombre} avec {deuxieme_nombre} est égal à {premier_nombre - deuxieme_nombre} ")
elif operateur == "*":
    print(f"Le résultat de la multiplication de {premier_nombre} avec {deuxieme_nombre} est égal à {premier_nombre * deuxieme_nombre} ")
elif operateur == "/":
    print(f"Le résultat de la division de {premier_nombre} avec {deuxieme_nombre} est égal à {premier_nombre / deuxieme_nombre} ")
else:
    print("Opérateur invalide")
