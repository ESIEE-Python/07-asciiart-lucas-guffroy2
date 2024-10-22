#### Imports et définition des variables globales
import sys
sys.setrecursionlimit(10000)

#### Fonctions secondaires


def artcode_i(s):
    # votre code ici

    encoded = []
    current_char = s[0]
    count = 1

    # Parcourir la chaîne de caractères
    for i in range(1, len(s)):
        if s[i] == current_char:
            count += 1
        else:
            encoded.append((current_char, count))
            current_char = s[i]
            count = 1

    # Ajouter le dernier tuple
    encoded.append((current_char, count))

    return encoded

def artcode_r(s):
    # votre code ici

    # cas de base
    # recherche nombre de caractères identiques au premier
    # appel récursif

    if not s:
        return []

    def count_consecutive(s, char, index):
        if index == len(s) or s[index] != char:
            return index
        return count_consecutive(s, char, index + 1)

    count = count_consecutive(s, s[0], 1)

    return [(s[0], count)] + artcode_r(s[count:])
#### Fonction principale


def main():
    print(artcode_i('MMMMaaacXolloMM'))
    print(artcode_r('MMMMaaacXolloMM'))

if __name__ == "__main__":
    main()
