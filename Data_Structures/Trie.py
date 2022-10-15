LATIN_ALPHABET_LENGTH = 26
LATIN_OFFSET = 97


class LatinTreeNode:
    def __init__(self, letter: str = None):
        self.letter = letter
        self.children = [None in range(LATIN_ALPHABET_LENGTH)]
        self.end_of_word = False


class Trie:

    def __init__(self):
        # root has no letter inside it
        self.root = LatinTreeNode(letter='#')

    def _search_any(self, word: str, is_full_word: bool) -> bool:
        curr = self.root
        for letter in word:
            letter_position: int = ord(letter) - LATIN_OFFSET
            print(f'letter pos: {letter_position}.\nLetter: {letter}')
            for i in range(26):
                print(f'index: {i}. letter: {curr.children[i].letter}')
            if curr.children[letter_position] is None:
                print('Here')
                return False
            curr = curr.children[letter_position]

        if is_full_word and not curr.end_of_word:
            return False
        return True

    def insert(self, word: str) -> None:
        curr = self.root
        for letter in word:
            letter_position: int = ord(letter) - LATIN_OFFSET
            if curr.children[letter_position] is None:
                new_node: LatinTreeNode = LatinTreeNode(letter=letter)
                curr.children[letter_position] = new_node
            curr = curr.children[letter_position]
        curr.end_of_word = True

    def search(self, word: str) -> bool:
        return self._search_any(word=word, is_full_word=True)

    def startsWith(self, prefix: str) -> bool:
        return self._search_any(word=prefix, is_full_word=False)
