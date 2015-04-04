#! /usr/bin/python
import fr

fname='../input/input.in'

numOfCases = fr.get_line(fname,0)
print numOfCases
case = 1

magicNum = 0

firstRow = 0
secondRow = 0

startingFirstRow = 1
startingSecondRow = 6

prevFirstRow = 2
prevSecondRow = 7

isDuplicate = 0
noMatch = True

firstRow = int(fr.get_element(fname,startingFirstRow,0))
secondRow = int(fr.get_element(fname,startingSecondRow,0))

firstLine = fr.get_line(fname,(startingFirstRow + firstRow))
secondLine = fr.get_line(fname,(startingSecondRow + secondRow))


while case != 100:
    #print "FirstLine: ",firstLine
    #print "SecondLine: ",secondLine

    for i in firstLine:
    #    print "This is i:" ,i
        for j in secondLine:
    #        print "This is j: ", j
            if i == j:
    #            print "They were a Match"
                magicNum = i
                isDuplicate += 1
                noMatch = False
   # print isDuplicate,"Duplicate num before compare"
    if isDuplicate > 1:
        print 'Case #', case, ':','Bad magician'
    elif noMatch == True:
        print 'Case #', case, ':', 'Volunteer cheated!'
    else:
        print 'Case #', case, ':', magicNum

    case = case + 1
    isDuplicate = 0

    startingFirstRow += 10
    startingSecondRow +=10

    firstLine = fr.get_line(fname,(startingFirstRow+int(fr.get_element(fname,startingFirstRow,0))))
    secondLine = fr.get_line(fname,(startingSecondRow+int(fr.get_element(fname,startingSecondRow,0))))

    prevFirstRow += 10
    prevSecondRow += 10

    noMatch = True


