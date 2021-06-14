# Biggie Size:
def bign(list):
    for x in range(0,len(list),1):
        if list[x]>0:
            list[x]="big"
    print(list)
bign([-2,1,-3,5,8])
# [-2, 'big', -3, 'big', 'big']

# Count Positives:
def positives(list):
    sum=0
    for x in range(0, len(list),1):
        if list[x]>0:
            sum=sum+1
    list.pop()
    list.append(sum)
    print(list)
    return list
positives([-1,2,-7,2,5])
# [-1, 2, -7, 2, 3]

# Sum Total:
def tot(list):
    sum=0
    for x in range (0,len(list),1):
        sum+=list[x]
    print(sum)
    return sum
tot([1,2,3,4])
# 10

# Average:
def average(list):
    sum=0
    for x in range (0,len(list),1):
        sum+=list[x]
    avg=sum/len(list)
    print(avg)
average([1,2,3,4])
# 2.5

# Length:
def length(list):
    print(len(list))
length([1,5,-5])
# 3

# Minimum:
def minimumn(list):
    min=list[0]
    if len(list) ==0:
        return False
    for x in range (0,len(list),1):
        if list[x]< min:
            min=list[x]
    print(min)
minimumn([1,-5,9,-3])
# -5

# Maximum:
def maximumn(list):
    max=list[0]
    if len(list)==0:
        return False
    for x in range (0, len(list),1):
        if list[x]> max:
            max = list[x]
    print(max)
maximumn([-5,6,8,9])
# 9

# Ultimate Analysis:
def dictionary(list):
    min=list[0]
    max=list[0]
    sum=0
    for x in range (0,len(list),1):
        if list[x]< min:
            min=list[x]
        if list[x]> max:
            max = list[x]
        sum+=list[x]
    avg = sum / len(list)
    dictlist = {'sum': sum, 'min': min, 'max': max, 'avg': avg, 'len_list': len(list)}
    print(dictlist)
    return dictlist
dictionary([1,-5,5,7])
# {'sum': 8, 'min': -5, 'max': 7, 'avg': 2.0, 'len_list': 4}

# Reverse List:
def reverse(list):
    print(list[::-1])
reverse([1,5,3,7])
# [7,3,5,1]


