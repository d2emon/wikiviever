#! /usr/bin/python3.5

import config
import wiki

def subpages(w):
    subs = ""
    for i, f in enumerate(w.items):
        subs += "{}.\t{}\n".format(i + 1, f)
    return subs

def print_subpages(w):
    print(subpages(w))

def print_path(p):
    print("Path: {}".format(p))
    print("----")

def print_text(text):
    print(text)

def print_menu(w):
    print("----")
    print("0.\t..")
    print_subpages(w)
    print("----")
    print("Q.\tExit")
    print("----")
    i = input("Your selection:\t")
    print("----")
    return i.lower()

subdir = ""

play = True
w = wiki.Wiki(config.path)
while play:
    w.load()

    print_path(w.filepath())
    print_text(w.text)
    a = print_menu(w)

    if a.startswith('q'):
        play = False
    else:
        try:
            i = int(a) - 1
            if not w.subitem(i):
                raise ValueError
        except (IndexError, ValueError):
            print("Wrong selection")
print("Bye!")
