# python-faker-commerce
Provider for [Faker](https://faker.readthedocs.io/) which adds fake commerce product names, prices, categories and descriptions.

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
