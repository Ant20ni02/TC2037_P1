#Marco Antonio Gardida Cortés A01423221
#Silvio Emmanuel Prieto Caro A01423341
#Miguel Jiménez Padilla A01423189






def signo(line, i):
    if(line[i] == '*' or line[i] == '+' or line[i] == '-'  or line[i] == '^' or line[i] == '/' ):
        return True
    else:
        return False


def CasoVariable(line, i,variable):
    if(variable == '-'):
        i+=1
    while(i<len(line)):
        if(line[i].isalpha() or line[i].isdigit() or line[i] == '_'):
            variable += line[i]
        else:
            break
        i+=1
    print(variable + '       ----->          Variable')
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
        print(numero + '       ----->          Error')
        return -1

    while(i<len(line)-1):
        if(line[i].isdigit()):
            pass
        else:
            break
        i+=1
    if(real):
        print(numero + '       ----->          Real')
    else:
        print(numero + '       ----->          Entero')

        

    return i-1


def CasoNumero(line, i,numero):
    flotante = False
    countpunto = 0
    if(numero == '-'):
        i+=1
    #print(i)
    while(i<len(line)):
        if(line[i].isdigit()):
            numero += line[i]
        elif(line[i] == '.'):
            if(line[i+1].isdigit() and countpunto < 1):
                numero += line[i]
                countpunto += 1
                flotante = True
            else:
                print(numero + '       ----->          Error')
                return -1
        elif(line[i] == 'E' or line[i] == 'e'):
            return casoE(line,i, numero)
        else:
            break
        i+=1
    if(flotante):
        print(numero + '       ----->          Real')
    else:
        print(numero + '       ----->          Entero')

    return i-1









def lexerAritmetico(archivo):
    with open(archivo) as f:
        line = f.readline()
        while line:
            #casos
            casovar = False
            casonum = False
            casosim = False
            #------
            casovariableasignacion = True
            casooperacion = False
            comentario = True
            parentesisAbierto = 0
            parentesisCerrado = 0
            line = f.readline()
            line = line.replace(" ","")
            i=0
            while(i<len(line)):
                if(comentario and line[i] == '/' and line[i+1] == '/'):
                    print(line[i:] + '       ----->          Comentario')
                    break
                elif(line[i].isalpha()):
                    
                    if(not line[i-1].isdigit() and i >0):
                        i = CasoVariable(line, i,'')
                        casovar = True
                        casonum = False
                        casosim = False
                        casooperacion = False
                    elif(line[i-1].isdigit() and i >0):
                        print(line[i] + '       ----->          Error')
                        break

                    if(casovariableasignacion):
                        i = CasoVariable(line, i,'')
                        casooperacion = False
                        i+=1
                        if(line[i] == '='):
                            print(line[i] + '       ----->          Asignación')
                            casovariableasignacion = False
                            comentario = False
                        else:
                            print(line[i] + '       ----->          Error')
                            break
                    else:
                        comentario = True
                        casooperacion = False
                elif(line[i].isdigit()):#Caso números
                    i = CasoNumero(line,i,'')
                    comentario = True
                    casooperacion = False
                    casovar = False
                    casonum = True
                    casosim = False
                    if(i == -1):
                        break
                elif(signo(line, i)):
                    casovar = False
                    casonum = False
                    casosim = True
                    if(line[i] == '-' and line[i-1] == '-'):
                        if( (not line[i-1].isdigit()) and (not line[i-1].isalpha())):
                            if(line[i+1].isdigit()):
                                i = CasoNumero(line,i,'-')
                                casooperacion = False 
                            elif(line[i+1].isalpha()):
                                i = CasoVariable(line,i,'-')
                                casooperacion = False 
                        else:
                            print(line[i] + '       ----->          Resta')
                            casooperacion = True

                    elif(line[i] == '+' and ((line[i-1] == ')') or (line[i-1].isdigit()) or (line[i-1].isalpha()))):
                        print(line[i] + '       ----->          Suma')
                        casooperacion = True
                    elif(line[i] == '*'and ((line[i-1] == ')') or (line[i-1].isdigit()) or (line[i-1].isalpha()))):
                        print(line[i] + '       ----->          Multiplicación')
                        casooperacion = True
                    elif(line[i] == '/' and ((line[i-1] == ')') or (line[i-1].isdigit()) or (line[i-1].isalpha()))):
                        print(line[i] + '       ----->          División')
                        casooperacion = True
                    elif(line[i] == '^' and ((line[i-1] == ')') or (line[i-1].isdigit()) or (line[i-1].isalpha()))):
                        print(line[i] + '       ----->          Potencia')
                        casooperacion = True
                    elif(line[i] == line[i-1] ):
                        print(line[i] + '       ----->          Error')
                        break
                    else:
                        print(line[i] + '       ----->          Error')
                        break

                elif(line[i] == '('):
                    if(casosim):
                        casosim = False
                        parentesisAbierto += 1
                        print(line[i] + '       ----->          Paréntesis que abre')
                    else:
                        print(line[i] + '       ----->          Error')
                        break
                elif(line[i] == ')'):
                    if(casovar or casonum):
                        casovar = False
                        casonum = False
                        print(line[i] + '       ----->          Paréntesis que cierra')
                    else:
                        print(line[i] + '       ----->          Error')
                        break

                else:
                    print(line[i] + '          ----->       Error')
                i+=1

            if(casooperacion):
                print('          ----->       Error, quedó una operación pendiente')
            elif(parentesisAbierto != parentesisCerrado):
                print('          ----->       Error, faltó un paréntesis')

                
                #print('Kiti: ' + str(i))
                



#file = input()
#lexerAritmetico(file)
lexerAritmetico('P1pruebas.txt')