import os
os.system("cls")
pares=0
impares=0
soma_pares=0
soma_geral=0
contador_geral=0

while True:
    numero=int(input("digite um número:"))
    if numero > 0:
        contador_geral += 1
        soma_geral += numero
        if numero % 2 == 0:
            pares +=1
            soma_geral +=numero
        else:
            impares += 1
            if numero ==0:
                break 

            #calculando
            if pares !=0:
                media_pares= soma_pares/pares
            else:
                media_pares=0
           
            media_pares = soma_geral/contador_geral

            if contador_geral!=0:
                media_geral=soma_geral/contador_geral
            else:
                media_geral= 0
print(f"\nquantidade de pares:{pares}")
print(f"\nquantidade de impares:{impares}")
print(f"\nmedia pares:{media_pares}")
print(f"\nmedia geral:{media_geral}")

