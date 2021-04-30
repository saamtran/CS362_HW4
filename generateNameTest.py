import unittest
import generateName
import math

class testCaseName(unittest.TestCase):
    def test_name(self):
        firstname = input(" == First Name: ")
        lastname = input(" == Last Name: ")
        expected = firstname + " " + lastname
        result = generateName.generateName(firstname, lastname)
        print(result)
        self.assertEqual(result, expected)

        firstname = input(" == First Name: ")
        lastname = input(" == Last Name: ")
        expected = firstname + " " + lastname
        result = generateName.generateName(firstname ,lastname)
        print(result)
        self.assertEqual(result, expected)

        firstname = input(" == First Name: ")
        lastname = input(" == Last Name: ")
        expected = firstname + " " + lastname
        result = generateName.generateName(firstname ,lastname)
        print(result)
        self.assertEqual(result, expected)



if __name__ == '__main__':
    unittest.main()