import fr

fname='input.in'
print fr.get_line(fname,0)
print fr.get_line(fname,2)

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


data1 = [[0 for x in range(4)] for x in range(4)]
data2 = [[0 for x in range(4)] for x in range(4)]

firstRow = int(fr.get_element(fname,startingFirstRow,0))
secondRow = int(fr.get_element(fname,startingSecondRow,0))

firstLine = fr.get_line(fname,(startingFirstRow + firstRow))
secondLine = fr.get_line(fname,(startingSecondRow + secondRow))

print "This is first line", firstLine
print "This is second line", secondLine

while case != 100:
    for i in firstLine:
        for j in secondLine:
            if i == j:
                magicNum = i
                isDuplicate += 1
                noMatch = False

    if isDuplicate > 1:
        print 'Case #', case, ':','Bad magician'
    elif noMatch == True:
        print 'Case #', case, ':', 'Volunteer cheated!'
    else:
        print 'Case #', case, ':', magicNum

    case = case + 1
    isDuplicate = 0

    firstLine = fr.get_line(fname,prevFirstRow+10)
    secondLine = fr.get_line(fname,prevSecondRow+10)

    prevFirstRow += 10
    prevSecondRow += 10

    noMatch = True


