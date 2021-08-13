#https://github.com/hazemabdo15/List-and-function-Task.git
def check_div (list=[1,2,3,4,5,6], num=2):
    print("The numbers in ", list1, "that are divisible by", num,"are:")
    for i in list:
        if i % num == 0 :
            print(i)
          
list1 =[]
print("Enter Length of list :")
len = int(input())
print("Enter Numbers")
for i in range(len):
    numb=int(input())
    list1.append(numb)
print("Enter divisor number")
num = int(input())
check_div(list1,num)