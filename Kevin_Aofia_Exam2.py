def fallingPath(arr):
    paths = arr[1:]
    minPath = [] 
    for i in range(len(arr[0])):
        newPath = [arr[0][i]] #list containing starting path int
        for j in range(len(paths)):
            if i == 0:
                newPath.append(min(paths[j][i],paths[j][i+1]))
            elif i == len(paths):
                newPath.append(min(paths[j][i-1],paths[j][i]))
            else:
                newPath.append(min(paths[j][i-1],paths[j][i],paths[j][i+1])) #min value -1,0,+1
        minPath.append(newPath) #add minimum path to list
    return min(minPath) #return the smallest falling path from list

def palind(string): #????
    palindCount = 0
    indexCheck = []
    for i in range(len(string)):
        for j in range(len(string)):
            word = string[i] + string[:j]
            if word == word[::-1]:
                index = [[i,j]]
                if index not in indexCheck:
                    indexCheck.append([[i,j]]) #listed pairs
                    indexCheck.append([[j,i]])
                    palindCount+= 1
    return palindCount

def arithmeticSlice(arr):
    return arr[:-1],arr[1:],arr[:]

def minASCII(s1,s2):
    abc = dict()
    letters = "abcdefghijklmnopqrstuvwxyz" #starting keys
    ASCII = 97                             #starting values
    minimum = 0                            #for ASCII sum
    for char in range(len(letters)):
        abc[letters[char]] = ASCII
        ASCII += 1
    str1 = set(s1)
    str2 = set(s2)
    
    diff = str1.symmetric_difference(str2)
    for letter in diff:
        minimum += abc.get(letter)
    
    return minimum

def maxLen(A):
    length,maximumL = 0,0
    for pair in A:
        start = pair
        length += 1
        for nextPair in A:
            if start[1] < nextPair[0]:
                length += 1
        if length > maximumL:
            maximumL = length
        length = 0
    return maximumL

if __name__ == "__main__":
    
    print(fallingPath([[1,2,3],[4,5,6],[7,8,9]]))
    
    print(palind("aaa"))
    
    print(arithmeticSlice([1,2,3,4]))
    
    print(minASCII("sea","eat"))
    
    print(maxLen([[1,2],[2,3],[3,4]]))
    
    
