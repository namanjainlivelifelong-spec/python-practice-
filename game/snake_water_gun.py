import random
'''
1 for sanke 
-1 for water 
0 for gun
'''
computer = random.choice([-1,0,1])
youstr = input("enter  your choice")
youDict = {"s":1,"w":-1,"g":0}
reversDict = {1:"snake", -1:"water",0: "Gun"}
you = youDict[youstr]
print(f"you chose")