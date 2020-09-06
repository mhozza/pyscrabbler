import argparse
import sys
from string_algorithms.trie import Trie
from collections import deque


def build_trie(words):
    trie = Trie()

    for word in words:
        trie.add(word)

    return trie


def initialize_dictionary(dict_fname):
    print("Initializing dictionary...", file=sys.stderr)
    with open(dict_fname) as f:
        words = list(map(str.strip, f.readlines()))
    trie = build_trie(words)
    print("Done.", file=sys.stderr)
    return trie, words


def find_word(word, trie):
    return trie.find(word)


def print_subtree(word, trie, limit=None):
    root = trie.get_node(word)
    q = deque([(root, word)])

    while len(q):
        node, w = q.popleft()
        if node.is_word:
            print(w)
        for c, subnode in sorted(node.children.items()):
            if limit is not None and limit > 0:
                if subnode.is_word:
                    limit -= 1
                q.append((subnode, w + c))


def find_permutations(letters, trie, limit=None):
    pass


def find_regex(regex, words, limit=None):
    pass


def main(args):
    trie, words = initialize_dictionary(args.dictionary)
    word = args.word
    if args.subtree:
        print_subtree(word, trie, args.limit)
    else:
        print(find_word(word, trie))


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Scrabbler")
    parser.add_argument("word", type=str, help="Input word")
    parser.add_argument("-d", "--dictionary", type=str, help="Dictironary to search.")
    parser.add_argument(
        "-l", "--limit", type=int, help="Limit the number of words printed"
    )
    parser.add_argument(
        "--subtree", action="store_true", help="Print all words starting by [word]"
    )
    main(parser.parse_args())
