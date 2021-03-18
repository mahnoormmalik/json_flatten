# JSON Flatten
> Script to flatten a JSON object

This script takes a JSON object and flattens it

## Algorithm Explanation:

Since JSON can be thought of as having a tree structure- with each value either being a leaf node or having 
child nodes- tree traversal algorithms can be applied to get the path to each leaf node/value.

In my script a stack is used for depth-first traversal of the JSON object. 

### The approach taken in this script is as follows:
* Initialise the stack with level 1 JSON keys
* while the stack is not empty:
    * pop an element from the stack
    * if element has child nodes, add the child node and the path to child node to the stack
    * if element has no child node, add the key/value pair to the output JSON

### Assumes the following:
* Input is a JSON object in text format following  [IETF RFC 8259](https://datatracker.ietf.org/doc/rfc8259/)
* JSON object does not contain arrays

### Example input and output for the script:

Input:
```sh
{
    "a": 1,
    "b": true,
    "c": {
        "d": 3,
        "e": "test"
    }
}
```

Output:
```sh
{
    "a": 1,
    "b": true,
    "c.d": 3,
    "c.e": "test"
}
```

## Usage example

The script uses command line input for JSON and outputs the result to the command line.

To run the script on linux:

```sh
cat <file.json> | python3 json_flatten.py
```

To run the test script on linux:
```sh
python3 unit_test.py -v
```

## Development setup

This script uses python 3. To install python use below:

OS X & Linux:

```sh
sudo apt-get update
sudo apt-get install python3.8
```

To test python version:
```sh
python3 --version
```
