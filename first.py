# print("hello world")
# print("yo yo ")
# print(3+3)
# str ="my name is don"
# print(str.endswith("on"))  #seacrh from last word
# print(str.replace("on","uck")) #replace on with uck
# print(str.count("n"))
# marks =int(input("enter your marks :"))
# print("enter the marks :", marks)
# if(marks>=90):
#     print("A grade")
# elif(marks>=80 and marks<90):
#     print("B grade")
# elif(marks>=70 and marks<80):
#     print("C grade")
# else:
#     print("fail")

# student = ["nj","don","123","wsfjfnf",7474]
# for name in student:      {print each name in new line this give by rhe chatgpt}
#     print(name)  
# print(student[3])
# student[2]= "333"
# print(student)  
# list = ['apple','grapes','banana']
# print(list.sort())  
# print(list)

info = {
    "name":"don",
    "age":24,
    "city":"hyd",
    "marks":87,
    27 : 323,
    "score":{
        "today": "hot0",
        "tommorow":"cold",

    }
}

# print(info)
# # print(info["city"])
# info["name"]="skit"
# print(info["name"])
print(info["score"]["today"]) 

print(info.keys())  #print all keys in the dictionary
print(info.values())  #print all values in the dictionary       
print(list(info.keys())) #print all keys in the dictionary in list form
print(len(list(info.keys()))) #print the number of keys in the dictionary
print(info.items()) #print all key value pairs in the dictionary