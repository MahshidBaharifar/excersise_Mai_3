number=int(input("Enter the number: "))
#list= [i for i in range(item): [item for item in range(number)]]
#list=[]
#li=[]
#lst = [(i, [j for j in range(1, i+1) if not divmod(i,j)[1]]) for i in range(1, 5)]
#print(lst)
#for item in range(number):
#    for i in range(item):
#        li.append(i)
#    list.append(item,[li])


list=[ (i ,[item for item in range(1,i) if item%i==0]) for i in range(1,number)]
print(list)