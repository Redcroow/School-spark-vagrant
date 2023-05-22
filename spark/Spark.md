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
        <dd><code>PySparkShell</code></dd>
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
#Exercice

# Créer la liste d'entiers
my_list = list(range(1, 10))

# Créer RDD à partir de la liste
rdd = sc.parallelize(my_list)

# Appliquer la première transformation
rdd = rdd.map(lambda x: x - 1)

# Appliquer la deuxième transformation
rdd = rdd.map(lambda x: x * 2)

# crée une liste à partir des éléments du RDD
result = rdd.collect()

# Afficher le résultat final
print(result)

```

    [0, 2, 4, 6, 8, 10, 12, 14, 16]





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

    RDD avec les doublons supprimés : [10, 8, 6, 4, 5, 3, 7]
    RDD avec les nombres pairs : [10, 8, 6, 4]
    RDD avec les nombres impairs : [5, 3, 7]
    Somme des éléments du RDD avec les nombres pairs : 28
    Somme des éléments du RDD avec les nombres impairs : 15



```python

```
