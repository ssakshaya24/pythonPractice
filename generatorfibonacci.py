def simpleGeneratorFunction():
    prev1=1
    prev2=1
    sumv=1
    yield sumv
    for i in range(0,5):
        yield sumv
        sumv=prev1+prev2
        prev1=prev2
        prev2=sumv

for value in simpleGeneratorFunction():
    print(value)
