game = [["☐","☐","☐","☐","☐"],["☐","☐","☐","☐","☐"],["☐","☐","☐","☐","☐"],["☐","☐","☐","☐","☐"],["☐","☐","☐","☐","☐"]]

ganar_nada= "☑"
perder_nada = "🖾"

ls_rpreguntas = ["Que es paiton?\n\n1. Game \n2. Lenguaje de programación\n3. Marca de carro \n4. Ninguna de ninguna ",
"Que es acheteemeele \n\n1. Lenguaje de maquetizacsion \n2. Marca de gasiosa \n3. Navegador que se navega\n4. Jot doc,",
]

ls_respueta= ["2","1"]


def fnt_pintarMatriz():
    for i in range(len(game)):
        for j in range(len(game[i])):
            print(game[i][j], end= " " )
        print()
        
sw = True 
contador = 0
for i in range(len(game)):
    for j in range(len(game[i])):
        import os
        os.system("cls")
        fnt_pintarMatriz()
        print()
        print(ls_rpreguntas[contador])
        print()
        r = input("-->")
        if r == ls_respueta[contador]:
            game[i][j] = ganar_nada
        else:
            game[i][j] = perder_nada
        contador += 1
        
        
