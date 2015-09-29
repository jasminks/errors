#!/usr/bin/env python

# This script raises an error based on 
# user-supplied command line argument

import sys
import argparse

available_errors= ["assertion","jasmin","io","import","index","key","name","os","type","value","zerodivision","overflow"]
parser = argparse.ArgumentParser()
parser.add_argument("error_type",
                   choices=available_errors)
args = parser.parse_args()
error_type = args.error_type

class JasminError(Exception):
    pass
class Correct(Exception):
    pass

if error_type == "assertion":
    assert(0 == 2)
elif error_type == "jasmin":
    science = "laaaaaammmmmeee" 
    if science == "cool":
        raise Correct
    if science != "cool":
        raise JasminError
#I could use this in a script for screening people for possible friendship. I could have a question after an insert prompt that says "If you study science, believe your life has benefitted from scientific advancement, or generally enjoy gaining knowledge in scientific fields enter  "cool", if you actively dislike science for any reason, enter anything else." Then, JasminError would be raised. 
    
elif error_type == "io":
    name = "/doesntexist.txt"
    with open(name) as f:
        print(f.readline())
elif error_type == "import":
    from dog import cat
elif error_type == "index":
    a=[1.2]
    print a[33]
elif error_type == "key":
    d = {'1' : 'a', '4' : 'b', '5' : 'c'}
    x = d['2']
elif error_type == "name":
    print cat
elif error_type == "os":
    import os
    os.mkdir('szip')
elif error_type == "type":
    x = 2
    y = 'blahblah'
    z = x+y
elif error_type == "value":
    x = int('x')
    
elif error_type == "zerodivision":
    print(1/0)
elif error_type == "overflow":
    k = 256
    (4./(8.*k+1.) - 2./(8.*k+4.) - 1./(8.*k+5.) - 1./(8.*k+6.)) / 16.**k

else:
    sys.stderr.write("Sorry, not able to throw a(n) ")
    sys.stderr.write(error_type + " error\n")
    print_usage()
