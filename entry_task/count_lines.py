import argparse

import os


def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument("--file", "-f", type=str, required=True)
    return parser.parse_args()


if __name__ == "__main__":
    args = parse_args()
    assert os.path.exists(args.file), "No file '%s' found" % args.file
    assert not os.path.isdir(args.file), "Please specify path to a file, not to the directory."

