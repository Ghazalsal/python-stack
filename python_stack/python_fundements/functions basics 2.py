# countdown
def countdown(n):
    list = []
    for x in range (n,-1,-1):
        list.append(x)
    print(list)
print(countdown(5))
//[5,4,3,2,1,0]

#Print and Return
def printreturn(list):
    print(list[0])
    return (list[1])
printreturn([0,1])
# 0

# firstplus:
def firstplus(list):
    print(list[0] + len(list))
firstplus([0,5,8,9,2,4])

# greater:
def secondgreat(list):
    newlist=[]
    max = list[1]
    if len(list) < 2:
            return false
    else:
        for x in range (0, len(list), 1):
            if list[x] > max:
                newlist.append(list[x])
                
    print(len(newlist))
    return newlist
    
print(secondgreat([0,1,2,5,9]))
# 3 , [2, 5, 9]

# This Length, That Value:
def interg(s,v):
    list=[]
    for i in range (s):
        list.append(v)
    print(list)
    return list
interg(4,7)



