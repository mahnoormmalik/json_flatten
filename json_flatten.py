import json
import sys

from collections import deque

""" JSON conversion to flattened JSON

This script allows the user to convert a JSON passed as a commandline input 
into a flattened JSON object.

The script requires a valid JSON to be passed without arrays

This file can be imported as a module and contains the following functions:

        * json_flatten - returns flattened JSON
        * main - main funtion of the script

Author: Mahnoor Malik
""" 

def json_flatten(json_unflattened: str) -> str:
    """ Converts JSON objects to a flattened JSON object

    Assumes the following:
        - Input is a JSON object in text format following 
        - JSON object does not contain arrays

    Parameters
    ----------
    json_flattened : str
        JSON object to flatten

    Returns
    -------
    str
        A flattened JSON object
    
    Raises
    ------
    ValueError
        If the passed JSON object is not valid
    
    """

    try:
        json_output = {}
        stack = deque()

        json_input = json.loads(json_unflattened)
        for key, value in json_input.items():
            stack.append((None, key, value))

        stack.reverse()
        while stack:

            curr_element = stack.pop()

            path = curr_element[0]
            key = curr_element[1]
            value = curr_element[2]

            if isinstance(value, dict):
                new_path = path + "." + key if (path is not None) else key
                
                for k, val in value.items():
                    stack.append((new_path, k, val))
            else:
                if path is None:
                    json_output[key] = value
                else:
                    json_output[path + "." + key] = value

        return json.dumps(json_output)

    except ValueError:
        print("Error while decoding JSON. Please pass a valid JSON object")

if __name__ == "__main__":
    json_unflattened = input()

    print(json_unflattened)

    json_output = json_flatten(json_unflattened)

    print(json_output)
