Scrabbler written in python.

Install: ``pip install scrabbler``

usage: ``scrabbler [-h] -d DICTIONARY [-l LIMIT] [--prefix PREFIX] [--allow_shorter] [--wildcard [WILDCARD]] [-r] [word]``

positional arguments:
  word                  Input word

optional arguments:
  -h, --help            show this help message and exit
  -d DICTIONARY, --dictionary DICTIONARY
                        Dictironary to search.
  -l LIMIT, --limit LIMIT
                        Limit the number of words printed.
  --prefix PREFIX       Only print words starting with the specified prefix.
  --allow_shorter       Don't require using all letters.

  --wildcard            Set a wildcard for the permutation matching (default: '?')

  -r, --regex           Print words matching regex.

