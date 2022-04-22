#Marco Antonio Gardida Cortés A01423221
#Silvio Emmanuel Prieto Caro A01423341
#Miguel Jiménez Padilla A01423189



casocomentario = True
casooperacion = False

def essigno(line, i):
    if(line[i] == '*' or line[i] == '+' or line[i] == '-'  or line[i] == '^' or line[i] == '/'):
        return True
    else:
        return False
    '''elif((casocomentario) and line[i] == '/' and not line[i+1] == '/'):
        return True
    elif(casocomentario==False and line[i] == '/'):
        return True'''
    


def CasoVariableAsignacion(line, i):
    while(i<len(line)):
        if(line[i].isalpha() or isinstance(line[i], int) or line[i] == '_'):
            pass
        elif(line[i] == '='):
            break
        else:
            print(line[0:i] + '  ----->  Error')
            return -1
        i+=1

    print(line[0:i-1] + '  ----->  Variable')
    print(line[i] + '  ----->  Asignación')
    

    return i


def CasoVariable(line, i):
    index = i
    while(i<len(line)):
        if(line[i].isalpha() or isinstance(line[i], int) or line[i] == '_'):
            pass
        elif(essigno(line, i)):
            break
        else:
            print(line[index:i] + '  ----->  Error')
            return -1
        #print(i)
        i+=1

    print(line[index:i-1] + '  ----->  Variable')
    if(line[i] == '/' and line[i+1] == '/'):
        casocomentario = True
        casooperacion = False
        return i
    else:
        casocomentario = False
        casooperacion = True
        if(line[i] == '*'):
            print(line[i] + '  ----->  Multiplicación')
        elif(line[i] == '+'):
            print(line[i] + '  ----->  Suma')
        elif(line[i] == '-'):
            print(line[i] + '  ----->  Resta')
        elif(line[i] == '/' ):
            print(line[i] + '  ----->  División')
        elif(line[i] == '^'):
            print(line[i] + '  ----->  Potencia')
        return i

def casoE(index,i,line):
    i+=1
    real = False
    if(i=='-'):
        real = True
        i+=1
    elif(i=='+'):
        i+=1

    if(isinstance(line[i], int)):
        pass
    else:
        print(line[index:i] + '  ----->  Error')
        return -1

    while(i<len(line)):
        if(isinstance(line[i], int)):
            pass
        elif(essigno(line, i)):
            break
        else:
            print(line[index:i] + '  ----->  Error')
            return -1
        i+=1
        
    if(real):
        print(line[index:i-1] + '  ----->  Real')
    else:
        print(line[index:i-1] + '  ----->  Entero')

    if(line[i] == '*'):
        print(line[i] + '  ----->  Multiplicación')
    elif(line[i] == '+'):
        print(line[i] + '  ----->  Suma')
    elif(line[i] == '-'):
        print(line[i] + '  ----->  Resta')
    elif(line[i] == '/' ):
        print(line[i] + '  ----->  División')
    elif(line[i] == '^'):
        print(line[i] + '  ----->  Potencia')

    return i


        




def flotanteoentero(line, i):
    index = i
    #numero = ''
    flotante = False
    countpunto = 0
    while(i<len(line)):
        if(isinstance(line[i], int)):
            #numero += line[i]
            pass
        elif(line[i] == '.'):
            countpunto += 1
            if(countpunto > 1):
                print(line[index:i] + '  ----->  Error')
                return -1
            elif(isinstance(line[i+1], int)):
                flotante = True
            else:
                print(line[index:i] + '  ----->  Error')
                return -1
        elif(essigno(line, i)):
            break
        elif(line[i] == 'E' or line[i] == 'e'):
            return casoE(index,i,line)

        else:
            print(line[index:i] + '  ----->  Error')
            return -1
        i+=1
    if(flotante):
        print(line[index:i-1] + '  ----->  Real')
    else:
        print(line[index:i-1] + '  ----->  Entero')

    if(line[i] == '*'):
        print(line[i] + '  ----->  Multiplicación')
    elif(line[i] == '+'):
        print(line[i] + '  ----->  Suma')
    elif(line[i] == '-'):
        print(line[i] + '  ----->  Resta')
    elif(line[i] == '/' ):
        print(line[i] + '  ----->  División')
    elif(line[i] == '^'):
        print(line[i] + '  ----->  Potencia')

    return i




  


def lexerAritmetico(archivo):
    with open(archivo) as f:
        line = f.readline()
        
        while line:
            casovarasig = True
            casocomentario = True
            casonumero = False
            casovar = False
            casoParentesis = False
            casooperacion = False
            line = f.readline()
            line = line.replace(" ","")
            i=0
            #print('kiti: ' + line)
            while(i<len(line)):
                if(casocomentario and line[i] == '/' and line[i+1] == '/'):
                    
                    print(line[i:] + '  ----->  Comentario')
                    break
                elif(casovarasig  and line[i].isalpha()):
                    i = CasoVariableAsignacion(line, i)
                    if(1 == -1):
                        break
                    casovarasig = False
                    casocomentario = False
                    casonumero = True
                    casovar = True
                elif(casonumero and isinstance(line[i], int)):
                    i = flotanteoentero(line, i)
                    if(1 == -1):
                        break
                    elif(essigno(line,i)):
                        casooperacion = True
                    else:
                        casooperacion = False
                        casocomentario = True
                elif(casovar and line[i].isalpha()):
                    i = CasoVariable(line, i)
                    if(1 == -1):
                        break
                    if(casocomentario):
                        i-=2
                else:
                    print(line[i:] + '  ----->  Error')
                    break


                i+=1
                

        if(casooperacion):
                print(line[i:] + '  ----->  Error (NO SE COMPLETÓ LA OPERACIÓN)')



#file = input()
#lexerAritmetico(file)
lexerAritmetico('p1.txt')