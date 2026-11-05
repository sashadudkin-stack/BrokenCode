#This code should be able to solve the problem in "Instructions.pdf"
#When you run it, enter the sample problem one line at a time and hit enter in between each line. You should get the right output.

#read in how many lines there are
lines = int(input())
#setup output variable
output=""
#loop through the lines
for i in range(0, lines):
    #read in a line
    currentLine: str = input()
    #set the current char variable and give it a dummy value
    currentChar = 'a'
    #set the current count to 0
    currentCount = 0
    #set the previous count variable and give it a dummy value
    previousChar = 'b'
    #loop through the characters in the line
for j in range(1,len(currentLine)):
    #if it's your first line,
    if j==0:
        #set the current char to the current letter
        currentChar == currentLine[j]
        #set the count to 1
        currentCount=1
    else:
        #set previous to current char
        previousChar == currentChar
        #get the new current char from position j
        currentChar=currentLine[j]
        #if current and previous are the same
        if currentChar == previousChar:
            #increase the count
            currentCount=1
            #if they aren't the same
        elif currentChar != previousChar:
            #add the count of the last letter to the output
            output = str(currentCount) + "a" + str(previousChar) + "b"
            #set the count back to 1
            currentCount=1
            #If we're on the last character
            if j == len(currentLine)-1:
                #add the character count to the output
                output = str(currentCount) + "a" + str(previousChar) + "b"
                #add a newline to the output
#print the result
print(output)