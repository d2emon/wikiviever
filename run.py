#! /usr/bin/python3.5

import sys
import os
import config

def load_subpages(path):
    try:
        subs = next(os.walk(path))[1]
    except StopIteration:
        subs = []
    subs = list(filter(lambda f: not f.startswith('.') and not f.startswith('_'), subs))
    subs.sort()
    return subs

def print_subpages(subs):
    for i, f in enumerate(subs):
        print("{}.\t{}".format(i + 1, f))

def print_menu(path, subs):
    print("Path: {}".format(path))
    print("----")
    print("0.\t..")
    print_subpages(subs)
    print("----")
    print("Q.\tExit")
    print("----")
    i = input("Your selection:\t")
    print("----")
    return i.lower()

path = config.path
wikipath = []
subdir = ""

play = True
while play:
    patharr = [path] + wikipath
    print(patharr)
    p = os.path.join(*patharr)

    subs = load_subpages(p)
    optfile = os.path.join(p, "__page.opt")
    textfile = os.path.join(p, "__page.text")
    if os.path.isfile(optfile):
        f = open(optfile, "r")
        opt = f.read()
    else:
        opt = "No 'opt' file"
    if os.path.isfile(textfile):
        f = open(textfile, "r")
        text = f.read()
    else:
        text = "No 'text' file"
    print(opt)
    print(text)

    a = print_menu(p, subs)
    if a.lower().startswith('q'):
        play = False
    else:
        try:
            i = int(a) - 1
            if i < 0:
                if not wikipath:
                    raise ValueError
                subdir = '..'
                wikipath.pop()
            else:
                try:
                    subdir = subs[i]
                except IndexError:
                    raise ValueError
                wikipath.append(subdir)
                print(p)
            print(subdir)
        except ValueError:
            print("Wrong selection")
print("Bye!")
