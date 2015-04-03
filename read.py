import csv
import api


fopen = open('info.txt','r')
fname = 'info.txt'

print api.get_len(fname)
print api.get_line(fname,1),
print api.get_element(fname,2,0)

print ("printing lines inbetween certain lines")
print api.iterate_certainlines(fname,0,2)


def addOne(x):
	return x+1

print ("printing the array with the function applied")
print api.func_nextlines(fname,addOne,0,2)

