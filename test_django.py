import unittest
import django
#  django-admin startproject basics_django

class MyTestCase(unittest.TestCase):
    def test_something(self):
        print(django.get_version())


if __name__ == '__main__':
    unittest.main()
