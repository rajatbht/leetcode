def maxmin(a):
    start=0
    max=a[start]
    min=a[start]
    while start<len(a)-1:
        start+=1
        if max<a[start]:
            max=a[start]
        if min>a[start]:
            min=a[start]
            # print(min)
    return max,min

a=[5,7,3,9,1,4,11,0]
maximum,minimum=maxmin(a)
print(f"maximum= {maximum}")
print(f"minimum= {minimum}")

