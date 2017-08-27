#!python
# -*- coding: utf-8 -*-#
#
# Author      : Bhishan Poudel; Physics Graduate Student, Ohio University
# Date        : Aug 9, 2017
# Last update :
# Est time    :

def main():
    """Run main function."""
    nums = [ 3, 107, 366, 376, 400, 417, 419, 541, 445 ]
    ans = [ 21, 123, 380, 388, 413, 429, 430, 551, 554 ]

    for n in nums:
        if n >=545:
            print(n+9)
        if n >=107:
            print(n+16)

if __name__ == "__main__":
    main()
