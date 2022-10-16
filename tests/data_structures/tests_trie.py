from typing import List

from data_structures.trie import *

# first list of inputs is commands (Trie, insert, search, startWith)
# second list is the arguments corresponding with the command
commands: List[str] = ["Trie", "insert", "search", "search", "startsWith", "insert", "search"]
arguments: List[List] = [[], ["apple"], ["apple"], ["app"], ["app"], ["app"], ["app"]]
for i in range(len(commands)):
    command = commands[i]
    related_arguments = arguments[i]
    if command == 'Trie':
        new_trie: Trie = Trie()
    elif command == 'insert':
        new_trie.insert(related_arguments[0])
        print(f'Inserted {related_arguments[0]}')
    elif command == 'search':
        print(f'Searching {related_arguments[0]}. Result: {new_trie.search(related_arguments[0])}')
    elif command == 'startsWith':
        print(f'Checking if starts with {related_arguments[0]}. Result: {new_trie.startsWith(related_arguments[0])}')


