def missing_number(missNum):
    sMiss = sum(missNum)
    print (sMiss)

    i = missNum[0]
    j = missNum[-1]
    actSum = sum(range(i, j+1))
    print (actSum)
    print (actSum-sMiss)
    

print(missing_number([10, 11, 12, 14, 15, 16, 17]))
