lines = int(input())
output = " "

for i in range(0, lines):
   currentLine = input()

   currentChar = " "
   currentCount = 0
   previousChar = " "

   for j in range(0, len(currentLine)):

       if j == 0:
           currentChar = currentLine[j]
           currentCount = 1

       else:
           previousChar = currentChar
           currentChar = currentLine[j]

           if currentChar == previousChar:
               currentCount += 1

           else:
               output += str(currentCount) + " " + str(previousChar) + " "
               currentCount = 1

       if j == len(currentLine) - 1:
           output += str(currentCount) + " " + str(currentChar) + " "

   output += "\n"

print(output)
