from functools import partial


STOP_TOKEN = '<STOP>'


class CharPrefixTree:
    def __init__(self):
        self.root_node = CharNode()

    def insert(self, word: str):
        """inserts the string `word` into the prefix tree."""
        current_node = self.root_node
        for char in word:
            if not current_node.has_child(char):
                current_node.add_child(char)
            current_node = current_node.get_child(char)
        current_node.add_child(STOP_TOKEN)

    def contains(self, word: str):
        """returns true/false if the given word exists in the prefix tree"""
        current_node = self.root_node
        for char in word:
            if not current_node.has_child(char):
                return False
            current_node = current_node.get_child(char=char)
        if not current_node.has_child(STOP_TOKEN):
            return False
        return True


class CharNode:
    def __init__(self):
        self.children = dict()

    def has_child(self, char: str):
        return char in self.children.keys()

    def add_child(self, char: str):
        self.children[char] = CharNode()

    def get_child(self, char: str):
        return self.children.get(
            char,
            ValueError(f'char {char} not in children')
        )


def test_trie_contains(word: str, expected: bool, trie: CharPrefixTree):
    pred = trie.contains(word)
    print(f'{word} in trie : {pred}')
    assert pred == expected


def main():
    trie = CharPrefixTree()
    trie.insert('abcd')

    trie_contains = partial(test_trie_contains, trie=trie)

    trie_contains('abcd', True)
    trie_contains('abc', False)
    trie_contains('abcdc', False)
    trie_contains('abcda', False)
    trie_contains('acbd', False)


if __name__ == '__main__':
    main()
