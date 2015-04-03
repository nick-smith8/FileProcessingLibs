File reading library for Programming Competitions
======

usage:
-------------

def get_len(fname)
Returns number of lines in file

def get_line(fname, linenum)
Return Specified line from line number

get_element(fname,linenum,index)
Returns certain element given line number and index.
Currently first position is 0 2nd is 2 and 3rd is 4.. idk why

iterate_certainlines(fname,beginline,endline)
Returns an array of the elements inbetween the given begining and end line.
GOTCHA: I converted them all to Ints but that might not be the case for some.

def func_nextlines(fname, func, beginline, endline)
Returns an array with the function applied to those lines.

