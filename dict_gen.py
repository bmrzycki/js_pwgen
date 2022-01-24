#!/usr/bin/env python3

from json import dumps
from textwrap import TextWrapper
from urllib.request import urlopen

def words(url, min_len, check=set()):
    s = set()
    with urlopen(url) as stream:
        for line in stream:
            w = line.decode("ascii").lower().strip()
            if (w.isalpha() and len(w) > min_len and
                w not in check):
                s.add(w)
    return s


def main():
    sets, min_len = {}, 3
    gh_raw = 'https://raw.githubusercontent.com/'
    sets['words'] = words(gh_raw +
                          'dolph/dictionary/master/ospd.txt',
                          min_len)
    sets['names'] = words(gh_raw +
                          'dominictarr/random-name/master/first-names.txt',
                          min_len, sets['words'])
    with open('dict.js', 'w') as stream:
        for name in sets:
            w = TextWrapper(width=70, subsequent_indent='\t')
            jsw = w.wrap(dumps(sorted(list(sets[name]))))
            stream.write(f"const {name} =\n\t")
            for i in range(len(jsw)):
                stream.write(jsw[i])
                if i + 1 == len(jsw):
                    stream.write(';')
                stream.write('\n')


if __name__ == '__main__':
    main()
