#Marco Antonio Gardida Cortés A01423221
#Silvio Emmanuel Prieto Caro A01423341
#Miguel Jiménez Padilla A01423189


def signo(line, i):
    if(line[i] == '*' or line[i] == '+' or line[i] == '-'  or line[i] == '^' or line[i] == '/' ):
        return True
    else:
        return False


def CasoVariable(line, i):
    variable = ''
    while(i<len(line)-1):
        if(line[i].isalpha() or line[i].isdigit() or line[i] == '_'):
            variable += line[i]
        else:
            break
        i+=1

    print(variable + '  ----->  Variable')
    return i-1


def casoE(line,i, numero):
    numero += line[i]
    i+=1
    real = False
    if(line[i]=='-'):
        real = True
        i+=1
        numero += line[i]
    elif(line[i]=='+'):
        i+=1
        numero += line[i]

    if(line[i].isdigit()):
        pass
    else:
        print(numero + '  ----->  Error')
        return -1

    while(i<len(line)-1):
        if(line[i].isdigit()):
            pass
        else:
            break
        i+=1
    if(real):
        print(numero + '  ----->  Real')
    else:
        print(numero + '  ----->  Entero')

        

    return i-1


def CasoNumero(line, i):
    numero = ''
    flotante = False
    countpunto = 0
    while(i<len(line)-1):
        if(line[i].isdigit()):
            numero += line[i]
        elif(line[i] == '.'):
            if(line[i+1].isdigit() and countpunto < 1):
                numero += line[i]
                countpunto += 1
                flotante = True
            else:
                print(numero + '  ----->  Error')
                return -1
        elif(line[i] == 'E' or line[i] == 'e'):
            return casoE(line,i, numero)
        else:
            break
        i+=1
    if(flotante):
        print(numero + '  ----->  Real')
    else:
        print(numero + '  ----->  Entero')

    return i-1




def lexerAritmetico(archivo):
    with open(archivo) as f:
        line = f.readline()
        while line:
            casooperacion = False
            casovariableasignacion = True
            comentario = True
            casosolosigno = False
            casoparentesis = False
            line = f.readline()
            line = line.replace(" ","")
            i=0
            while(i<len(line)-1):
                if(comentario and line[i] == '/' and line[i+1] == '/'):
                    print(line[i:] + '  ----->  Comentario')
                    break
                elif(line[i].isalpha()):
                    i = CasoVariable(line, i)
                    if(casovariableasignacion):
                        i+=1
                        if(line[i] == '='):
                            print(line[i] + '          ----->       Asignación')
                            casovariableasignacion = False
                            comentario = False
                        else:
                            print(line[i] + '          ----->       Error')
                            break
                    else:
                        comentario = True
                        casooperacion = False
                elif(line[i].isdigit()):#Caso números
                    i = CasoNumero(line,i)
                    comentario = True
                    casocperacion = False
                    if(i == -1):
                        break
                elif(signo(line, i)):
                    if(line[i] == '-'):
                        print(line[i] + '  ----->  Resta')
                    elif(line[i] == '+'):
                        print(line[i] + '  ----->  Suma')
                    elif(line[i] == '*'):
                        print(line[i] + '  ----->  Multiplicación')
                    elif(line[i] == '/' ):
                        print(line[i] + '  ----->  División')
                    elif(line[i] == '^'):
                        print(line[i] + '  ----->  Potencia')
                        casocperacion = True
                else:
                    print(line[i] + '          ----->       Error')

                i+=1
                #print('Kiti: ' + str(i))
                



#file = input()
#lexerAritmetico(file)
lexerAritmetico('p1.txt')