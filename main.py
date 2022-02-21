divided = []
divided_cubed = []

for number in range(0,101):
    if number % 5 == 0:
        divided.append(number)

for i in divided:
    divided_cubed.append(i**3)

print(f'{divided}\n{divided_cubed}')