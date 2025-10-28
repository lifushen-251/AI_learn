def sum_1(n,list1):
    list_result=[]
    i=0
    m=len(list1)
    while i<m:
        list2=list1[:]
        x= list1[0]
        list2.remove(x)
        for y in list2:
            if x+y==n:
                list_result.append((x,y))
        list1.remove(x)
        i=i+1
    return list_result

def sum_2(n,list1):
    list_result=[]
    m=len(list1)
    for i in range(m):
        x=list1[i]
        for j in range(i+1,m):
            y=list1[j]
            if x+y==n:
                list_result.append((x,y))
    return list_result

def sum_3(n,list1):
    result=[]
    r=len(list1)
    for i in range(r):
        t=list1[0]
        m=n-t
        if m in list1 and m!=t:
            result.append((t,m))
        list1.pop(0)
    return result


print(sum_1(10,[2,5,8,4,7,6,3]))
print(sum_2(10,[2,5,8,4,7,6,3]))
print(sum_3(10,[2,5,8,4,7,6,3]))