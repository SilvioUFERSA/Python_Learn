# termos de condição em python  -> IF ;  ELSE ; ELIF.
# condicionais -> END, OR, NOT.

a = int(input('insira um valor para a: '))
b = int(input('insira um valor para b: '))
c = int(input('insira um valor para c: '))


if a > b and a > c:
    print('o numero: {} eh maior'.format(a))
    if a % 2 == 0:
        print('o numero : {} eh par'.format(a))
    else:
        print('o numero : {} eh impar'.format(a))

elif b > a and b > c:
    print('o numero: {} eh maior'.format(b))
    if b % 2 == 0:
        print('o numero : {} eh par'.format(a))
    else:
        print('o numero : {} eh impar'.format(a))

else:
    print('o numero: {} eh maior'.format(c))
    if c % 2 == 0:
        print('o numero : {} eh par'.format(a))
    else:
        print('o numero : {} eh impar'.format(a))

print('\nfim do programa.')