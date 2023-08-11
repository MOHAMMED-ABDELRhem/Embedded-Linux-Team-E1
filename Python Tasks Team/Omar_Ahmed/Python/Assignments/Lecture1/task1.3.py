#!/usr/bin/python3

import os

env = input('Enter env variable : ').strip()

if  env in os.environ:
    print(os.environ.get(env))
else :
    print("Not env variable")
    