# n =int(input("enter the no. = "))
# for i in range(1,n+1):
#     for j in range(1, n+1):
#         if(i==1 or i==n):
#             print("*",end= "")
#         elif(j==1 or j==n):
#             print("*",end= "")
#         else: 
#             print(" ",end= "") 
#     print()        






# now by recusion we print the strars 
#***
#**
#*
def pattern_star(n):
    if (n==0):
        return
    else:
            print("* "* n)
            return pattern_star(n-1)
            
n = int(input("enter the no. "))
pattern_star(n)    