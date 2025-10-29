def x(l):
    if l!=[]:
        s=0
        for i in range(0,len(l),1):s+=l[i]
        return s/len(l)

nums=[1.5,2.5,3.5,4.5]
print("ans:",x(nums))

