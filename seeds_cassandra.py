#!/usr/bin/env python3

import sys
import os
import fileinput

ipfile = open('seeds', 'r')
line = ipfile.readline()
while line:
    line = line.rstrip(",")  # strip trailing spaces and newline
    # process the line
    #print(f'- seeds: "{line}"')
    newseeds = '- seeds: "{var}"'.format(var=line)
    print(f'{newseeds}')
    with open('cassandra.yaml', 'r') as file:
        filedata = file.read()
    filedata = filedata.replace('- seeds: "127.0.0.1:7000"', '{}'.format(newseeds))
    with open('cassandra.yaml', 'w') as file:
        file.write(filedata)

    line = ipfile.readline()

ipfile.close()






