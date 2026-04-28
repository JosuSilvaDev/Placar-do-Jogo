

salario = float(input("DIGITE O SALARIO POR MES: "))
salario_minimo = 1580

media = salario / salario_minimo

print (f"MEDIA DO COM SALARIO MINIMO: {media:.2f}")

if media < 1.26 :
    print(f'\n MEIDA : {media:.2f}\n SALARIO: r$:{salario} \n CLASSE : "E" , BAIXA RENDA ')

elif media > 1.26 and media < 2.53 :
    print(f'\n MEIDA : {media:.2f}\n SALARIO: r$:{salario} \n CLASSE : "D" , MEDIA BAIXA  ')

elif media > 2.53 and media < 6.32 :
    print(f'\n MEIDA : {media:.2f}\n SALARIO: r$:{salario} \n CLASSE : "C" , CLASE MEDIA   ')
elif media > 6.32 and media < 12.65 :
    print(f'\n MEIDA : {media:.2f}\n SALARIO: r$:{salario} \n CLASSE : "B" , CLASE ALTA   ')    
else:
    print(f'\n MEIDA : {media:.2f}\n SALARIO: r$:{salario} \n CLASSE : "A" , CLASE MUITO ALTA  ')     


