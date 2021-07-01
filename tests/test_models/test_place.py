#!/usr/bin/python3
'''Testing file for the class Place'''
import unittest
from models import place
from models.place import Place
import datetime


class TestPlace(unittest.TestCase):
    '''Class to test the class Place'''

    def test_init(self):
        '''Testing the creation of the class'''
        test = Place()
        self.assertTrue(isinstance(test, Place))
        self.assertTrue(hasattr(test, "id"))
        self.assertTrue(hasattr(test, "created_at"))
        self.assertTrue(hasattr(test, "updated_at"))
        test.name = "Holberton"
        self.assertEqual(test.name, "Holberton")

        test_dict = {"id": "ff02d7e0-4254-43b3-b867-d9decb0dda13",
                     "created_at": "2021-06-28T17:47:38.773238",
                     "updated_at": "2021-06-28T17:47:38.773248",
                     "__class__": "Place"}
        test_1 = Place(**test_dict)
        self.assertTrue(isinstance(test, Place))
        self.assertEqual(test_1.id, "ff02d7e0-4254-43b3-b867-d9decb0dda13")
        self.assertEqual(test_1.created_at, datetime.datetime(
            2021, 6, 28, 17, 47, 38, 773238))
        self.assertEqual(test_1.updated_at, datetime.datetime(
            2021, 6, 28, 17, 47, 38, 773248))
        self.assertTrue(isinstance(test_1.id, str))
        self.assertTrue(isinstance(test_1.created_at, datetime.datetime))
        self.assertTrue(isinstance(test_1.updated_at, datetime.datetime))

        test_dict = {}
        test_3 = Place(**test_dict)
        self.assertTrue(isinstance(test_3, Place))
        self.assertTrue(hasattr(test_3, "id"))
        self.assertTrue(hasattr(test_3, "created_at"))
        self.assertTrue(hasattr(test_3, "updated_at"))
        test_3.name = "Holberton"
        self.assertEqual(test_3.name, "Holberton")
        self.assertTrue(isinstance(test_3.id, str))
        self.assertTrue(isinstance(test_3.created_at, datetime.datetime))
        self.assertTrue(isinstance(test_3.updated_at, datetime.datetime))

    def test_str(self):
        ''' Function to test the __str__ instance method'''
        import sys
        from io import StringIO

        std_out = sys.stdout

        out = StringIO()
        sys.stdout = out
        test_1 = Place()
        print(test_1)
        output = out.getvalue()

        test_1_dict = test_1.__dict__

        for key, value in test_1_dict.items():
            if type(value) == datetime.datetime:
                value = value.isoformat()
            else:
                self.assertIn(str(key), output)
                self.assertIn(str(value), output)

        str_test = "[Place] ({})".format(test_1.id)
        self.assertIn(str_test, output)

    def test_save(self):
        '''Function to test the save instance method'''
        test_1 = Place()
        update_1 = test_1.updated_at
        test_1.save()
        update_2 = test_1.updated_at
        self.assertNotEqual(update_1, update_2)

    def test_to_dict(self):
        '''Function to test the instance method to_dict'''

        test_1 = Place()

        test_1_dict = test_1.to_dict()

        for key, value in test_1_dict.items():
            self.assertTrue(hasattr(test_1, key))

            if key == "created_at" or key == "updated_at":
                self.assertNotEqual(type(value), datetime.datetime)

        self.assertIn("__class__", test_1_dict.keys())

    def test_arguments(self):
        '''Funtion to test more arguments to the class Place'''
        with self.assertRaises(TypeError):
            test = Place()
            test.__str__("Perro")

        with self.assertRaises(TypeError):
            test.save("Perro")

        with self.assertRaises(TypeError):
            test.to_dict("Perro")

    def test_class_attributes(self):
        '''Function to test the class attributes'''
        self.assertTrue(hasattr(Place, "city_id"))
        self.assertTrue(hasattr(Place, "user_id"))
        self.assertTrue(hasattr(Place, "name"))
        self.assertTrue(hasattr(Place, "description"))
        self.assertTrue(hasattr(Place, "number_rooms"))
        self.assertTrue(hasattr(Place, "number_bathrooms"))
        self.assertTrue(hasattr(Place, "max_guest"))
        self.assertTrue(hasattr(Place, "price_by_night"))
        self.assertTrue(hasattr(Place, "latitude"))
        self.assertTrue(hasattr(Place, "longitude"))
        self.assertTrue(hasattr(Place, "amenity_ids"))
