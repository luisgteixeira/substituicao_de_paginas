#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys, getopt
from fifo import *
from otm import *
from lru import *

def main():
    # Carrega o arquivo em uma lista
    lines = sys.stdin.readlines()

    fifo = FIFO(lines)
    otm = OTM(lines)
    lru = LRU(lines)

    print('FIFO', fifo.output)
    print('OTM', otm.output)
    print('LRU', lru.output)

if __name__ == "__main__":
    main()
