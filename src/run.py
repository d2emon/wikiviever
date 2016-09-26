#! /usr/bin/python

import config
from wiki.models import WikiPage


def subpages(w):
    subs = ""
    for i, f in enumerate(w.children):
        subs += "{}.\t{}\n".format(i + 1, f.title)
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
    try:
        i = raw_input("Your selection:\t")
    except(NameError):
        i = input("Your selection:\t")
    print("----")
    return str(i).lower()

subdir = ""

play = True
w = WikiPage(root=config.path)  # wikiobj.Wiki(config.path)
path = ''
while play:
    w.load(path=path)

    print_path(w.get_filepath())
    print_text(w.text)
    a = print_menu(w)

    if a.startswith('q'):
        play = False
    else:
        try:
            i = int(a) - 1
            if i < 0:
                path = w.get_upper()
                continue
            if not w.children[i]:
                raise ValueError
            c = w.children[i]
            path = c.path
        except (IndexError, ValueError):
            print("Wrong selection")
print("Bye!")
