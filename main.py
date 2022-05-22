#Marco Antonio Gardida Cortés A01423221
#Silvio Emmanuel Prieto Caro A01423341
#Miguel Jiménez Padilla A01423189

def signo(line, i):
    if(line[i] == '*' or line[i] == '+'  or line[i] == '^' or line[i] == '/'):
        return True
    else:
        return False


def CasoVariable(line, i,variable):
    while(i<len(line)):
        if(line[i].isalpha() or line[i].isdigit() or line[i] == '_'):
            variable += line[i]
        else:
            break
        i+=1

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
    while(i<len(line)):
        if(line[i].isdigit()):
            numero += line[i]
        elif(line[i] == '.'):
            if(line[i+1].isdigit() and countpunto < 1):
                numero += line[i]
                countpunto += 1
                flotante = True
            else:
                print(numero + '       ----->          ErrorNum')
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
        casooperacion = False
        curr = ''
        var = ''
        restare = False
        primercaso = False
        #ParentesisCount
        parentesisAbierto = 0
        parentesisCerrado = 0
        while(i<len(line)):
            if(comentario and line[i] == '/' and line[i+1] == '/'):
                    print(line[i:] + '       ----->          Comentario')
                    break
            elif(casovar and line[i].isalpha()):#Caso variable
                i = CasoVariable(line, i,var)
                if casovariableasignacion:
                    casovar = False
                    casonum = False
                    comentario = False
                    casosim = False
                    casooperacion = False
                    primercaso = False
                    curr = 'Variable'
                    restare = False
                    var = ''
                else:
                    casovar = False
                    casonum = False
                    comentario = True
                    casosim = True
                    casooperacion = False
                    primercaso = False
                    curr = 'Variable'
                    restare = False
                    var = ''

            elif(casonum and casovariableasignacion == False and line[i].isdigit() ):#Caso números
                    i = CasoNumero(line,i,var)
                    casovar = False
                    casonum = False
                    comentario = True
                    casosim = True
                    casooperacion = False
                    primercaso = False
                    curr = 'Número'
                    restare = False
                    var = ''
            elif((casosim or restare or primercaso ) and casovariableasignacion == False and line[i] == '-'):
                
                if( curr != 'Variable' and curr != 'Número'):
                    casovar = True
                    casonum = True
                    comentario = False
                    casosim = False
                    casooperacion = True
                    primercaso = False
                    restare = False
                    curr = 'Símbolo'
                    var = '-'    
                else:
                    casovar = True
                    casonum = True
                    comentario = False
                    casosim = False
                    casooperacion = True
                    restare = False
                    curr = 'Símbolo'
                    var = ''
                    print(line[i] + '       ----->          Resta')
            elif(casosim and casovariableasignacion == False and signo(line, i) ):
                    restare = False
                    if(line[i] == '+'):
                        curr = 'Símbolo'
                        casovar = True
                        casonum = True
                        comentario = False
                        casosim = False
                        casooperacion = True
                        var = ''
                        print(line[i] + '       ----->          Suma')
                    elif(line[i] == '*'):
                        curr = 'Símbolo'
                        casovar = True
                        casonum = True
                        comentario = False
                        casosim = False
                        casooperacion = True
                        var = ''
                        print(line[i] + '       ----->          Multiplicación')
                    elif(line[i] == '/'):
                        curr = 'Símbolo'
                        casovar = True
                        casonum = True
                        comentario = False
                        casosim = False
                        casooperacion = True
                        var = ''
                        print(line[i] + '       ----->          División')
                    elif(line[i] == '^' ):
                        curr = 'Símbolo'
                        casovar = True
                        casonum = True
                        comentario = False
                        casosim = False
                        casooperacion = True
                        var = ''
                        print(line[i] + '       ----->          Potencia')
                    
                        

                    else:
                        print(line[i] + '       ----->          Error')
                        casooperacion = False
                        break
            

            elif(casovariableasignacion == False and  line[i] == '('):
                if(curr == 'Símbolo' or primercaso):
                    if(var== '-'):
                        print( '-       ----->          Resta')
                    curr = 'ParéntesisA'
                    casovar = True
                    casonum = True
                    comentario = False
                    casosim = False
                    casooperacion = False
                    primercaso = False
                    restare = True
                    var = ''
                    parentesisAbierto += 1
                    print(line[i] + '       ----->          Paréntesis que abre')
                else:
                    print(line[i] + '       ----->          ErrorPA')
                    break
            elif( casovariableasignacion == False and  line[i] == ')'):
                if(curr == 'Variable' or curr == 'Número' ):
                    curr = 'ParéntesisC'
                    casovar = False
                    casonum = False
                    comentario = True
                    casosim = True
                    casooperacion = False
                    restare = False
                    var = ''
                    parentesisCerrado += 1
                    print(line[i] + '       ----->          Paréntesis que cierra')
                else:
                    print(line[i] + '       ----->          ErrorPC')
                    break
            elif(line[i] == ' '):
                pass
            elif(line[i] == '=' and casovariableasignacion):
                        casovariableasignacion = False
                        casovar = True
                        casonum = True
                        comentario = False
                        casosim = False
                        casooperacion = False
                        primercaso = True
                        curr = 'Asignación'
                        var = ''
                        print('=       ----->          Asignación')
            else:
                print(line[i] + '          ----->       Error-main')
                break
            if(i == -1):
                break
            i+=1
            #print(curr)

        if(parentesisAbierto != parentesisCerrado):
            print('          ----->       Error, faltó un paréntesis')
        if(casooperacion):
            print('          ----->       Error, quedó una operación inconclusa')
        


#Escritura de 
def lexerAritmetico(archivo):
    with open(archivo) as f_in:
        lines = (line.rstrip() for line in f_in) 
        lines = list(line for line in lines if line) # Non-blank lines in a list
        main(lines)
            
            
            


            


#lexerAritmetico('P1pruebas.txt')
lexerAritmetico('p1.txt')


