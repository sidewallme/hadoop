#!/usr/bin/env python3 
import sys
#!export PYTHONIOENCODING=latin-1
sep = '\t'

with sys.stdin as fin:
    with sys.stdout as fout:
    
        for line in fin:
        
            line = line.strip()
            words = line.split(",")
            
            if len(words) > 20 :
                word = words[16]
                fout.write("{0}{1}1\n".format(word, sep))