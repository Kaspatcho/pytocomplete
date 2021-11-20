import readline
from os import system, listdir
from sys import argv
from typing import List, Union
from tree import Tree, text_search, insert_text

no_shell = any((arg == '-s' for arg in argv))
root = Tree()

if not no_shell:
    programs = listdir('/bin')
    for program in programs: insert_text(root, program)


def complete_word(text: str, state: int) -> Union[List[str], str, None]:
    options = text_search(root, text)
    try:
        return options[state]
    except IndexError:
        return None

readline.set_completer(complete_word)
readline.parse_and_bind("tab: complete")

while True:
    value = input("$ ")
    word = value.split(' ')[0]
    insert_text(root, word)
    if not no_shell: system(value)
    else: print(f'voce digitou `{value}`')
