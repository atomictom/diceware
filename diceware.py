#!/usr/bin/python3
# A small program for generating random, pronounceable usernames.
# Copyright (C) 2019 Thomas Manning
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <https://www.gnu.org/licenses/>.

import argparse
import math
import random
import re


class Options:
    def __init__(self, stats, phrases, words, blacklist_regex, word_file):
        self.stats = stats
        self.phrases = phrases
        self.words = words
        self.blacklist_regex = blacklist_regex
        self.word_file = word_file


def get_options():
    parser = argparse.ArgumentParser(description='Generate random passphrases',
                                     add_help=True)
    parser.add_argument('--stats',
                        '-v',
                        dest='stats',
                        default=True,
                        action='store_true',
                        help='Print stats about the generated passphrases.')
    parser.add_argument('--phrases',
                        '-p',
                        dest='phrases',
                        type=int,
                        default=10,
                        help='How many phrases to generate and display.')
    parser.add_argument('--words',
                        '-w',
                        dest='words',
                        type=int,
                        default=5,
                        help='How many words to generate in each phrase.')
    parser.add_argument('--blacklist_regex',
                        '-b',
                        dest='blacklist_regex',
                        type=str,
                        default=r"[A-Z']",
                        help='Any words to ignore from the word file.')
    parser.add_argument('--word_file',
                        '-f',
                        dest='word_file',
                        type=str,
                        default='/usr/share/dict/words',
                        help='The source of words for generating phrases.')
    args = parser.parse_args()
    return Options(stats=args.stats,
                   phrases=args.phrases,
                   words=args.words,
                   blacklist_regex=args.blacklist_regex,
                   word_file=args.word_file)


def get_words(options):
    with open(options.word_file) as word_file:
        words = list(word_file.readlines())

    excluded = 0

    def valid_word(word):
        nonlocal excluded
        blacklisted = re.search(options.blacklist_regex, word)
        if blacklisted:
            excluded += 1
        return not blacklisted

    return [word.strip() for word in words if valid_word(word)], excluded


def gen_passwords(options):
    r = random.SystemRandom()
    words, excluded = get_words(options)
    for i in range(options.phrases):
        password = ' '.join(r.choice(words) for _ in range(options.words))
        print(password)

    if options.stats:
        total_words = len(words)
        entropy = math.log(total_words**options.words) / math.log(2)
        print()
        print('Stats: ')
        print('  Source: {}'.format(options.word_file))
        print('  Used Words: {}'.format(len(words)))
        print('  Excluded words: {}'.format(excluded))
        print('  Entropy: {:.2f} bits per phrase'.format(entropy))


def main():
    options = get_options()
    gen_passwords(options)


if __name__ == '__main__':
    main()
