import argparse

import os

import re

DO_NOT_WANT_TO_LOAD_IN_MEMORY_LIMIT = 10 ** 7 #bytes


def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument("--file", "-f", type=str, required=True)
    return parser.parse_args()


def count_lines_in_file(path, buffer=DO_NOT_WANT_TO_LOAD_IN_MEMORY_LIMIT):
    lines_counted = 1
    with open(path) as inn:
        while True:
            content = inn.read(DO_NOT_WANT_TO_LOAD_IN_MEMORY_LIMIT)
            if len(content) == 0:
                break
            lines_counted += len(re.findall(r"\n", content))
    return lines_counted

if __name__ == "__main__":
    args = parse_args()
    assert os.path.exists(args.file), "No file '%s' found" % args.file
    assert not os.path.isdir(args.file), "Please specify path to a file, not to the directory."

    print(count_lines_in_file(args.file))


