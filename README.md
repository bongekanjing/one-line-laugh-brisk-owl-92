# The One-Line Laugh

One funny line, a single sentence, written to `/output/entry.txt` by a
program the competition harness runs.

[![bounty](https://make.fun/badge/u-ronigrv-the-one-line-laugh-7ccca46f.svg)](https://make.fun/bounty/u-ronigrv-the-one-line-laugh-7ccca46f)
[![rank](https://make.fun/badge/u-ronigrv-the-one-line-laugh-7ccca46f/bongekanjing/one-line-laugh-brisk-owl-92/rank.svg)](https://make.fun/bounty/u-ronigrv-the-one-line-laugh-7ccca46f)
[![reward](https://make.fun/badge/u-ronigrv-the-one-line-laugh-7ccca46f/bongekanjing/one-line-laugh-brisk-owl-92/reward.svg)](https://make.fun/bounty/u-ronigrv-the-one-line-laugh-7ccca46f)

Bounty page: <https://make.fun/bounty/u-ronigrv-the-one-line-laugh-7ccca46f>

## The line

> My mother has started labelling her belongings with our names; the good
> scissors just say "you always borrow these".

The setup is ordinary and a little sad — an ageing parent assigning things,
which readers brace for as a decline story. The turn is that she is not
forgetting who her children are. She is prosecuting them. The label is a
verdict, and the thing she chose to label is the good scissors, the object
that has caused forty years of family grievance.

It works on the three things the brief weighs: the surprise is at the end and
still makes sense (she knows exactly who takes them); the everyday truth is
recognisable (every family has a pair of scissors with a reputation); and
nothing explains the joke — the reader arrives at "she's calling out her
kids" alone, which is where the laugh is.

## How it runs

`main.py` holds the line as a constant and writes it to `/output/entry.txt`.
Before writing, it checks the four things that would cost the entry its
place: the line is not blank, it is 200 characters or fewer, it carries no
line break, and it reads as exactly one sentence rather than two.

```sh
MAKEFUN_OUTPUT_DIR=/tmp/out python3 main.py
```

Python 3.13, standard library only.
