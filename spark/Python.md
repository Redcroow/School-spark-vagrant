### Uppercase a string


```python
str_1 = "This is a string"
str_1 = str_1.upper()
print(str_1)
```

    THIS IS A STRING


### Capitalize a string


```python
str_2 = "new string"
str_2_cap = str_2.capitalize()
print(str_2_cap)
```

    New string


### Display the city 


```python
my_dict = {
    'company': 'nbs',
    'ceo': 'joe',
    'city': 'rome'
}
my_dict['city']
```




    'rome'



### Capitalize the value of a dict


```python
my_dict = {
    "name": "edison",
    "city": "chicago",
}
my_dict['city'] = my_dict['city'].capitalize()
my_dict
```




    {'name': 'edison', 'city': 'Chicago'}



### split a string to words


```python
str_3 = "Please split this sentence to words"
str_4 = str_3.split()
str_4
```




    ['Please', 'split', 'this', 'sentence', 'to', 'words']



### Strip the words


```python
word_1 = 'hi!'
word_2 = ', world'

print(word_1.strip('!'))
print(word_2.strip(', '))
```

    hi
    world


### Split the sentence, strip words and lower them


```python
str_4 = "Please, split This Sentence to words!"

# Split the sentence into words
words = str_4.split()

# Strip and lowercase each word
stripped_lower_words = [word.strip(',!').lower() for word in words]

print(stripped_lower_words)n
```

    ['please', 'split', 'this', 'sentence', 'to', 'words']



```python

```
