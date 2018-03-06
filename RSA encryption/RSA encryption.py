import math
#RSA Encryption
"""
We have a message 'M' we want to encrypt.
We need to find 2 very large primes. p and q
"""
p = 7
q = 11
n = p*q

phi = (p-1)*(q-1)
print("This is phi " + str(phi))

e = 13

#for two things to be relatively prime they need to adhere to
# ex + ny = 1 where e is the prime e, and n is the phi showing the set of integers
#the x is the value that will output 1 when multiplied by e in mod phi.
for y in range(-phi,phi):
    for x in range(-phi,phi):
        if x < 0:
            x = x % phi
            if (e*x + phi*y == 1):
                d = x
                print(d)

#now we send the message
message = 28

x = math.fmod(message**e, n)
print ("This is x " + str(x))
k = math.fmod(x**d,n)

print(k)

