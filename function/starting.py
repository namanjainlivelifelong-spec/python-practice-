# def avg():
#     n = int(input("enter the no. = "))
#     sum =0
#     for i in range(1,n+1):
#         sum += i
#     print("average = ",sum/n)
# avg()    


# def avg():
#     a = int(input("enter the no. = "))
#     b=  int(input("enter the no. = "))
#     c = int(input("enter the no. = "))
#     avgrage = (a+b+c)/3
#     print("average = ",avgrage)
# avg()    




# def hello(name ,ending,starting):
#     print("hello",name)
#     print(starting)
#     print(ending)

# hello("sachin","good morning","how are you")   
# hello("naman","good evening","how are you")



def hello(name ,ending,starting):
    print("hello",name)
    print(starting)
    print(ending)
    return "fantastic job"

a = hello("sachin","good morning","how are you")   # idhar jo return hoga vo a me store hoga because humne function ko call kiya hai aur uska return value ko a me store kar diya hai ye ek function hai jo ki 3 argument leta hai aur return karta hai ek string ko. ye ek rule hai ki agar humne function me return kiya hai to usko kisi variable me store karna chahiye taki hum usko use kar sake.
print(a)