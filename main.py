import readline
from os import system
from sys import argv
from tree import Tree, text_search, insert_text

root = Tree()

no_shell = any((arg == '-s' for arg in argv))

def completer(text, state):
    options = text_search(root, text)
    try:
        return options[state]
    except IndexError:
        return None

readline.set_completer(completer)
readline.parse_and_bind("tab: complete")

while True:
    value = input("$ ")
    word = value.split(' ')[0]
    insert_text(root, word)
    if not no_shell: system(value)
    else: print(f'voce digitou `{value}`')
