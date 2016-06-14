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
    return i

path = config.path
wikipath = []
subdir = ""

play = True
while play:
    patharr = [path] + wikipath
    print(patharr)
    # patharr.append(subdir)
    p = os.path.join(*patharr)
    subs = load_subpages(p)
    a = print_menu(p, subs)
    if a.lower().startswith('q'):
        play = False
    else:
        try:
            i = int(a) - 1
            if i < 0:
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
