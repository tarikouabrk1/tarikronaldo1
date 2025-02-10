# TP : Structure d'un programme C++

Ce TP regroupe plusieurs exercices permettant d'explorer différents concepts fondamentaux du langage C++. L'objectif est de compiler et exécuter chaque exercice en utilisant des directives du préprocesseur.

## Organisation du TP

- Le fichier principal est \`main.cpp\`.
- L'exercice à compiler est sélectionné à l'aide de la macro \`EXO\`.
- Par défaut, l'exercice 1 est compilé.
- Pour compiler un autre exercice, il faut définir la macro \`EXO\` lors de la compilation (ex: \`-DEXO=2\` pour l'exercice 2).

## Compilation et Exécution

Pour compiler et exécuter le programme en sélectionnant un exercice spécifique, utilisez la commande suivante :

pour compiler
`sh
g++ main.cpp -o tp -DEXO=n 
`

Remplacez \`n\` par le numéro de l'exercice à compiler.

pour executer:

\`\`\`sh
./tp
\`\`\`
## Description des Exercices

### Exercice 1 : Analyse de la mémoire d’un tableau
- Déclare et initialise un tableau d'entiers.
- Affiche la taille totale du tableau, la taille d’un élément et le nombre total d’éléments.

### Exercice 2 : Estimation pour le service de nettoyage de tapis
- Demande à l'utilisateur le nombre de pièces à nettoyer.
- Calcule le coût total en tenant compte des taxes.
- Affiche une estimation détaillée.

### Exercice 3 : Calcul de la factorielle à la compilation avec \`constexpr\`
- Implémente une fonction \`constexpr\` récursive pour calculer la factorielle.
- Vérifie la validité du calcul avec \`static_assert\`.

### Exercice 4 : Variables Globales et Locales (Shadowing)
- Définit une variable globale et une variable locale du même nom.
- Affiche les deux valeurs en utilisant l'opérateur \`::\` pour accéder à la variable globale.

### Exercice 5 : Utilisation avancée des constantes
- Utilise \`const\`, \`constexpr\` et \`#define\` pour définir différentes constantes.
- Calcule l’aire d’un cercle et affiche les résultats.

### Exercice 6 : Détection d’overflow lors d’une multiplication
- Implémente une fonction \`safeMultiply\` pour vérifier si une multiplication provoque un overflow.
- Utilise \`std::numeric_limits\` pour éviter les dépassements de capacité.
- Teste la fonction avec différents cas.

## Exemple de Compilation et d’Exécution

Compilation de l'exercice 3 :
\`\`\`sh
g++ main.cpp -o tp -DEXO=3 && ./tp
\`\`\`

## Structure du Répertoire

Le projet doit être organisé comme suit :
\`\`\`
TP2_Nom_Prénom/
│── main.cpp
│── README.md
\`\`\`
