#!/usr/bin/env python
# coding: utf-8

# In[ ]:


#To find if a number is blum integer( number that has 2 prime numbers as its factors ie, n=p*q and the prime numbers p,q should satisfy (p%4==3 and q%4==3))


def is_prime(n):
    if n>1:
        for i in range(2,int(n**0.5)+1):
            if n % i== 0:
                return False
    return True

def is_blum_integer(num):
    for p in range(2,int(num**0.5)+1):
            if num % p == 0:
                q = num // p

                if is_prime(p) and is_prime(q) :
                    if p % 4 == 3 and q % 4 == 3:
                        return True
    return False

nt = int(input("give the composite number"))
result = is_blum_integer(nt) 
if result:
    print("True")
else:
    print("False")


# In[ ]:




