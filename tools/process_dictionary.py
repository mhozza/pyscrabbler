#! /usr/bin/env python
import argparse


def load_dictionary(dict_fname):
    with open(dict_fname) as f:
        for word in f.readlines():
            yield word.strip().lower()


def write_dictionary(dict_fname, words):
    with open(dict_fname, "w") as f:
        f.writelines(map(lambda word: f"{word}\n", words))


def main():
    parser = argparse.ArgumentParser(description="Makes all words lowercase")
    parser.add_argument("src", type=str, help="Source dictionary")
    parser.add_argument("dst", type=str, help="Destination dictionary")

    args = parser.parse_args()

    words = sorted(set(load_dictionary(args.src)))
    write_dictionary(args.dst, words)


if __name__ == "__main__":
    main()
