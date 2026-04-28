pessoa = {"nome": "João", "sobrenome":"Silva " ,"nome": "Carolina","sobrenome": "Sambaio" , "idade": 30 , "idade" : 34 , "cidade": "São Paulo"}

for chave in pessoa.keys():
    print(chave)
print("\n valores \n")
for valor in pessoa.values():
    print(valor)
print("\n chave e valor \n")    

for valor , chave in pessoa.items():
    print(f"{valor} : {chave}")    
print("\n chave e valor \n")

for tudo in pessoa.items():
    print(tudo)

for nome, sobrenome in pessoa.items():
    print(f"{nome} : {sobrenome}")    
print("\n Range() \n")

for i in range(0,5):
    print("Digite" , i)

print("\n")  



print (len(pessoa)) # len() conta a quantidade de itens do dicionário, ou seja, quantas chaves existem 

linta = [1 , 2 , 3 , 4 , 25]

for indice in range(0, len(linta)):
    print("Indice :" , indice , "Valor :" , linta[indice])

linta[3] = 525

print(linta)

linta.append(100)
print(linta)
print("\n Range() \n")
for indice in range(0, len(linta)):
    if indice == 3:
        linta[indice] = 555
    print("Indice :" , indice , "Valor :" , linta[indice])


#enumerate() é uma função que retorna um objeto enumerado, que é um iterador que produz pares de índice e valor. Ele é comumente usado em loops para obter tanto o índice quanto o valor de uma sequência.
print("\n Enumerate() \n")

lista_enumerate = ["a", "b", "c", "d"]
for indice, valor in enumerate(lista_enumerate):
    print(f"Índice: {indice}, Valor: {valor}")
print("\n for pratica\n")

frutas = ["maçã", "banana", "laranja", "uva"]
for indice, fruta in enumerate(frutas):
    print(f"Índice: {indice}, Fruta: {fruta}")
    if frutas ==  "banana" :
        print(f"Fruta altamente rica em vitamina")
    else:
        print("Fora do grupo\n\n\n")   
print("\t\tTABUADA\n")
ind = 0
for n in range(0,11):
    ind = ind + 1 
    resultado = n * 1
    print(f"{n} x {1} = {resultado} \n")

    if ind == 11 :
        ind = 0
        for n in range(0,11):
            ind = ind + 1 
            resultado = n * 2
            print (f"{n} x {2} = {resultado}")
          

            if ind == 11 :
                ind = 0
                for n in range(0,11):
                    ind = ind + 1 
                    resultado = n * 3
                    print (f"{n} x {3} = {resultado}")


                    if ind == 11 :
                        ind = 0
                        for n in range(0,11):
                            ind = ind + 1 
                            resultado = n * 4
                            print (f"{n} x {4} = {resultado}")                            

             
                


    