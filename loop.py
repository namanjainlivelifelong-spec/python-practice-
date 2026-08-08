# i=1
# while i<7:
#     print(i)
#     i+=1
#  l = [1,"namna ",True,"hello",False]
#  i=0
# while (i<len(l)):
#     print(l[i])
#     i+=1
# for i in l:
#     print(i)


# for i in l:
#     print(i)   #if we use else with the for loop then it will execute after the loop is completed
# else:
#     print("Loop completed successfully")
# for i in range(1,15):
#     if (i== 10):
#         break
#     print(i)    
# for i in range(1,15):
#     if (i == 10):
#         continue
#     print(i)




# n = int(input("enter a no."))
# for i in range(1,11):
#     print(f"{n} * {i} = {n * i}")



# name = "Naman"
# age = 20

# print(f"My name is {name} and I am {age} years old.")  # f se hum string me variable ko directly use kar sakte hai


n = int(input("enter a no. "))
factorial=1
for i in range (1,n+1):
    # factorial = n*i    //it is a wrong approch 
    factorial *= i
print(f"the factorial of {n} is {factorial}")

print("thanks")
