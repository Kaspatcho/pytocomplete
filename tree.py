from typing import Dict, Optional

class Tree:
    def __init__(self) -> None:
        self.children: Dict[str, Tree] = {}

    def get(self, letter: str) -> Optional['Tree']:
        return self.children.get(letter)


def insert_text(root: Tree, text: str) -> Tree:
    if text == '': return root

    letter = text[0]
    if root.children.get(letter) is None: root.children[letter] = Tree()

    root.children[letter] = insert_text(root.children[letter], text[1:])

    return root


def get_words(node: Tree, prefix: str = None) -> str:
    if prefix is None: prefix = ''
    if len(node.children) < 1: return prefix

    words = []

    for letter, child in node.children.items():
        words.append(get_words(child, prefix + letter))

    if len(words) < 2: return words[0]
    return words


def text_search(node: Tree, search: str, prefix: str = None) -> None:
    if prefix is None: prefix = ''
    root = node

    while search != '':
        letter = search[0]
        search = search[1:]
        prefix += letter
        node = node.get(letter)

    if node is None: return root

    all_words = []    

    for key, child in node.children.items():
        words = get_words(child, prefix + key)
        if isinstance(words, list): all_words += words
        else: all_words.append(words)

    return all_words


if __name__ == '__main__':
    root = Tree()
    root = insert_text(root, 'hello')
    root = insert_text(root, 'helium')
    root = insert_text(root, 'hola')
    root = insert_text(root, 'pedra')
    root = insert_text(root, 'pedro')
    possible_words = text_search(root, 'pedr')
    print(possible_words)
