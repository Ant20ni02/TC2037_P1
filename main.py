#Marco Antonio Gardida Cortés A01423221
#Silvio Emmanuel Prieto Caro A01423341
#Miguel Jiménez Padilla A01423189


def lexerAritmetico(archivo):
    with open(archivo) as f:
        line = f.readline()
        casovar= False
        while line:
            line = f.readline()
            i=0
            print('kiti: ' + line)
            while(i<len(line)):
                if(line[i] == '/' and line[i+1] == '/'):
                    print(line[i:] + "    Comentario")
                    break
                if(line[i].isalpha()):
                    casovar = True

                    
                i+=1



#file = input()
#lexerAritmetico(file)
lexerAritmetico('P1_pruebas_.txt')