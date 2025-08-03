def lru_cache(request,size):
    d={}
    for i in request:
        if(request.count(i) not in d):
            lst=[]
            d[request.count(i)]=lst.append(i)
            print(d)
        else:
            d[request.count(i)].extend(i)
    sort_dict=dict(sorted(d.items(),key=lambda x:x[0]))
    c=[]
    for i in range(1,size+1):
        if(i==1):
            a,b=sort_dict.popitem()
            c.extend(b)
        else:
            a,b=sort_dict.popitem()
            c.extend(b[::-1])
    return lst[:size]
request=list(map(int,input().split()))
size=int(input())
print(lru_cache(request,size))

