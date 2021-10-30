par = 0
impar = 0

for c in range(1, 101):
    n = int(input())
    if n % 2 == 0:
        par = par + 1
    elif n % 2 != 0:
            impar = impar + 1
print(f'{par}')
print(f'{impar}')
    
