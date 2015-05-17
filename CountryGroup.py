#Problem Statement: http://community.topcoder.com/stat?c=problem_statement&pm=13687
def countryGroup(arr):
    countryGrp = {}
    prev = None
    for i in range(len(arr)):
        val = arr[i]
        if( val in countryGrp):
            countryGrp[val] +=1
            if(val != 1):
                if prev != None and prev !=val:
                    return -1
                if countryGrp[val] > val:
                    return -1
            prev = val
        else:
            countryGrp[val] =1
            prev = val
    total = 0
    for key in countryGrp.keys():
        if key == 1:
            total+= countryGrp[key]
        else:
            if (countryGrp[key] != key):
                return -1
            else:
                total +=1
    return total
    
print countryGroup([2,2,3,3,3])
print countryGroup([1,1,1,1,1])
print countryGroup([3,3])
print countryGroup([4,4,4,4,1,1,2,2,3,3,3])
print countryGroup([2,1,2,2,1,2])
