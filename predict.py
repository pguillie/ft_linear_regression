#!/usr/bin/env python3

import struct

def define_function():
    definition_file = '.function'

    try:
        f = open(definition_file, 'rb')
    except:
        print("No definition file found, setting function to default")
        return (0, 0)

    try:
        return struct.unpack('ff', f.read())
    except:
        print("Error: unable to read \"{}\" file".format(definition_file))
        exit(1)

def predict(m, p):
    try:
        km = int(input("Enter mileage: "))
    except:
        print("Invalid input")
        exit(1)
    print("The estimated price of the vehicule is", m * km + p)

if __name__ == '__main__':
    (m, p) = define_function()
    predict(m, p)
