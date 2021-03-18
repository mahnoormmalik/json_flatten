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

        #stack used to traverse the JSON depth-first
        stack = deque()

        json_input = json.loads(json_unflattened)

        #stack initialisation 
        #stack tuple format: (path to key, key, value)
        for key, value in json_input.items():
            stack.append((None, key, value))

        #stack traversal: pops the top key and appends the element to 
        #output if no child node otherwise adds the children to stack
        while stack:

            curr_element = stack.pop()

            path_to_key = curr_element[0]
            key = curr_element[1]
            value = curr_element[2]

            if isinstance(value, dict):
                new_path = path_to_key + "." + key if (path_to_key is not None) else key
                
                for k, val in value.items():
                    stack.append((new_path, k, val))
            else:
                if path_to_key is None:
                    json_output[key] = value
                else:
                    json_output[path_to_key + "." + key] = value

        return json.dumps(json_output)

    except ValueError:
        print("Error while decoding JSON. Please pass a valid JSON object")
        return 400, "Error while parsing"

if __name__ == "__main__":
    json_unflattened = input()

    print(json_unflattened)

    json_output = json_flatten(json_unflattened)

    print(json_output)
