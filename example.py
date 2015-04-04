import fr


fname = 'info.txt'

print fr.get_len(fname)
print fr.get_line(fname,1),
print fr.get_element(fname,0,2)

print ("printing lines inbetween certain lines")
print fr.iterate_certainlines(fname,0,2)


def addOne(x):
    return x+1

print ("printing the array with the function applied")
#print fr.func_nextlines(fname,addOne,0,2)

