#!/usr/bin/env python3

import sys

from Lexer import Lexer
from Parser import Parser
from Passage import Passage



for i in range(1,len(sys.argv)):

    code=sys.argv[i]

    tokens=Lexer.lex(code)

    cites=Parser(tokens).parse()

    passages=[]
    for cite in cites:
        if cite:
            passages.extend(Passage.find(cite))

    print()
    for passage in passages:
        print(passage)
        print()
