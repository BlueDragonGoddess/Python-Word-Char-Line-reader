#Colton Dean
#Started April 8th and Finished on April 11th
#C0741555
#This program will take file paths using argparse and count the words, lines and chars contained within the file.

import argparse
import sys


# FILE safe_file_open (string)
#    Attempt to open a file and return its file descriptor
#    If this fails, exit.
def safe_file_open(file_path):
     try:
		
        if open(file_path, "r"):
            return True
     except OSError:
        print("Could not open [%s]! Aborting." % file_path)
        return False
     except IOError:
        print("Could not open [%s]! File doesn't exist." % file_path)
        return False


# {int} get_word_count (file_path)
#    Returns a dict with the file statistics fields
#    applied.
#    
#    The keys are:
#        int words
#        int chars
#        int lines
#
def get_file_stats(file_path):
    print("Getting stats from %s ..." % file_path)
    file = open(file_path)
    out = file.read()
    filestats = {
        "name":  file_path,
        "words": len(out.split()),
        "chars": len(out),
        "lines": len(out.splitlines())
    }
    return filestats


# boolean valid_fstat (dict)
#    Determine if the dict passed contains all of our required
#    keys.
#
def valid_fstat(dict):
    for __key in ["words", "chars", "lines"]:
        if not isinstance(dict[__key], int):
            print("Missing field [%s] in file [%s]" % (dict["name"], __key))
            return False
    return True


# BEGIN
#
def main(args):
    for __file in args.file:
        
        test = safe_file_open(__file)

        if test == True:
            fdict = get_file_stats(__file)
            
            if not valid_fstat(fdict):
                sys.exit(1)
                
            print("[%s] Word count: %d" % (__file, fdict["words"]))
            print("[%s] Char count: %d" % (__file, fdict["chars"]))
            print("[%s] Line count: %d" % (__file, fdict["lines"]))



#Makes sure the file running isn't sourced and is the main.
#Standard practice
#
if __name__=="__main__":
    print("Hello, world!")
    args = argparse.ArgumentParser()
    args.add_argument("-f", "--file", help="Add a file to parse",
        type=str, action='append')
    main(args.parse_args())

