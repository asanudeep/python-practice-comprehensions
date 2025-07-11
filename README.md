# Comprehensions in Python

## Introduction
Comprehensions are a powerful tool in python. This repository provides
three simple excercises you can practice to get familiar with comprehenions.

### List Comprehensions

```python
squared_list = [item ** 2 for item in range(10)]
```

### Dictionary Comprehensions

```python
squared_dict = {key: value ** 2 for key, value in enumerate(range(10))}
```

### Set Comprehensions

```python
squared_set = {item ** 2 for item in range(10)}
```

### Generator Expression

```python
squared_generator = (item ** 2 for item in range(10))
```

---
[ ] TODO: Write basic introduction to comprehensions