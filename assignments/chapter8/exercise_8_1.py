#!/usr/bin/python3

# function to remove the first and last elements of a list and return None

def chop(myList):
    '''Remove the first and last elements from a list'''
    del myList[0]
    del myList[-1]
    return = None


def middle(myList):
    '''Takes a list and returns a list without the first and last element'''
    return myList[1:-1]
