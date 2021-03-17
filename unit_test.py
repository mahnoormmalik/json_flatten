import unittest
import json

from json_flatten import json_flatten

class TestStringMethods(unittest.TestCase):

    def test_simple_json(self):
        json_data = '{ "a": 1, "b": true, "c": { "d": 3, "e": "test" } }'
        json_flattened = json_flatten(json_data)
        # print(isinstance(json_flattened, dict))
        self.assertEqual(json.loads(json_flattened), json.loads('{ "a": 1, "b": true, "c.d": 3, "c.e": "test" }'))
        print(json_flattened)


if __name__ == "__main__":
    unittest.main()