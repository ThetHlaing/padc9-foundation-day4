lower_limit = int(input("Enter the lower limit"))
upper_limit = int(input("Enter the upper limit"))


odd_numbers = []

for i in range(lower_limit+1,upper_limit):
    if i%2 != 0 :
        odd_numbers.append(i)
print(odd_numbers)

