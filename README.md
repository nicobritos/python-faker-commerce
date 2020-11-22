# python-faker-commerce
Provider for [Faker](https://faker.readthedocs.io/) which adds fake commerce product names, prices, categories and descriptions.

[![Issues](https://img.shields.io/github/issues/nicobritos/python-faker-commerce)](https://github.com/nicobritos/python-faker-commerce/issues)
![](https://img.shields.io/pypi/pyversions/faker-commerce.svg)
![](https://img.shields.io/github/license/nicobritos/python-faker-commerce)

# Installation

```
pipenv install faker-commerce
```

# Usage

## Python

```python
from faker import Faker

import faker_commerce

fake = Faker()
fake.add_provider(faker_commerce.Provider)
print(fake.ecommerce_name())  # prints a product name
```
