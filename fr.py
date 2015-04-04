#Helper Functions for reading from files

# Returns number of lines in file
def get_len(fname):
    with open(fname) as f:
        for i, l in enumerate(f):
            pass
    return i 

#Return Specified line from line number
def get_line(fname, linenum):
    with open(fname) as f:
        for i, line in enumerate(f):
            if i == linenum:
                line = line.split(' ')
                line[-1] = line[-1].strip()
                line = [ int(x) for x in line ]
                return line


# Returns certain element given line number and index.
#Currently first position is 0 2nd is 2 and 3rd is 4.. idk why
def get_element(fname,linenum,index):
    with open(fname) as f:
        for i, line in enumerate(f):
            if i == linenum:
                return line[index]


#Returns an array of the elements inbetween the given begining and end line.
#GOTCHA: I converted them all to Ints but that might not be the case for some.
def iterate_certainlines(fname,beginline,endline):
    container = []
    with open(fname) as f:
        for i, line in enumerate(f):
            if (i >= beginline and i <= endline):
                container.append(int(line.rstrip('\n')))
    return container


#Returns an array with the function applied to those lines.
def func_nextlines(fname, func, beginline, endline):
    with open(fname) as f:
        array = iterate_certainlines(fname,beginline,endline)
        for element in array:
            array[element-1] = func(array[element-1])
    return array
