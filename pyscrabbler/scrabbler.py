import argparse
import sys
from string_algorithms.trie import Trie
from collections import deque, Counter
import re


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
                    print(w)
                    limit -= 1
                q.append((subnode, w + c))


def find_permutations(word, trie, use_all_letters=True, limit=None):
    root = trie.root
    letters = Counter(word)
    q = deque([(root, "", letters)])

    while len(q):
        node, w, l = q.popleft()
        for c, subnode in sorted(
            filter(lambda item: l[item[0]] > 0, node.children.items())
        ):
            if limit is not None and limit > 0:
                new_w = w + c
                if (not use_all_letters or len(new_w) == len(word)) and subnode.is_word:
                    print(new_w)
                    limit -= 1
                q.append((subnode, new_w, l - Counter(c)))


def find_regex(regex, words, limit=None):
    pattern = re.compile(regex)
    words = filter(lambda w: pattern.match(w), words)
    for i, w in enumerate(words):
        if limit is not None and i > limit:
            break
        print(w)


def main(args):
    trie, words = initialize_dictionary(args.dictionary)
    word = args.word
    if args.subtree:
        print_subtree(word, trie, limit=args.limit)
    elif args.permutations:
        find_permutations(
            word, trie, use_all_letters=not args.allow_shorter, limit=args.limit
        )
    elif args.regex:
        find_regex(word, words, limit=args.limit)
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
    parser.add_argument(
        "-p", "--permutations", action="store_true", help="Print all permutations"
    )
    parser.add_argument(
        "--allow_shorter", action="store_true", help="Don't require using all letters."
    )
    parser.add_argument(
        "-r", "--regex", action="store_true", help="Print words matching regex."
    )

    main(parser.parse_args())
