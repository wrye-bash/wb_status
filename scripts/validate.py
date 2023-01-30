#!/bin/python3
import json
import sys
from pathlib import Path

from jsonschema import validate

def main(args):
    if len(args) < 3:
        print('Syntax: validate.py <schema> <file(s)>', file=sys.stderr)
        sys.exit(1)
    schema_path = Path(args[1])
    print(f':: Parsing schema {schema_path}')
    with open(schema_path, 'r', encoding='utf-8') as ins:
        schema = json.load(ins)
    json_paths = list(map(Path, args[2:]))
    json_data = []
    for json_path in json_paths:
        print(f':: Parsing JSON file {json_path}')
        with open(json_path, 'r', encoding='utf-8') as ins:
            json_data.append(json.load(ins))
    print(':: JSON parsed successfully, running schema validation')
    for j in json_data:
        validate(j, schema)
    print(':: All files validated successfully')

if __name__ == '__main__':
    main(sys.argv)
