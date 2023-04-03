def findMissingNumber(n):
    numbers =set(n)
    length = len(n)
    
    output= []
    
    for i in range(1,n[-1]):
        if i not in numbers:
            output.append(i)
    return output


listofNumbers=[1,2,3,5,7,6,8,11,13,14]
print(findMissingNumber(listofNumbers))