#!/usr/bin/env python3
# requires python 3.8 for the walrus tusks := operator
import subprocess
import os
import glob
import argparse
import re

class Symbol:
    def __init__(self, name, kind):
        self.name = name
        self.kind = kind
        
class NMParser:
    
    def __init__(self, name, options):
        self.name = name
        self.current_object = ""
        self.symbols = set()
            
        nm = subprocess.check_output(['nm', options, name]).decode('utf-8').splitlines()
        for line in nm:
            self.insert(line)

            
    #  Parses the file one line at a time 
    def insert(self, line):
        # Return if line is blank
        if line == "\n":
            return
        if m := re.match(r'(.*) ([TtSsUu]) (\w+)', line):
            symbol_address = m.group(1)
            symbol_kind = m.group(2) # sS, tT, uU, etc
            symbol_name = m.group(3)

            symbol = Symbol(symbol_name, symbol_kind)
            self.symbols.add(symbol_name)
        
parser = argparse.ArgumentParser(description='Find what library symbols are used in another library or executable')
parser.add_argument("src_lib", help = "the library file to run nm on")
parser.add_argument("consumer_lib", help = "The executbale/library that uses the first library")

args = parser.parse_args()

src_lib_name = args.src_lib
consumer_lib_name = args.consumer_lib

src_lib = NMParser(src_lib_name, "--defined-only")
consumer_lib = NMParser(consumer_lib_name, "--extern-only")

print(f"Symbols provided by '{src_lib_name}' that are used by '{consumer_lib_name}':")
for symbol in consumer_lib.symbols.intersection(src_lib.symbols):
    print("   ", symbol)

