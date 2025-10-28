def leetcode_3(string):
    n=len(string)
    result=string[0]
    for i in range(n):
        a=string[i]
        b=a
        for x in range(i+1,n):
            y=string[x]
            if y not in b:
                b=b+y
            else:
                break
        if len(b)>len(result):
            result=b
    return result

def leetcode_1(n,list1):
    result=[]
    list2=list1[:]
    r=len(list1)
    for i in range(r):
        t=list1[0]
        m=n-t
        if m in list1 and list1.index(m)!=i:
            result.append((i,list2.index(m)))
        list1.pop(0)
    return result

# def leetcode_4(list_input):
#      result=list_input[0]
#      return result
print(leetcode_3("114514"))
print(leetcode_1(6,[2,4,5,1]))