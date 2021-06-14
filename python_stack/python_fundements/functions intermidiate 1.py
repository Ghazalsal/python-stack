def randInt(min=0, max=100):
    import random
    num = random.random()*(max-min) + min
    return(int(num))
print(randInt())
print(randInt(min=50, max=50))
print(randInt(min=50, max=100))
print(randInt(min=50, max=500))