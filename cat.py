#!/usr/bin/python3
import os
from sys import argv

path = argv[1]

file = open(path, 'r')

print(file.read())
file.close()
