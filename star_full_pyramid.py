# n= int(input("enter the no. : "))
# for i in range(1,n): # idhar n ka kaam hai ki humko kitne rows print karne hai
#     for j in range(0,2*i-1): #idhaar 2*i-1 ka kaam hai kuki humko har row me odd no. of stars print karne hai and yaha i ka kaam hai ki humko kitne rows print karne hai 
#         print(""* (n-1),end="") # idhar n-1 ka kaam hai ki humko kitne spaces print karne hai
#         print("*",end="")
        
#     print()


n= int(input("enter the no. : "))
for i in range(1,n+1): # idhar n ka kaam hai ki humko kitne rows print karne hai
    print(" "*(n-i),end="") # idhar n-1 ka kaam hai ki humko kitne spaces print karne hai
    for j in range (0,2*i-1):
        print("*",end="")

    print()   
