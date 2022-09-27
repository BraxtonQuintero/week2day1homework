#Exercise 1

#list_num = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]

for list_num in [1, 8, 27, 64, 125, 216, 343, 512, 719, 1000, 1331]:
    if list_num >= 1001:
        break
    print(list_num)
print('number exceeds 1000')




#Exercise 2

num = 71

prime = False

if num > 1:
    for i in range(2, num):
        if (num / i) == 0:
            prime = True
            break
if prime:
    print(num, "is not a prime number")
else:
    print(num, "is a prime number")



# Exercise 3

person_age = 67 

if person_age < 18:
    print('kids')
elif person_age <= 65:
    print('adults')
else:
    print('seniors')