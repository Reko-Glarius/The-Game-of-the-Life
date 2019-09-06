#########################################################  Datos  ############################################################
"""
Nombres Integrantes:
Ramo:
Seccion:
Fecha:
"""
#######################################################  Librerias  ##########################################################
import os ##Libreria para limpiar pantalla
#######################################################  Funciones  ##########################################################
def transtoint(matriz): ##Transforma los numeros desde el tipo str al tipo int
    a=[]
    matriz_a=[]
    for fila in matriz:
        for columna in fila:
            j=eval(columna)
            a.append(j)
            j=0
        matriz_a.append(a)
        a=[]
    return matriz_a

def impresion(matriz):##Imprime la matriz por consola; fila x fila
    for fila in matriz:
        print(fila)

def nextgen(matriz): ##Realiza la "evolucion" de la matriz
    fi=[]
    a=10
    matriz_a=[]
    filas=len(matriz)
    columnas=len(matriz[0])
    for f in range(0,filas):
        for c in range(0,columnas):
            a=0
            if(matriz[f][c]==0):  ##Celulas Muertas (0)
########################
                if(f==0):
                    if(c==0):  ##Columna Izq.
                        a=matriz[0][1]+matriz[1][0]+matriz[1][1]
                        if(a==3):
                            fi.append(1)
                        else:
                            fi.append(0)
                    elif(c==columnas-1): ##Columna Der.
                        a=matriz[0][columnas-2]+matriz[1][columnas-2]+matriz[1][columnas-1]
                        if(a==3):
                            fi.append(1)
                        else:
                            fi.append(0)
                    else: ##Demas Columnas
                        a=matriz[f][c-1]+matriz[f][c+1]+matriz[f+1][c-1]+matriz[f+1][c]+matriz[f+1][c+1]
                        if(a==3):
                            fi.append(1)
                        else:
                            fi.append(0)
#################################
                elif(f==filas-1): ##Fila Inferior (Los demas if son mismo concepto del de arriba)
                    if(c==0):
                        a=matriz[filas-1][1]+matriz[filas-2][0]+matriz[filas-2][1]
                        if(a==3):
                            fi.append(1)
                        else:
                            fi.append(0)
                    elif(c==columnas-1):
                        a=matriz[filas-1][columnas-2]+matriz[filas-2][columnas-2]+matriz[filas-2][columnas-1]
                        if(a==3):
                            fi.append(1)
                        else:
                            fi.append(0)
                    else:
                        a=matriz[f][c-1]+matriz[f][c+1]+matriz[f-1][c-1]+matriz[f-1][c]+matriz[f-1][c+1]
                        if(a==3):
                            fi.append(1)
                        else:
                            fi.append(0) 
#####################
                else:  ##Todas las demas celdas que no son orilla
                    if(c==0):
                        a=matriz[f-1][c]+matriz[f+1][c]+matriz[f-1][c+1]+matriz[f][c+1]+matriz[f+1][c+1]
                        if(a==3):
                            fi.append(1)
                        else:
                            fi.append(0)
                    elif(c==columnas-1):
                        a=matriz[f-1][c]+matriz[f+1][c]+matriz[f-1][c-1]+matriz[f][c-1]+matriz[f+1][c-1]
                        if(a==3):
                            fi.append(1)
                        else:
                            fi.append(0)
                    else:
                        a=matriz[f-1][c-1]+matriz[f-1][c]+matriz[f-1][c+1]+matriz[f+1][c-1]+matriz[f+1][c]+matriz[f+1][c+1]+matriz[f][c-1]+matriz[f][c+1]
                        if(a==3):
                            fi.append(1)
                        else:
                            fi.append(0)
################################################################################################################        
            else: ##Celulas Vivas (1); sigue el mismo patro que la parte de las celulas muertas
                if(f==0):
                    if(c==0):
                        a=matriz[0][1]+matriz[1][0]+matriz[1][1]
                        if(a==2 or a==3):
                            fi.append(1)
                        elif(a<2 or a>3):
                            fi.append(0)
                    elif(c==columnas-1):
                        a=matriz[0][columnas-2]+matriz[1][columnas-2]+matriz[1][columnas-1]
                        if(a==2 or a==3):
                            fi.append(1)
                        else:
                            fi.append(0)
                    else:
                        a=matriz[f][c-1]+matriz[f][c+1]+matriz[f+1][c-1]+matriz[f+1][c]+matriz[f+1][c+1]
                        if(a==2 or a==3):
                            fi.append(1)
                        else:
                            fi.append(0)
#################################
                elif(f==filas-1):
                    if(c==0):
                        a=matriz[filas-1][1]+matriz[filas-2][0]+matriz[filas-2][1]
                        if(a==2 or a==3):
                            fi.append(1)
                        else:
                            fi.append(0)
                    elif(c==columnas-1):
                        a=matriz[filas-1][columnas-2]+matriz[filas-2][columnas-2]+matriz[filas-2][columnas-1]
                        if(a==2 or a==3):
                            fi.append(1)
                        else:
                            fi.append(0)
                    else:
                        a=matriz[f][c-1]+matriz[f][c+1]+matriz[f-1][c-1]+matriz[f-1][c]+matriz[f-1][c+1]
                        if(a==2 or a==3):
                            fi.append(1)
                        else:
                            fi.append(0) 
#####################
                else:
                    if(c==0):
                        a=matriz[f-1][c]+matriz[f+1][c]+matriz[f-1][c+1]+matriz[f][c+1]+matriz[f+1][c+1]
                        if(a==2 or a==3):
                            fi.append(1)
                        else:
                            fi.append(0)
                    elif(c==columnas-1):
                        a=matriz[f-1][c]+matriz[f+1][c]+matriz[f-1][c-1]+matriz[f][c-1]+matriz[f+1][c-1]
                        if(a==2 or a==3):
                            fi.append(1)
                        else:
                            fi.append(0)
                    else:
                        a=matriz[f-1][c-1]+matriz[f-1][c]+matriz[f-1][c+1]+matriz[f+1][c-1]+matriz[f+1][c]+matriz[f+1][c+1]+matriz[f][c-1]+matriz[f][c+1]
                        if(a==2 or a==3):
                            fi.append(1)
                        else:
                            fi.append(0)
        matriz_a.append(fi)
        fi=[]
    return matriz_a

def evo(matrizo, matrizn): ##Verifica si la matriz "evolucionara" o no; es para detener el ciclo while de maner natural
    a=0
    filas=len(matriz)
    columnas=len(matriz[0])
    for f in range(0,filas):
        for c in range(0,columnas):
            if(matrizo[f][c]!=matrizn[f][c]):
                a+=1
            else:
                a=a
    if(a>0):
        return True
    else:
        return False
###########################################################  Main  ##########################################################
file1=open("matrizinicial.txt", "r") ##Inicia Lectura Matrizinicial.txt
matriz=[]
lineas=file1.readlines()
c=1

for linea in lineas:
    a=linea.split(',')
    if(a[0]!=';\n'):
        matriz.append(a)

file1.close() ##Termina Lectura Matrizinicial.txt
matriz=transtoint(matriz)
print("Generacion ",c)
c+=1
impresion(matriz)
os.system ("cls") ##Limpia consola
p=input()
matriz_aux=matriz
matriz=nextgen(matriz)
evolution=evo(matriz,matriz_aux)

while(evolution): ##Proceso de evolucion continua
    print("Generacion ",c)
    c+=1
    impresion(matriz)
    os.system ("cls")
    matriz_aux=matriz
    matriz=nextgen(matriz)
    evolution=evo(matriz,matriz_aux)
    if(evolution==True):
        print("En caso de celula estable, ingrese el numero 2, en caso contrario, solo presione enter.")
    p=input()
    if(p=='2'): ##Es para que, si sale una celula estable (una que siempre existira, nunca morira), se puda terminar el ciclo
        evolution=False

file2=open("Matrizfinal.txt", "w+") ##Inicia Creacion y escritura Matrizfinal.txt
for fila in matriz_aux:
    for columna in fila:
        file2.write(str(columna)+",")
    file2.write("\n")
file2.close() ##Termina escritura Matrizfinal.txt

file3=open("Estadisticas.csv","w+") ##Inicia Creacion y escritura estadisticas.csv
file3.write(str(len(matriz[0]))+","+str(len(matriz))+","+str(c-2)) ##Columnas,filas,N° de pasos
file3.close() ##Termina Escritura estadisticas.csv

print("Archivos Creados Exitosamente")


    
