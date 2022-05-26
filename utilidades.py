import re
from datetime import datetime as dt

def longitud_caracteres(documento:str, longitud_max:int, longitud_min:int = 1):
    """Función que tiene como objetivo el validar los caracteres en la totalidad de su longitud
        de acuerdo al numero de caracteres valido ingresado para la funcion.

    Args:
        documento (str): numero de documento
        longitud (int): tamaño de caracteres permitidos a validar

    Returns:
        bool: retorna True en caso de cumplir la validacion False en caso contrario
    """
    if documento.__len__() <= longitud_max and documento.__len__() >= longitud_min:
        return True
    else:
        return False

def buscar_simbolo(texto:str, simbolo:str):
    """funcion encargada de buscar un simbolo y compararlo con el texto

    Args:
        texto (str): _description_
        simbolo (str): _description_

    Returns:
        bool: retorna True en caso de cumplir la validacion False en caso contrario
    """
    if re.search(rf'(.)\{simbolo}', texto):
        return True
    else:
        return False

def tipo_doc(documento:str):
    """Esta función tiene como objetivo el validar el tipo de documento CC, TI, PA

    Args:
        documento (str): tipo de documento ingresado a la función

    Returns:
        bool: retorna True en caso de cumplir la validacion False en caso contrario
    """
    
    if documento == 'CC' or documento == 'TI' or documento == 'PA':
        return True
    else:
        return False

def validar_numero_doc(documento:str):
    if bool(re.search(r'\D', documento)) == False:
        return True
    else:
        return False

def validar_correo(correo:str):
    """Funcion que nos permite validar el correo analizando analizando correo electronico
        dominio.

    Args:
        correo (string): _description_

    Returns:
        bool: retorna True en caso de cumplir la validacion False en caso contrario
    """
    expresion = r'^(\w|\.|\_|\-)+[@](\w|\_|\-|\.)+[.]\w{2,3}$'
    if validar_longitud_caracteres(correo,30,6) and re.search(expresion,correo):
        return True
    else:
        return False

def validar_rh(rh:str):
    """Funcion que permite valiadar las primres posiciones del RH y grupo sanguineo


    Args:
        rh (str): rh y grupo sanguineo (O+)

    Returns:
        _type_: _description_
    """

    if validar_longitud_caracteres(rh, 2):
        if rh[0] == 'O' or rh[0] == 'A' or rh[0]=='B' :
            if buscar_simbolo(rh, '+') or buscar_simbolo(rh, '-'):
                return True
            else:
                return False
        else:
            return False
    else:
        return False




def registrar_cita():
    pass

def cargar_archivos():
    pass

def buscar():
    pass

def salir():
    print("salir")


def menu():
    op = 0

    while op != 5:

        print("1. Registrar paciente")
        print("2. Registrar cita")
        print("3. Cargar Archivos")
        print("4. Busqueda por filtro")
        print("5. Salir del programa")
        op = int(input("digite su opcion: "))

        if op == 1:
            print('\n\n****************************************************************************')
            print('****************************************************************************')
            print('                           FORMULARIO DE REGISTRO                              ')
            print('- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - \n')

            tipo_documento = input("Ingrese el tipo de documento (CC, TI, PA): ").upper()

            if tipo_documento(tipo_documento):
                pass
                
            
        elif op == 2:
            registrar_cita()
        elif op == 3:
            cargar_archivos()
        elif op == 4:
            buscar()
        elif op == 5:
            salir()