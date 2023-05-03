def even_list(list):
    new_list=[]
    new_list=[item for item in list if item%2==0]
    return new_list
num=int(input("enter the number of your items: "))
list=[index for index in range(num) ]
print(list)
new_list=even_list(list)
print(new_list)

num=int(input("enter the number of your items: "))
even_number=[2*item for item in range(num) ]
print(even_number)


