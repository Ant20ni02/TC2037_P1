#Marco Antonio Gardida Cortés A01423221
#Silvio Emmanuel Prieto Caro A01423341
#Miguel Jiménez Padilla A01423189

def signo(line, i):
    if(line[i] == '*' or line[i] == '+' or line[i] == '-'  or line[i] == '^' or line[i] == '/' ):
        return True
    else:
        return False


def CasoVariable(line, i,variable, variableasignacion):
    if(variable == '-'):
        i+=1
    while(i<len(line)):
        if(line[i].isalpha() or line[i].isdigit() or line[i] == '_'):
            variable += line[i]
        else:
            break
        i+=1
    if(variableasignacion):
        pass
    else:
        print(variable + '       ----->          Variable')
    return i-1


def casoE(line,i, numero):
    real = False
    
    if(i != len(line) and line[i]=='-'):
        numero += line[i]
        real = True
        i+=1
    elif(i != len(line) and line[i]=='+'):
        numero += line[i]
        i+=1
        
    if(i != len(line) and line[i].isdigit()):
        pass
    else:
        print(numero + '       ----->          Error')
        return -1

    while(i<len(line)):
        if(line[i].isdigit()):
            numero += line[i]
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
            numero += line[i]
            i+=1
            return casoE(line,i, numero)
        else:
            break
        i+=1
    if(flotante):
        print(numero + '       ----->          Real')
    else:
        print(numero + '       ----->          Entero')

    return i-1






def main(lines):
    for line in lines:
        print("Línea Actual: "+ line)
        i=0
        #Casos activos
        casovariableasignacion = True
        casovar = True
        casonum = False
        casosim = False
        comentario = True
        #ParentesisCount
        parentesisAbierto = 0
        parentesisCerrado = 0
        while(i<len(line)):
            if(comentario and line[i] == '/' and line[i+1] == '/'):
                    print(line[i:] + '       ----->          Comentario')
                    break
            elif(casovar and line[i].isalpha()):#Caso variable
                    if(casovariableasignacion):
                        xd = i
                        i = CasoVariable(line, i,'',casovariableasignacion)
                        i+=1
                        if(line[i] == '=' or (line[i] == ' ' and line[i+1] == '=' )):
                            print( line[xd:i] +'       ----->          Variable')
                            print( '=' +'       ----->          Asignación')
                            i+=1
                            casovariableasignacion = False
                            casovar = True
                            casonum = True
                            comentario = False
                            casosim = False
                        else:
                            print(line[i] + '       ----->          Error')
                            break
                    else:
                        i = CasoVariable(line, i,'',casovariableasignacion)
                        casovar = False
                        casonum = False
                        comentario = True
                        casosim = True

            elif(line[i].isdigit()):#Caso números
                    i = CasoNumero(line,i,'')
                    casovar = False
                    casonum = False
                    comentario = True
                    casosim = True
            elif(signo(line, i)):  
                    if(line[i] == '-' and line[i-1] != '-'):
                        #print('kiti')
                        if( (not line[i-1].isdigit()) and (not line[i-1].isalpha())):
                            if(line[i+1].isdigit()):
                                print('kiti')
                                i = CasoNumero(line,i,'-')
                                casooperacion = False 
                                casovar = False
                                casonum = True
                                casosim = False
                            elif(line[i+1].isalpha()):
                                i = CasoVariable(line,i,'-')
                                casooperacion = False 
                                casovar = True
                                casonum = False
                                casosim = False
                        else:
                            casovar = False
                            casonum = False
                            casosim = True
                            print(line[i] + '       ----->          Resta')
                            casooperacion = True

                    elif(line[i] == '+' and ((line[i-1] == ')') or (line[i-1].isdigit()) or (line[i-1].isalpha()))):
                        print(line[i] + '       ----->          Suma')
                        casooperacion = True
                        casovar = False
                        casonum = False
                        casosim = True
                    elif(line[i] == '*'and ((line[i-1] == ')') or (line[i-1].isdigit()) or (line[i-1].isalpha()))):
                        print(line[i] + '       ----->          Multiplicación')
                        casooperacion = True
                        casovar = False
                        casonum = False
                        casosim = True
                    elif(line[i] == '/' and ((line[i-1] == ')') or (line[i-1].isdigit()) or (line[i-1].isalpha()))):
                        print(line[i] + '       ----->          División')
                        casooperacion = True
                        casovar = False
                        casonum = False
                        casosim = True
                    elif(line[i] == '^' and ((line[i-1] == ')') or (line[i-1].isdigit()) or (line[i-1].isalpha()))):
                        print(line[i] + '       ----->          Potencia')
                        casooperacion = True
                        casovar = False
                        casonum = False
                        casosim = True
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
                    parentesisCerrado += 1
                    casovar = False
                    casonum = False
                    print(line[i] + '       ----->          Paréntesis que cierra')
                else:
                    print(line[i] + '       ----->          Error')
                    break
            elif(line[i] == ' '):
                pass
            else:
                print(line[i] + '          ----->       ErrorA')
                break
            if(i == -1):
                break
            i+=1

        if(parentesisAbierto != parentesisCerrado):
            print('          ----->       Error, faltó un paréntesis')
        


#Escritura de 
def lexerAritmetico(archivo):
    with open(archivo) as f_in:
        lines = (line.rstrip() for line in f_in) 
        lines = list(line for line in lines if line) # Non-blank lines in a list
        main(lines)
            
            
            


            


#lexerAritmetico('P1pruebas.txt')
lexerAritmetico('p1.txt')


