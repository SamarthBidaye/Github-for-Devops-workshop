array=[1,2,3,4,5]
for i in range(len(array)):
    if i%2==0:
        array[i]=array[i]*2
    else:
        array[i]=array[i]*3
print(array)