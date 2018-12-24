#gtg3vv
#12/01 Puzzle 1

pastFrequencies = {0:1}
lastFrequency = 0

       
def parseInputFile(filename, currentFreq):
    with open(filename,'r') as file:
        for line in file:
           currentFreq += int(line)
    return currentFreq
    
def parseFileForDups(filename, currentFreq):
    global lastFrequency
    
    with open(filename,'r') as file:
        for line in file:
            currentFreq += int(line)
            lastFrequency = currentFreq
            if currentFreq not in pastFrequencies:
                pastFrequencies[currentFreq] = 1;
            else:
                pastFrequencies[currentFreq] = pastFrequencies[currentFreq]+1;
                return True
           
    return False
    


if __name__ == "__main__":
    
    foundDup = False
    while not foundDup:
        foundDup = foundDup or parseFileForDups('input.txt', lastFrequency)
    
    print(lastFrequency)