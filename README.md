# Offline JavaScript random and word password generators

Generate random or word-based passwords completely offline in
almost all web browsers that support JavaScript. This is for
anyone who prefers a completly offline generator with fairly
customizable options.

simply open the `*.html` files in your favorite browser and
generate as many passwords you want.

## Random

The `random.html` variant generates passwords from sets of
newline-separate strings. The default load uses the upper and
lower-cased English alphabet and digits 0-9. Users may alter any
of the strings to add or remove characters.

Duplicate character filtering is supported. Regardless of where
a character is defined the generated password will only allow
N duplicates of it (0 = ignore duplicate filtering).

## Words

The `words.html` variant generates passwords using words, and
optionally names, from the `dict.js` file. Users may wish to
generate their own `dict.js` for complete control. There is
an included `dict_gen.py` Python script which generates
English words and popular American names from lists found
on external Github projects.

The format is `prefix,word1,sepA,word2,...wordN,sepN,suffix`
where `prefix`, `suffix`, and `separator` are selected from
a user-specified set of strings. The number of words can
be selected, and optional enablement of proper names.

Finally, the words themselves can be mutated using different
upper- and lower- case algorithms. Note these algorithms have
only been tested with ascii and not with UTF-8 alphabets.
