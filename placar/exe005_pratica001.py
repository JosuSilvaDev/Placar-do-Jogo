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
    print ("VANTAGEM CORINTHIAS :"  ), 
elif media_ex_jogador > medio_jogador_1:
    time_visitante_vatagem = 1 
    print ("VANTAGEM PALMEIRAS :" ) ,
else :
    print("IMPATE")   
    
    
print( "-" * 90 )

print (f"PRIMEIRO JOGO FOI: \t{time_casa} 1 x {time_visitante} 2")
print()
placar_anterior =1,2 


print (f"QUANTO ACHA QUE IRA SER O PROXIMO JOGO:")
placar_time1 = int(input("TIME DA CASA PLACAR:"))
placar_time2 = int(input("TIME VISITANTE PLACAR:"))

placar = placar_time1,placar_time2
print (placar)

print (f"NO AGRAGADO ESTA \t{placar[0] + placar_anterior[0]} X {placar[1] + placar_anterior[1]}")


placar_agregado = placar[0] + placar_anterior[0] , placar[1] + placar_anterior[1]


if placar_agregado[0] > placar_agregado[1]    :
    if medio_jogador_1 > media_ex_jogador :
        print (f"MEDIA : {medio_jogador_1} SER MAIOR. {time_casa} CLASIFICA") ,
    else:
        print (f"{media_ex_jogador} SER MAIOR. E TER VENCIADO DE {placar_agregado}POREM COM O PLACAR DE {placar_agregado[0]} X {placar_agregado[1]} O TIME {time_casa} CLASIFICA COM 70% DE CHANCE") ,     

elif placar_agregado[0] < placar_agregado[1]    :
    print (f"Time {time_visitante} clasificou"),

else:
    if medio_jogador_1 > media_ex_jogador :
        print (f"MEDIA : {medio_jogador_1} SER MAIOR. {time_casa} CLASIFICA") ,
    else:
        print (f"MEDIA : {media_ex_jogador} SER MAIOR. {time_visitante} CLASIFICA") , 





