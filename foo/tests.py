from django.test import TestCase

# Create your tests here.


class FooTest(TestCase):
    def test_foo(self):
        self.assertEqual(1+1, 2)
