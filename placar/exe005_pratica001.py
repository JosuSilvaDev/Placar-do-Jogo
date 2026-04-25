time_casa = "CORINTHIANS"
time_visitante = "PALMEIRAS"
time_avante = "Flamengo"

jogador_1 = 99
jogador_2 = 150
jogador_3 = 120
jogador_4 = 82

ex_jogador_1 = 85
ex_jogador_2 = 15
ex_jogador_3 = 96
ex_jogador_4 = 100

medio_jogador_1 = (jogador_1 + jogador_2+ jogador_3 + jogador_4) /4   
media_ex_jogador = (ex_jogador_1 + ex_jogador_2 + ex_jogador_3 + ex_jogador_4) / 4

print ("TIME 1" , medio_jogador_1)
print ("TIME 2" , media_ex_jogador)

if medio_jogador_1 > media_ex_jogador :
    time_vantagem = 1
    print ("VANTAGEM TIME-1 :"  ), 
elif media_ex_jogador > medio_jogador_1:
    time_visitante_vatagem = 1 
    print ("VANTAGEM TIME-2 :" ) ,
else :
    print("impate")   
    
    
print( "-" * 90)
print("")
print (f"PRIMEIRO JOGO FOI: {time_casa} 1 x {time_visitante} 2")
print()
placar_anterior =1,2 


print (f"QUANTO ACHA QUE IRA SER O PROXIMO JOGO:")
placar_time1 = int(input("TIME-1 PLACAR:"))
placar_time2 = int(input("TIME-2 PLACAR:"))

placar = placar_time1,placar_time2
print (placar)
print (placar[0])
print (placar[1])

print (f"NO AGRAGADO ESTA {placar[0] + placar_anterior[0]} a {placar[1] + placar_anterior[1]}")


placar_agregado = placar[0] + placar_anterior[0] , placar[1] + placar_anterior[1]


if placar_agregado[0] > placar_agregado[1]    :
    if medio_jogador_1 > media_ex_jogador :
        print (f"Time {time_casa} COM {placar_agregado} 100% NA FINAL") ,
    else:
        print (f"Time {time_casa} TEM 80% DE CHANCE")      

elif placar_agregado[0] < placar_agregado[1]    :
    print (f"Time {time_visitante} clasificou"),

else:
    if medio_jogador_1 > media_ex_jogador :
        print (f"MEDIA : {medio_jogador_1} SER MAIOR. {time_casa} CLASIFICA") ,
    else:
        print (f"MEDIA : {media_ex_jogador} SER MAIOR. {time_visitante} CLASIFICA") ,





