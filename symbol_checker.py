#!/usr/bin/env python3
import subprocess
import os
import glob
import argparse
import re

class Symbol:
    def __init__(self, name, kind, object_file):
        self.name = name
        self.kind = kind
        self.object_file = object_file

    def __hash__(self):
        return hash(self.name)

    def __eq__(self, other):
        return self.name == other.name

    def __ne__(self, other):
        return not self.__eq__(other)
        
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
        if self.name in line:
            self.current_object = line[line.find("(")+1:line.find(")")]

        m = re.match(r'(.*) ([TtSsUu]) (\w+)', line)
        if m:
            symbol_address = m.group(1)
            symbol_kind = m.group(2) # sS, tT, uU, etc
            symbol_name = m.group(3)

            symbol = Symbol(symbol_name, symbol_kind, self.current_object)
            self.symbols.add(symbol)
        
parser = argparse.ArgumentParser(description='Find what library symbols are used in another library or executable')
parser.add_argument("src", help = "the library file to run nm on")
parser.add_argument("bin", help = "The executbale/library that uses the first library")

args = parser.parse_args()

src_name = args.src
bin_name = args.bin

src_nm = NMParser(src_name, "--defined-only")
lib_symbols = []

if os.path.exists(bin_name):
    if os.path.isfile(bin_name):
        lib_symbols.append(NMParser(bin_name, "--extern-only"))
    else:
        for root, dirs, files in os.walk(bin_name):
            for filename in files:
                print(filename)
                if src_name not in filename:
                    lib_symbols.append(NMParser(os.path.join(bin_name, filename), "--extern-only"))
else:
    print("bin doesn't exist")


for lib in lib_symbols:
    print(f"Symbols provided by '{src_name}' that are used by '{lib.name}':")
    intersection = lib.symbols.intersection(src_nm.symbols)
    if not intersection:
        print("    None")
    else:
        for symbol in intersection:
            print("   ", symbol.name, " from ", symbol.object_file)

