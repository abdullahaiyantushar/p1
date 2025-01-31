nums=(1,2, 3,4,5,6,7,8,9,0,)
x=50
for i in nums:
    if i==x:
        print("found")
        break

    
else:
    print("not found")



nums=(1,2, 3,4,5,6,7,8,9,0,)
x=5
ind=0
for i in nums:
    if i==x:
        print("found",ind)
        break
    ind+=1