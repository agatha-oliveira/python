nome = 'Agatha'
sobrenome = input('Escreva seu sobrenome: ')
idade = input('Escreva sua idade: ') # input sempre retorna um obj type str
altura = 1.61
tipo_nome = type(nome) # normalmente utilizado para testar o tipo 
tipo_idade = type(idade)
tipo_altura = type(altura)
frase = nome + ' tem ' + str(idade) + ' anos e ' + str(altura) + ' de altura' # precisa utilizar a string pq no caso o + só identifica string

''' o phyton não precisa declarar o tipo da variavel, ele proprio já identifica, 
por isso utilizamos o type mais para testes '''

print('teste\nlilili')
print('lalala\tlololo\n')

print(nome, sobrenome, 'tem', idade, 'anos e', altura, 'de altura') # dá pra usar , ou + lembrando que o + nao da espaço
print(frase)
print(type(nome)) # normalmente utilizado para testar o tipo 
print(tipo_nome, tipo_idade, tipo_altura)

numero1 = 2
numero2 = 3
numero3 = 16

resultado1 = numero1 + (numero2 / numero1) * numero2 - numero3 * 1
resultado2 = numero1 ** 2 # potencia
resultado3 = numero3 ** (1/2) # raiz quadrada

print('\nResultado 1 e 2:', resultado1, resultado2, resultado3)







