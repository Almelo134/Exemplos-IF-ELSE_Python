a = 's'

while (a == 's'):
    x = int(input('Insira um valor:'))
    y = int(input('Insira um valor:')) 
    z = x * y
    z = z % 1000
    
    if (z > 600):
        z= z / 2
    elif(z < 400):
        z = 2 * z

    print(z)

    a = input('Novos Numeros? S/N:')
    if (a == 'n'):
        exit()
