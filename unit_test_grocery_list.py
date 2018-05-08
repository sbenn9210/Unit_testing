import unittest
from grocery_app import Store

class Grocery_store_tested(unittest.TestCase):

    def setUp(self):
        print("SETUP")
        self.grocery_app = Store()

    def test_grocery_list(self):
        self.assertEqual(title, grocery_list)












if __name__ == '__main__':
    unittest.main()
