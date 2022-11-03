a = 's'

while (a == 's'):
    x = int(input('Idade:'))
    if (x < 16):
        print('Preso')
    if ((x < 18) and (x >= 16)):
        print('liberado')
    else:
        if(x >=18):
            print('Testar Alcool')
            teste = input('Alcool No Sangue? S/N:')
            if(teste == 's'):
               print('Preso')
            else:
               print('Liberado')
    a = input('Deseja realizar novo teste? S/N:')

if (a == 'n'):
    exit()
    
