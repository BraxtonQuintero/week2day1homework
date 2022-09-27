#Exercise 1

#list_num = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]

for i in [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]:
    i = i*i*i
    if i >= 1001:
        break
    print(i)
print('number exceeds 1000')

#Exercise 2



prime = False

for i in range(2, 100):
        if (i / i) == 0:
            prime = True
            break
if prime:
    print(i, "is not a prime number")
else:
    print(i, "is a prime number")



# Exercise 3

person_age = 67 

if person_age < 18:
    print('kids')
elif person_age <= 65:
    print('adults')
else:
    print('seniors')