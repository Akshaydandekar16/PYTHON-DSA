a=int(input())
list=list(map(int,str(a)))
root_sum=0
for i in range(0,len(list)):
    digit=list[i]
    root_sum=root_sum+digit

print(root_sum)

    