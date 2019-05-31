def f(a,b,*args,**keywords):
    print(f'a*b:{a*b}')
    print('args:')
    for arg in args:
        print(arg)
    print('dictionary')
    for key in keywords:
        print(f'{key}={keywords[key]}')

f(2,2,3,4,5,c=2)
