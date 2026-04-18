matriz_dos_assentos = [
 ['D','D','D','D','D','D','D','D','D','D'],
 ['D','D','D','D','D','D','D','D','D','D'],
 ['D','D','D','D','D','D','D','D','D','D'],
 ['D','D','D','D','D','D','D','D','D','D'],
 ['D','D','D','D','D','D','D','D','D','D']
]
def demonstra_assentos(matriz):
    print('   ', end='')
    for c in range(len(matriz[0])):
        print(f'{c+1}  ',end='')
    print()
    for f in range(len(matriz)):
        print(f'{f+1:2} ',end='')
        for a in range(len(matriz[f])):
         print(f'{matriz[f][a]:2}',end=' ')
        print()

demonstra_assentos(matriz_dos_assentos)
print('='*30)
print('           menu'.upper())
print('='*30)
print('''1.ver assentos disponiveis
2.escolher assento
3. sair'''.upper())
print('-'*30)
r = 0
while r != 3:
 try:
  r = int(input('qual sua escolha?: '))
  if r not in [1,2,3]:
      print('digite uma opçao valida(1,2 ou 3)')
      print()
      continue
  if r == 1:
        demonstra_assentos(matriz_dos_assentos)
  if r == 2:
      try:
          fila = int(input('qual fileira voce quer reservar: '))
          assento_f = int(input('qual assento voce quer'))
          if fila < 1 or fila > 5 or assento_f < 1 or assento_f > 10:
              print('posiçao invalida')
              continue

          if  matriz_dos_assentos[fila-1][assento_f-1] != 'D':
              print('o assento ja esta reservado')
              continue

          matriz_dos_assentos[fila-1][assento_f-1] = 'R'
          demonstra_assentos(matriz_dos_assentos)
      except ValueError:
         print('entrada invalida')

 except ValueError:
     print('digite uma opçao valida(1,2 ou 3)')
     print()
print()
print('programa finalizado com sucesso!!')