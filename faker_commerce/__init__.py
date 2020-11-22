"""Provider for Faker which adds fake microservice names."""

import random

import faker.providers

CATEGORIES = [
  "Books",
  "Movies",
  "Music",
  "Games",
  "Electronics",
  "Computers",
  "Home",
  "Garden",
  "Tools",
  "Grocery",
  "Health",
  "Beauty",
  "Toys",
  "Kids",
  "Baby",
  "Clothing",
  "Shoes",
  "Jewelery",
  "Sports",
  "Outdoors",
  "Automotive",
  "Industrial"
]

PRODUCT_DATA = {
    'material': [
        "Steel",
        "Wooden",
        "Concrete",
        "Plastic",
        "Cotton",
        "Granite",
        "Rubber",
        "Metal",
        "Soft",
        "Fresh",
        "Frozen"
    ],
    'product': [
        "Chair",
        "Car",
        "Computer",
        "Keyboard",
        "Mouse",
        "Bike",
        "Ball",
        "Gloves",
        "Pants",
        "Shirt",
        "Table",
        "Shoes",
        "Hat",
        "Towels",
        "Soap",
        "Tuna",
        "Chicken",
        "Fish",
        "Cheese",
        "Bacon",
        "Pizza",
        "Salad",
        "Sausages",
        "Chips"
    ],
    'adjective': [
        "Small",
        "Ergonomic",
        "Rustic",
        "Intelligent",
        "Gorgeous",
        "Incredible",
        "Fantastic",
        "Practical",
        "Sleek",
        "Awesome",
        "Generic",
        "Handcrafted",
        "Handmade",
        "Licensed",
        "Refined",
        "Unbranded",
        "Tasty",
        "New",
        "Gently Used",
        "Used",
        "For repair"
    ]
}


class Provider(faker.providers.BaseProvider):
    """Provider for Faker which adds fake microservice names."""

    def ecommerce_name(self):
        """Fake product names."""
        product = self.random_element(PRODUCT_DATA['product'])
        adjective = self.random_element(PRODUCT_DATA['adjective'])
        material = self.random_element(PRODUCT_DATA['material'])

        choices = [
            product,
            "".join([adjective, product]),
            "".join([material, product]),
            "".join([adjective, material, product]),
        ]

        names = random.choices(choices, k=1)
        return names[0]

    def ecommerce_category(self):
        return self.random_element(CATEGORIES)

    def ecommerce_price(self):
        return self.random_int(min=100, max=99999999) / 100
