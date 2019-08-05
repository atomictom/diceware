Diceware
========

This is a small Python 3 executable-file that generates random passphrases. The
easiest way to explain it is via an example:

```sh
$ diceware
fallow server saving reupholstering
pillages prop fierce gaps
mainstays lagging transited wheezier
upending choruses suffered invisibility
robberies plaintiffs moderation mobilize
fulcrums penitential cultivate peppered
betwixt hyaenas sieges badmouthed
redbreast snuggle hectored forebodings
horseman wackiness resoluteness detach
hogshead broomstick therapy destabilize

Stats:
  Used Words: 63006
  Excluded words: 36165
  Entropy: 63.77 bits per phrase
```

By default it generates a few (10) passphrases, each with 4 words using
`/usr/share/dict/words` with a regex to blacklist any with capital letters or
single apostrophes (i.e. it blacklists `[A-Z']`). It also reports on how many
words were used, how many were excluded, and what the effective entropy is
(assuming you told your adversary that you used this program to generate your
passphrases).

There are a few flags to customize the usage:

```sh
$ diceware -h
usage: diceware [-h] [--stats] [--phrases PHRASES] [--words WORDS]
                [--blacklist_regex BLACKLIST_REGEX] [--word_file WORD_FILE]

Generate random passphrases

optional arguments:
  -h, --help            show this help message and exit
  --stats, -v           Print stats about the generated passphrases.
  --phrases PHRASES, -p PHRASES
                        How many phrases to generate and display.
  --words WORDS, -w WORDS
                        How many words to generate in each phrase.
  --blacklist_regex BLACKLIST_REGEX, -b BLACKLIST_REGEX
                        Any words to ignore from the word file.
  --word_file WORD_FILE, -f WORD_FILE
                        The source of words for generating phrases.
```

It currently only works without any options on Unix distributions that have
`/usr/share/dict/words` but the word file used can be overridden with
`--word_file`. The default word file and blacklist regex lead to some fairly
complicated words and phrases (I learn new words anyway), so it might be
beneficial to use a custom word list restricted to a more reasonable subset of
words (like, say, [one of these from the EFF][EFF word list]). You can use the
stats to match some target bits of entropy.

[EFF word list]: https://www.eff.org/deeplinks/2016/07/new-wordlists-random-passphrases
