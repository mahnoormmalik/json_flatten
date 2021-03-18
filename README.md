# JSON Flatten
> Script to flatten a JSON object

This script takes a JSON object and flattens it

### Assumes the following:
    - Input is a JSON object in text format following  IETF RFC 8259 (https://datatracker.ietf.org/doc/rfc8259/)
    - JSON object does not contain arrays

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
