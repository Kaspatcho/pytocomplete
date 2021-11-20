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


if __name__ == '__main__':
    root = Tree()
    root = insert_text(root, 'hello')
    root = insert_text(root, 'helium2')
    print(root)
