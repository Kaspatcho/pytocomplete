from typing import Dict, List, Optional, Union

class Tree:
    def __init__(self) -> None:
        self.end_word = False
        self.children: Dict[str, Tree] = {}

    def get(self, letter: str) -> Optional['Tree']:
        return self.children.get(letter)


def insert_text(root: Tree, text: str) -> Tree:
    if text == '':
        root.end_word = True
        return root

    letter = text[0]
    if root.children.get(letter) is None: root.children[letter] = Tree()

    root.children[letter] = insert_text(root.children[letter], text[1:])

    return root


def get_words_from_subtree(node: Tree, prefix: str = None) -> Union[str, List[str]]:
    '''
    returns all words in subtree `node` for given `prefix`

    Parameters:
        node   (Tree):   subtree to get words from
        prefix (str):    prefix to start word
    '''

    if prefix is None: prefix = ''
    if len(node.children) < 1: return prefix

    words = []

    for letter, child in node.children.items():
        possible_words = get_words_from_subtree(child, prefix + letter)
        if node.end_word: words.append(prefix)

        if isinstance(possible_words, list): words += possible_words
        else: words.append(possible_words)

    if len(words) < 2: return words[0]
    return words


def text_search(node: Tree, search: str, prefix: str = None) -> List[str]:
    '''
    returns all possible words in `node` for given `search`

    Parameters:
        node   (Tree):   root tree to search words
        search (str):    string to be searched in tree
        prefix (str):    prefix to start word
    '''

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
        words = get_words_from_subtree(child, prefix + key)
        if isinstance(words, list): all_words += words
        else: all_words.append(words)

    return all_words


if __name__ == '__main__':
    root = Tree()
    root = insert_text(root, 'hello')
    root = insert_text(root, 'helium')
    root = insert_text(root, 'hola')
    root = insert_text(root, 'metal')
    root = insert_text(root, 'mist')
    root = insert_text(root, 'mercury')

    possible_words = text_search(root, 'me')
    print(possible_words)
