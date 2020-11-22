#!/usr/bin/env python3
#
import io
import re
import os
import sys
import pdb

# filename = "/home/wd/wordcount.log"

def count_file(filename):

    f = io.open(filename, 'r', encoding='utf8')
    # print(len(f.read()))

    # First find all 'normal' words and interpunction
    # '[\x21-\x2f]' includes most interpunction, change it to ',' if you only need to match a comma

    s = f.read()
    count = 0
    # count = len(re.findall(r'\\w+|[\\x21-\\x2]', s))

    for word in s:
        for ch in word:
            # see https://stackoverflow.com/a/11415841/1248554 for additional ranges if needed
            if 0x4e00 < ord(ch) < 0x9fcc:
                count += 1

    return count

    # https://stackoverflow.com/questions/16528005/find-the-length-of-a-sentence-with-english-words-and-chinese-characters


# count all files in specific directory

def count_directory(directory):
    ''' count files in a directory'''


def walk(top, maxdepth):
    dirs, nondirs = [], []
    for name in os.listdir(top):
        (dirs if os.path.isdir(os.path.join(top, name)) else nondirs).append(name)
    yield top, dirs, nondirs
    if maxdepth > 1:
        for name in dirs:
            for x in walk(os.path.join(top, name), maxdepth-1):
                yield x


# for x in walk(".", 2):
#     print(x)


if __name__ == "__main__":

    # pdb.set_trace()

    if len(sys.argv) != 4:
        print("usage: python chinese_wc.py [dir] [depth] [appendix]\r\nlike: python chinese_wc.py ~/Documents/org 3 \'.org\'")
    else:
        # print("This is the name of the script: ", sys.argv[0])
        # print("Number of arguments: ", len(sys.argv))
        # print("The arguments are: " , str(sys.argv))
        dir = sys.argv[1] # directory
        appendix = sys.argv[3]

        print("the directory is: ", dir)

        files = walk(dir, int(sys.argv[2]))
        for f in files:
            # print(f)
            for e in f[2]:
                # print(e)
                if e.endswith(appendix):
                    print("{count}\t{filename}".format(filename=f[0]+'/'+e,count=count_file(f[0]+'/'+e)))
