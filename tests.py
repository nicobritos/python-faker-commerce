"""Tests for faker-commerce."""

import unittest

from faker import Faker, Generator

import faker_commerce


class IntegrationTestCase(unittest.TestCase):
    """Integration tests."""

    def setUp(self):
        self.fake = Faker()
        self.fake.add_provider(faker_commerce.Provider)

    def test_integration(self):
        """Test integration with Faker."""
        result = self.fake.ecommerce_name()
        self.assertIsInstance(result, str)
        self.assertGreater(len(result), 1)

        """Test integration with Faker."""
        result = self.fake.ecommerce_category()
        self.assertIsInstance(result, str)
        self.assertGreater(len(result), 1)

        """Test integration with Faker."""
        result = self.fake.ecommerce_price()
        self.assertIsInstance(result, float)
        self.assertGreaterEqual(result, 1)
        self.assertLessEqual(result, 999999.99)


class EcommerceProviderTestCase(unittest.TestCase):
    """Provider test case."""

    # pylint: disable=protected-access

    def setUp(self):
        self.provider = faker_commerce.Provider(Generator())

    def test_no_duplicates(self):
        """Test lists in root of module don't contain duplicates."""
        for attr_name, attr in faker_commerce.__dict__.items():
            with self.subTest(attr_name=attr_name):
                if isinstance(attr, list):
                    self.assertEqual(len(attr), len(set(attr)))

    def test_price(self):
        """Test lists in root of module don't contain duplicates."""
        result = self.provider.ecommerce_price()
        self.assertIsInstance(result, float)
        self.assertGreaterEqual(result, 1)
        self.assertLessEqual(result, 999999.99)

    def test_category(self):
        """Test lists in root of module don't contain duplicates."""
        result = self.provider.ecommerce_category()
        self.assertIsInstance(result, str)
        self.assertGreater(len(result), 1)

    def test_name(self):
        """Test lists in root of module don't contain duplicates."""
        result = self.provider.ecommerce_name()
        self.assertIsInstance(result, str)
        self.assertGreater(len(result), 1)


if __name__ == "__main__":
    unittest.main()
