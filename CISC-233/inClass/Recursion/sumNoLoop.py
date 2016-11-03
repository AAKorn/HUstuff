def listFun(lisT):

    if len(lisT) == 1:
        return lisT[0]
    else:
        return lisT[0] + listFun(lisT[1:])
    
lisT = [1,2,3,4,5]

print listFun(lisT)   
