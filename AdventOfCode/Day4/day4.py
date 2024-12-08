file = open('input.txt', 'r');

result = 0
data = []
word = ["X", "M", "A", "S"]

result2 = 0


def checkXMAS(data, i, j):
    if i <= 0 or j <= 0 or i >= len(data) - 1 or j >= len(data[0]) - 1:
        return 0

    diag1 = data[i - 1][j - 1] + data[i + 1][j + 1]
    diag2 = data[i - 1][j + 1] + data[i + 1][j - 1]

    if (diag1 == "MS" or diag1 == "SM") and (diag2 == "MS" or diag2 == "SM"):
        return 1
    else:
        return 0


# Checks for word in a 2D matrix called data starting at position (i,j)
# Optionally only continues checking (recursivly) in a certain direction
def checkMatch(word, data, i, j, di=0, dj=0):
    ## Main recusrsion guard
    ## If we've reached the end of the word, we've had a succesful match
    if len(word) == 0:
        return 1

    ## Secondary guard
    ## If we reach the dge of the matrix, stop searching
    elif i < 0 or j < 0 or i >= len(data) or j >= len(data[0]):
        return 0

    else:
        ## Does the current letter match?
        if word[0] == data[i][j]:

            ## No direction yet? Check em all...
            if di == 0 and dj == 0:

                ## Recursivly check the 8 directions
                return (
                        checkMatch(word[1:], data, i, j + 1, 0, 1) +
                        checkMatch(word[1:], data, i, j - 1, 0, -1) +
                        checkMatch(word[1:], data, i - 1, j - 1, -1, -1) +
                        checkMatch(word[1:], data, i - 1, j, -1, 0) +
                        checkMatch(word[1:], data, i - 1, j + 1, -1, 1) +
                        checkMatch(word[1:], data, i + 1, j - 1, 1, -1) +
                        checkMatch(word[1:], data, i + 1, j, 1, 0) +
                        checkMatch(word[1:], data, i + 1, j + 1, 1, 1)
                )
            else:
                ## Recursivly check the direction we are already going in
                return checkMatch(word[1:], data, i + di, j + dj, di, dj)

        ## letter doesnt' match?
        else:
            return 0


## Read Wordsearch into a big 2d array
for line in file:
    data.append(list(line.rstrip()));

## Go through the matrix looking for first letter
for i in range(0, len(data)):
    for j in range(0, len(data[0])):
        if data[i][j] == word[0]:
            ## check to see how many copies of the word exist in any direction from this point
            result += checkMatch(word, data, i, j)
        if data[i][j] == 'A':
            result2 += checkXMAS(data, i, j)

## Final total
print('Result is: ' + str(result))
print('Result2 is ' + str(result2))