# pytocomplete
sistema de autocomplete com [prefix tree](https://en.wikipedia.org/wiki/Trie) inspirado por [tsoding trie](https://gitlab.com/tsoding/trie).
## quickstart
executar o arquivo `main.py` vai abrir um shell
com os comandos linux.

```console
$ python3 main.py
$ # shell normal
$ echo "Ola, mundo!"
Ola, mundo!
```

executar com a flag `-s` vai tirar o shell,
deixando apenas um cmd com autocomplete
que guarda as palavras que voce escrever
para sugerir depois.

```console
$ python3 main.py -s
$ teste1
voce digitou `teste1`
$ teste2
voce digitou `teste2`
$ teste
teste1  teste2
```
