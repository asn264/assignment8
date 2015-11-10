from unittest import TestCase
from Interactions import *

class Parse_for_List_Test(TestCase):

    #Ensure an empty list is returned when there are no opening and closing brackets
    def test_no_brackets(self):
	self.assertEqual(parse_for_list("10,100"), [])

    #Ignore extra whitespace
    def test_whitespace(self):
        self.assertEqual(parse_for_list("[ 10, 100  ]"), parse_for_list("[10,100]"))

    #Ensure an empty list is returned if there is an unnecessary comma at the end
    def test_commas(self):
        self.assertEqual(parse_for_list("[10,100,]"), [])
    
    #Ensure an empty list is returned for decimal values with otherwise correct formatting
    def test_decimals(self):
        self.assertEqual(parse_for_list("[10, 100.0]"), [])

    #Ensure an empty list is returned for decimal values with otherwise correct formatting
    def test_negatives(self):
	self.assertEqual(parse_for_list("[10,-100]"), [])
    
    #Ensure it works!
    def test_casting(self):
        self.assertEqual(parse_for_list("[10,100,1000]"), [10,100,1000])

class Parse_for_Int_Test(TestCase):

    #Ensure it works
    def test_casting(self):
	self.assertEqual(parse_for_int("10"), 10)
    
    #Ensure it works with whitespace
    def test_whitespace(self):
	self.assertEqual(parse_for_int("    10     "), 10)

    #Ensure it rejects alphabet characters
    def test_alphabetchar(self):
	self.assertEqual(parse_for_int("askd"), None)

    #Ensure it rejects floats
    def test_floats(self):
	self.assertEqual(parse_for_int("10.0"), None)

    #Ensure it rejects negative integers
    def test_negative(self):
        self.assertEqual(parse_for_int("-5"), None)

    #Ensure it rejects 0
    def test_zero(self):
	self.assertEqual(parse_for_int("0"), None)
