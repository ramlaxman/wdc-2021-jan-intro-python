x = input('Enter x: ').strip()
y = input('Enter y: ').strip()

if not x.isdigit():
    print(f'{x} is not numeric')

elif not y.isdigit():
    print(f'{y} is not numeric')

else:
    x = int(x)
    y = int(y)

    print(f'{x} + {y} = {x+y}')
