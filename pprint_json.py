import json
import argparse
import sys


def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument('file', help='Path to file with json data')
    return parser.parse_args()


def load_data(filepath):
    try:
        with open(filepath) as file:
            content = file.read()

        return json.loads(content)
    except (FileNotFoundError, json.decoder.JSONDecodeError, TypeError):
        return None


def prettify_json(data_object):
    return json.dumps(data_object, indent=4, ensure_ascii=False)


if __name__ == '__main__':
    args = parse_args()

    filepath = args.file
    data_object = load_data(filepath)

    if data_object is None:
        sys.exit('Failed to open json file (not found or incorrect format)')

    prettified_json = prettify_json(data_object)

    print(prettified_json)
