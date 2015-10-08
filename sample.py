#!/usr/bin/python
# see book: Cathedral & Bazaar
import module1 as m

# def myFunc(var1):
#     print var1
#     return var1

# x=myFunc(5)


# userInput = raw_input("Press some value: \n")

# print 'You printed ', userInput

def main():
    print('main called')
    m.firstFunction(4)

if __name__ == '__main__':
    print 'This program can run itself'
    main()
else:
    print '\n*** This module is an import'
