import unittest
import json

from json_flatten import json_flatten

""" Testing of JSON converter to flatenned JSON

This script provides unit tests to test the json_flatten method in the json_flatten module.

This file can be run from the commandline as below:
    >python3 unit_test.py -v

It contains the following funtions:

        * main - main funtion of the script

It also contains the following classes:

        * main - test class which imports from unittest

Author: Mahnoor Malik
""" 

class TestJSONFlattenMethod(unittest.TestCase):
    """
    Class to test JSON flatten method inherits from unittest.Testcase
    ...

    Methods
    -------
    test_example_json
        Tests the example JSON provided in the assignment

    test_empty_json
        Tests the empty JSON corner case

    test_base_case_json
        Tests JSON with one key value pair

    test_invalid_json
        Tests an invalid JSON object 
    """

    def test_example_json(self):
        json_data = '{ "a": 1, "b": true, "c": { "d": 3, "e": "test" } }'
        json_flattened = json_flatten(json_data)
        self.assertEqual(json.loads(json_flattened), json.loads('{ "a": 1, "b": true, "c.d": 3, "c.e": "test" }'))
    
    def test_empty_json(self):
        json_data = '{ }'
        json_flattened = json_flatten(json_data)
        self.assertEqual(json.loads(json_flattened), json.loads('{ }'))
    
    def test_base_case_json(self):
        json_data = '{"a": 1}'
        json_flattened = json_flatten(json_data)
        self.assertEqual(json.loads(json_flattened), json.loads('{"a" : 1}'))

    def test_embedded_json(self):
        json_data = '{"a": {"b" : true } }'
        json_flattened = json_flatten(json_data)
        self.assertEqual(json.loads(json_flattened), json.loads('{"a.b" : true}'))

    def test_invalid_json(self):
        json_data = '{ "a": {"b" : true }'
        json_flattened = json_flatten(json_data)
        self.assertEqual(json_flattened[0], 404)

    def test_long_json(self):
        json_data = '{ "glossary": { "title": "example glossary", "GlossDiv": { "title": "S", "GlossList": { "GlossEntry": { "ID": "SGML", "SortAs": "SGML", "GlossTerm": "Standard Generalized Markup Language", "Acronym": "SGML", "Abbrev": "ISO 8879:1986", "GlossDef": { "para": "A meta-markup language, used to create markup languages such as DocBook.", "GlossSeeAlso": "GML" }, "GlossSee": "markup" } } } } }'
        json_flattened = json_flatten(json_data)
        self.assertEqual(json.loads(json_flattened), json.loads('{ "glossary.title": "example glossary", "glossary.GlossDiv.title": "S", "glossary.GlossDiv.GlossList.GlossEntry.ID": "SGML", "glossary.GlossDiv.GlossList.GlossEntry.SortAs": "SGML", "glossary.GlossDiv.GlossList.GlossEntry.GlossTerm": "Standard Generalized Markup Language", "glossary.GlossDiv.GlossList.GlossEntry.Acronym": "SGML", "glossary.GlossDiv.GlossList.GlossEntry.Abbrev": "ISO 8879:1986", "glossary.GlossDiv.GlossList.GlossEntry.GlossDef.para": "A meta-markup language, used to create markup languages such as DocBook.", "glossary.GlossDiv.GlossList.GlossEntry.GlossDef.GlossSeeAlso": "GML", "glossary.GlossDiv.GlossList.GlossEntry.GlossSee": "markup" }'))

    


if __name__ == "__main__":
    unittest.main()