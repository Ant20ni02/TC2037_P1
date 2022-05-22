#Marco Antonio Gardida Cortés A01423221
#Silvio Emmanuel Prieto Caro A01423341
#Miguel Jiménez Padilla A01423189

from asyncore import write
import webbrowser


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

    writeInterface('        <span style="color: #40CFFF;" class="objects">')
    writeInterface("\n")
    writeInterface(str("            " + variable))
    writeInterface("\n")
    writeInterface("        </span>")

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
        print(numero + '       ----->          ErrorCorto')

        writeInterface('        <span class = "endSquareError">')
        writeInterface("\n")
        writeInterface("→ Error ")
        writeInterface("\n")
        writeInterface("        </span>")

        return -1

    while(i<len(line)):
        if(line[i].isdigit()):
            numero += line[i]
        else:
            break
        i+=1
    if(real):
        print(numero + '       ----->          Real')

        writeInterface('        <span style="color: pink;" class="objects">')
        writeInterface("\n")
        writeInterface(str("            " + numero))
        writeInterface("\n")
        writeInterface("        </span>")
    else:
        print(numero + '       ----->          Entero')

        writeInterface('        <span style="color: orange;" class="objects">')
        writeInterface("\n")
        writeInterface(str("            " + numero))
        writeInterface("\n")
        writeInterface("        </span>")

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
                print(numero + '       ----->          ErrorCorto')

                writeInterface('        <span class = "endSquareError">')
                writeInterface("\n")
                writeInterface("→ Error ")
                writeInterface("\n")
                writeInterface("        </span>")

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

        writeInterface('        <span style="color: pink;" class="objects">')
        writeInterface("\n")
        writeInterface(str("            " + numero))
        writeInterface("\n")
        writeInterface("        </span>")
    else:
        print(numero + '       ----->          Entero')

        writeInterface('        <span style="color: orange;" class="objects">')
        writeInterface("\n")
        writeInterface(str("            " + numero))
        writeInterface("\n")
        writeInterface("        </span>")

        

    return i-1


def writeInterface(line):
    with open("app.html",'a') as f:
        f.write(line)



def main(lines):
    for line in lines:
        print("Línea Actual: "+ line)
        i=0

        ####### top div #########
        writeInterface("\n")
        writeInterface('    <div style = "margin-top: 1em;">')
        writeInterface("\n")
        #########################

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

                    writeInterface('        <span style="color: #AB9144;" class="objects">')
                    writeInterface("\n")
                    writeInterface(str("            " + line[i:]))
                    writeInterface("\n")
                    writeInterface("        </span>")

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

                    writeInterface('        <span style="color: green;" class="objects">')
                    writeInterface("\n")
                    writeInterface(str("            " + "-"))
                    writeInterface("\n")
                    writeInterface("        </span>")

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

                        writeInterface('        <span style="color: purple;" class="objects">')
                        writeInterface("\n")
                        writeInterface(str("            " + "+"))
                        writeInterface("\n")
                        writeInterface("        </span>")

                    elif(line[i] == '*'):
                        curr = 'Símbolo'
                        casovar = True
                        casonum = True
                        comentario = False
                        casosim = False
                        casooperacion = True
                        var = ''
                        print(line[i] + '       ----->          Multiplicación')

                        writeInterface('        <span style="color: brown;" class="objects">')
                        writeInterface("\n")
                        writeInterface(str("            " + "*"))
                        writeInterface("\n")
                        writeInterface("        </span>")

                    elif(line[i] == '/'):
                        curr = 'Símbolo'
                        casovar = True
                        casonum = True
                        comentario = False
                        casosim = False
                        casooperacion = True
                        var = ''
                        print(line[i] + '       ----->          División')

                        writeInterface('        <span style="color: gray;" class="objects">')
                        writeInterface("\n")
                        writeInterface(str("            " + "/"))
                        writeInterface("\n")
                        writeInterface("        </span>")

                    elif(line[i] == '^' ):
                        curr = 'Símbolo'
                        casovar = True
                        casonum = True
                        comentario = False
                        casosim = False
                        casooperacion = True
                        var = ''
                        print(line[i] + '       ----->          Potencia')

                        writeInterface('        <span style="color: #efc90b;" class="objects">')
                        writeInterface("\n")
                        writeInterface(str("            " + "^"))
                        writeInterface("\n")
                        writeInterface("        </span>")
                    
                        

                    else:
                        print(line[i] + '       ----->          ErrorCorto')

                        writeInterface('        <span class = "endSquareError">')
                        writeInterface("\n")
                        writeInterface("→ Error ")
                        writeInterface("\n")
                        writeInterface("        </span>")

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

                    writeInterface('        <span style="color: blue;" class="objects">')
                    writeInterface("\n")
                    writeInterface(str("            " + "("))
                    writeInterface("\n")
                    writeInterface("        </span>")

                else:
                    print(line[i] + '       ----->          ErrorCorto')

                    writeInterface('        <span class = "endSquareError">')
                    writeInterface("\n")
                    writeInterface("→ Error ")
                    writeInterface("\n")
                    writeInterface("        </span>")
                    
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

                    writeInterface('        <span style="color: blue;" class="objects">')
                    writeInterface("\n")
                    writeInterface(str("            " + ")"))
                    writeInterface("\n")
                    writeInterface("        </span>")

                else:
                    print(line[i] + '       ----->          ErrorCorto')

                    writeInterface('        <span class = "endSquareError">')
                    writeInterface("\n")
                    writeInterface("→ Error ")
                    writeInterface("\n")
                    writeInterface("        </span>")

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

                        writeInterface('        <span style="color: red;" class="objects">')
                        writeInterface("\n")
                        writeInterface(str("            " + "="))
                        writeInterface("\n")
                        writeInterface("        </span>")
            else:
                print(line[i] + '          ----->       ErrorCorto')

                writeInterface('        <span class = "endSquareError">')
                writeInterface("\n")
                writeInterface("→ Error ")
                writeInterface("\n")
                writeInterface("        </span>")

                break
            if(i == -1):
                break
            i+=1
            #print(curr)

        ########## bottom close div ############
        writeInterface("\n")
        writeInterface('    </div>')
        writeInterface("\n")

        ########################################

        if(parentesisAbierto != parentesisCerrado):
            print('          ----->       ErrorLargo')

            writeInterface('        <span class = "endSquareError">')
            writeInterface("\n")
            writeInterface("→ Error ")
            writeInterface("\n")
            writeInterface("        </span>")

        if(casooperacion):
            print('          ----->       ErrorLargo')

            writeInterface('        <span class = "endSquareError">')
            writeInterface("\n")
            writeInterface("→ Error ")
            writeInterface("\n")
            writeInterface("        </span>")
        


#Escritura de 
def lexerAritmetico(archivo):
    with open(archivo) as f_in:
        lines = (line.rstrip() for line in f_in) 
        lines = list(line for line in lines if line) # Non-blank lines in a list
        main(lines)
        ####
        writeInterface("\n")
        writeInterface("\n")
        writeInterface("\n")

        writeInterface("    </body>")
        writeInterface("\n")    
        writeInterface("</html>")

        webbrowser.open_new_tab("./app.html")
            
            
#lexerAritmetico('P1pruebas.txt')
lexerAritmetico('P1pruebas.txt')


