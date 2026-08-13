def calcute_sum(n):
    
    if(n ==1):
        return 1
    else:
        return calcute_sum(n-1)+n
n =  int(input("enter the no. = "))   #return ki value ko hamne n me store kiya hai taki hum usko use kar sake. ye ek function hai jo ki ek argument leta hai aur return karta hai ek integer ko. ye ek rule hai ki agar humne function me return kiya hai to usko kisi variable me store karna chahiye taki hum usko use kar sake.
print(calcute_sum(n) )      
