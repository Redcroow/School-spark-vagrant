# Exercice


```python
#Exercice1
my_list = [1,2,3,4,5]

# Initialiser la variable pour stocker la somme
sum = 0

# Parcourir la liste et ajouter chaque élément à la somme
for num in my_list:
    sum += num

# Afficher la somme
print("La somme des éléments de la liste est :", sum)
```

    La somme des éléments de la liste est : 15



```python
#Exercice2
my_list = [1,2,3,4,5]
my_list2 = [3,4,5,2,1,9,8]

# Initialiser la liste pour stocker la somme de chaque élément
result = []

# Parcourir chaque élément correspondant dans les deux listes et ajouter la somme à la liste de résultats
for i in range(len(my_list)):
    if i < len(my_list2):
        sum = my_list[i] + my_list2[i]
    else:
        sum = my_list[i]
    result.append(sum)

# Ajouter les éléments restants de my_list2 à la fin de la liste de résultats
result.extend(my_list2[len(my_list):])

# Afficher la liste de résultats
print(result)
```

    [4, 6, 8, 6, 6, 9, 8]



```python
#Exercice3
person = [
    {
        'name': 'ali',
        'age' : 14
    },
        {
        'name': 'alice',
        'age' : 16
    },
        {
        'name': 'dave',
        'age' : 4
    },
]
def age(personnes):
    personne_max = personnes[0]
    for personne in personnes:
        if personne['age'] > personne_max['age']:
            personne_max = personne
    return personne_max
print(age(person))
```

    {'name': 'alice', 'age': 16}


# Lecons


```python
#SPARK
sc
```





<div>
    <p><b>SparkContext</b></p>

    <p><a href="http://10.0.2.15:4040">Spark UI</a></p>

    <dl>
      <dt>Version</dt>
        <dd><code>v3.2.4</code></dd>
      <dt>Master</dt>
        <dd><code>local[*]</code></dd>
      <dt>AppName</dt>
        <dd><code>Comptage du mot</code></dd>
    </dl>
</div>





```python
#cours
my_list = [i for i in range(1,11)]
print('Ma liste : ',my_list)

rdd = sc.parallelize(my_list)
print('parallelize method : ',type(rdd))

result = rdd.collect()
print('collect method : ',result)

print('First Action : ',rdd.first())
print('Take Action : ',rdd.take(3))

rdd_inc = rdd.map(lambda x: x+1)
print('Lambda Action for transform list : ',rdd_inc.collect())

```

    Ma liste :  [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    parallelize method :  <class 'pyspark.rdd.RDD'>
    collect method :  [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    First Action :  1
    Take Action :  [1, 2, 3]
    Lambda Action for transform list :  [2, 3, 4, 5, 6, 7, 8, 9, 10, 11]


# Exercice


```python
# Créer la liste d'entiers
my_list = list(range(1, 10))

# Créer RDD à partir de la liste
rdd = sc.parallelize(my_list)

# Appliquer la première transformation
rdd = rdd.map(lambda x: x - 1)

# Appliquer la deuxième transformation
rdd = rdd.map(lambda x: x * 2)

# Créer une liste à partir des éléments du RDD
result = rdd.collect()

# Afficher le résultat final
print(result)


```


    ---------------------------------------------------------------------------

    TypeError                                 Traceback (most recent call last)

    Cell In[62], line 2
          1 # Créer la liste d'entiers
    ----> 2 my_list = list(range(1, 10))
          4 # Créer RDD à partir de la liste
          5 rdd = sc.parallelize(my_list)


    TypeError: 'list' object is not callable



```python
#Exercice
# Importer la bibliothèque random pour générer les nombres aléatoires
import random

# Créer la liste d'entiers aléatoires
my_list = [random.randint(1, 10) for _ in range(20)]

# Créer RDD à partir de la liste
rdd = sc.parallelize(my_list)

# Supprimer les doublons
rdd_deduplicated = rdd.distinct()

# Créer deux RDDs : un avec les nombres pairs et l'autre avec les nombres impairs
rdd_even = rdd_deduplicated.filter(lambda x: x % 2 == 0)
rdd_odd = rdd_deduplicated.filter(lambda x: x % 2 != 0)

# Somme des éléments de chaque RDD
sum_even = rdd_even.sum()
sum_odd = rdd_odd.sum()

# Afficher les résultats
print("RDD avec les doublons supprimés :", rdd_deduplicated.collect())
print("RDD avec les nombres pairs :", rdd_even.collect())
print("RDD avec les nombres impairs :", rdd_odd.collect())
print("Somme des éléments du RDD avec les nombres pairs :", sum_even)
print("Somme des éléments du RDD avec les nombres impairs :", sum_odd)

```

    RDD avec les doublons supprimés : [10, 4, 1, 5, 7, 3]
    RDD avec les nombres pairs : [10, 4]
    RDD avec les nombres impairs : [1, 5, 7, 3]
    Somme des éléments du RDD avec les nombres pairs : 14
    Somme des éléments du RDD avec les nombres impairs : 16


# 15/05/2023


```python
list = [ [1,2,3], [3,4,5], [6,7,8] ]

def inc_list_element(x: list) -> list: 
    return [i+1 for i in x] 
flat_map = sc.parallelize(list).flatMap(inc_list_element).collect() 
_map = sc.parallelize(list).map(inc_list_element).collect() 
print(f"FlatMap: {flat_map}") 
print(f"Map: {_map}")
```

    FlatMap: [2, 3, 4, 4, 5, 6, 7, 8, 9]
    Map: [[2, 3, 4], [4, 5, 6], [7, 8, 9]]


### Exo 1


```python
from typing import List, Tuple
cars: List[Tuple[str,str,str,int]] = [
    ('Volkswagen', 'Golf', 'Yellow', 2018),
    ('Toyota', 'Yaris', 'White', 2020),
    ('Volkswagen', 'Golf', None, 2010),
    ('Peugeot', '208', 'Green', 2005),
    ('Honda', None, 'Blue', 2003),
]

def filter_and_sort_cars(cars):
    filtered_cars = [car for car in cars if all(value is not None for value in car)]
    sorted_cars = sorted(filtered_cars, key=lambda car: car[3])
    
    return sorted_cars

rdd = sc.parallelize(cars).collect()
result = filter_and_sort_cars(rdd) 

for car in result:
    print(car)
```

    ('Peugeot', '208', 'Green', 2005)
    ('Volkswagen', 'Golf', 'Yellow', 2018)
    ('Toyota', 'Yaris', 'White', 2020)


### Exo 2


```python
mot_recherche = 'the'
fichier = 'pg69794.txt'

# Lire le fichier en tant que RDD
lines = sc.textFile(fichier)

# Compter le nombre d'occurrences du mot 'the'
occurrences = lines.flatMap(lambda ligne: ligne.split(' ')).filter(lambda mot: mot == mot_recherche).count()

# Afficher le résultat
print(f"Le mot '{mot_recherche}' apparaît {occurrences} fois dans le fichier.")

```

    Le mot 'the' apparaît 170 fois dans le fichier.


### Exo 3 : nombre de mots


```python
fichier = 'pg69794.txt'

# Lire le fichier en tant que RDD
lines = sc.textFile(fichier)

# Compter le nombre total de mots
word_count = lines.flatMap(lambda ligne: ligne.split(' ')).count()

# Afficher le résultat
print(f"Le fichier contient un total de {word_count} mots.")
```

    Le fichier contient un total de 52518 mots.


### nmbre de lignes


```python
fichier = 'pg69794.txt'

# Lire le fichier en tant que RDD de lignes
lines = sc.textFile(fichier)

# Compter le nombre de lignes
line_count = lines.count()

# Afficher le résultat
print(f"Le fichier contient un total de {line_count} lignes.")
```

    Le fichier contient un total de 5119 lignes.


### texte transformé


```python
import re

fichier = 'pg69794.txt'

# Lire le fichier en tant que RDD de lignes
lines = sc.textFile(fichier)

# Supprimer la ponctuation et mettre les mots en minuscules
cleaned_lines = lines.map(lambda line: re.sub(r'[^\w\s]', '', line)
                          .lower()
                          
                         )

print("Affichage des 10 première lignes apres la transformation")
print("-----")

# Afficher les 10 premières lignes pour vérification
for line in cleaned_lines.take(10):
    print(line)
```

    Affichage des 10 première lignes apres la transformation
    -----
    the project gutenberg ebook of de pontoise à stamboul by edmond
    about
    
    this ebook is for the use of anyone anywhere in the united states and
    most other parts of the world at no cost and with almost no restrictions
    whatsoever you may copy it give it away or reuse it under the terms
    of the project gutenberg license included with this ebook or online at
    wwwgutenbergorg if you are not located in the united states you
    will have to check the laws of the country where you are located before
    using this ebook


### 10 mots les plus utilisé


```python
import re

fichier = 'pg69794.txt'

# Lire le fichier en tant que RDD de lignes
lines = sc.textFile(fichier)

# Diviser les lignes en mots et les compter
word_counts = lines.flatMap(lambda line: re.sub(r'[^\w\s]', '', line).lower().split()) \
                   .map(lambda word: (word, 1)) \
                   .reduceByKey(lambda x, y: x + y)

# Trier les mots par nombre d'occurrences décroissant
sorted_word_counts = word_counts.sortBy(lambda wc: wc[1], ascending=False)

# Afficher les 10 mots les plus utilisés
print("Les 10 mots les plus utilisés :")
for word, count in sorted_word_counts.take(10):
    print(f"{word}: {count}")
```

    Les 10 mots les plus utilisés :
    de: 2300
    et: 1395
    la: 1295
    le: 1082
    les: 1050
    à: 921
    un: 676
    des: 608
    que: 603
    nous: 603



```python
people = spark.read.json('file.json')

people.select('*').show()
```

    +----+-------+
    | age|   name|
    +----+-------+
    |null|Michael|
    |  30|   Andy|
    |  19| Justin|
    +----+-------+
    



```python

```
