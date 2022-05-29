import utilidades as util
from datetime import datetime
from time import sleep

lista_usuarios = []
lista_citas = []
menu = 0

while (menu != 5):
  print("\033[1;33m"+ """
----------------------------------------------------------------------
           Bienvenido al sistema de agendamiento de citas
----------------------------------------------------------------------
        1. Registrar persona
        2. Visualizar listado de las personas
        3. Asignar una cita
        4. Cargar archivo
        5. Busqueda
        6. Salir de la aplicación
  """"\033[0;m")
  
  menu = util.convertir_entero(input("Seleccione una opción: "))
  
  util.clear()

  if (menu == 1):
    #Capturar los datos validados con diccionario
    dicc_datos = {"tipo_documento":"", "numero_documento":"", "nombre":"", "apellido":"", "fecha_nacimiento":"", "rh_grupo":"", "email":"", "telefono":"", "cita":"Sin cita"}
	  
    validar_tipo_documento = False
    while (validar_tipo_documento == False):
      tipo = input("Ingrese el tipo de documento, solo se acepta: CC, CE, TI, PA: ").upper()
      validar_tipo_documento = util.validar_tipo_documento(tipo)
  
    validar_documento = False
    while ( validar_documento == False):
      documento = input("Ingrese el número de documento: ")
      validar_documento = util.validar_numero_documento(documento)    
      usuario_existe = util.buscar_documento(tipo, documento, lista_usuarios )
      if usuario_existe == True:
          print("El documento que digito ya existe existe")
          validar_documento = False
    
    validar_nombre = False
    while ( validar_nombre == False):
      nombre = input("Ingrese su nombre: ")
      validar_nombre = util.validar_nombre(nombre)
    
    validar_apellido = False
    while ( validar_apellido == False):
      apellido = input("Ingrese su apellido: ")
      validar_apellido = util.validar_nombre(apellido)
    
    validar_fecha = False
    while (validar_fecha == False):
      fecha_temp = input("Ingrese la fecha de nacimiento: con el formato AAAA-MM-DD: ")
      validar_fecha = util.validar_fecha(fecha_temp, '%Y-%m-%d')
    
    validar_rh = False
    while ( validar_rh == False):
      rh = input("Ingrese el grupo sanguineo, primer carácter solo permite O, A, B, el segundo carácter solo permite (+) o (-) : ").upper()
      validar_rh = util.validar_rh(rh)
    
    validar_correo = False
    while ( validar_correo == False):
      correo = input("Ingrese el correo electrónico: ").lower()
      validar_correo = util.validar_correo(correo)

    validar_telefono = False
    while( validar_telefono == False):
      telefono = input("Ingrese el número telefónico: ")
      validar_telefono = util.validar_telefono(telefono)
    
    #Creación de diccionario de registro    
    dicc_datos["tipo_documento"] = tipo
    dicc_datos["numero_documento"] = documento
    dicc_datos["nombre"] = nombre
    dicc_datos["apellido"] = apellido
    dicc_datos["fecha_nacimiento"] = fecha_temp
    dicc_datos["rh_grupo"] = rh
    dicc_datos["email"] = correo
    dicc_datos["telefono"] = telefono

    #Agregar a las lista de usuarios
    lista_usuarios.append(dicc_datos)
    archivo = open(file='pacientes.txt',mode='a',encoding="utf_8")
    archivo.write(f"{dicc_datos}\n")
    archivo.close()

    print("\nUsuario registrado con exito")
    
  elif (menu == 2):
    print("\033[1;33m"+"""
----------------------------------------------------------------------
                  Visualización listado de personas:
----------------------------------------------------------------------
""" "\033[1;33m")
    titulo = f"Posicion \tTipo documento \t\t Número documento \t\t Nombres y apellidos \t\t Edad \t\t Fecha/hora Cita"
    print(titulo)
    
    for posicion, usuario in enumerate(lista_usuarios):
      #Calcular edad
      fecha_nacimiento = datetime.strptime(usuario['fecha_nacimiento'],'%Y-%m-%d')
      edad = datetime.now().year - fecha_nacimiento.year
      
      #Buscar si tiene citas asociadas
      fecha_cita = ""
      for cita in lista_citas:
        if cita[0] == usuario['numero_documento']:
          fecha_cita = cita[1]

      registro = f"{posicion+1} \t{usuario['tipo_documento']} \t\t {usuario['numero_documento']} \t\t {usuario['nombre']} {usuario['apellido']} \t\t {edad} años \t\t {fecha_cita}"
      print(registro)

      input("\nOprima tecla enter para continuar...")

  elif (menu == 3):

    validar_tipo_documento = False
    while (validar_tipo_documento == False):
      tipo = input("Ingrese el tipo de documento, solo se acepta: CC, CE, TI, PA: ").upper()
      validar_tipo_documento = util.validar_tipo_documento(tipo)
  
    validar_documento = False
    while ( validar_documento == False):
      documento = input("Ingrese el número de documento: ")
      validar_documento = util.validar_numero_documento(documento)    
    
    #Buscar el usuario
    usuario_existe = util.buscar_documento(tipo, documento, lista_usuarios )
    if usuario_existe == True:
      validar_fecha = False
      while (validar_fecha == False):
        fecha_temp = input("Ingrese la fecha/hora de la cita: con el formato AAAA-MM-DD HH:MM :")
        validar_fecha = util.validar_fecha(fecha_temp, '%Y-%m-%d %H:%M')      
        #Validar fecha de cita
        if validar_fecha :
          if datetime.strptime(fecha_temp, '%Y-%m-%d %H:%M') <= datetime.now():
            print("No es posible asignar la cita en la fecha indicada")
            validar_fecha = False
          else:
            validar_fecha = True
      
      fecha_cita = datetime.strptime(fecha_temp, '%Y-%m-%d %H:%M')
      tupla_cita = (tipo, documento, fecha_temp)
      lista_citas.append(tupla_cita)
      
      #agregamos la cita al archivo citas
      lista_citas.append(dicc_datos)
      archivo = open(file='citas.txt',mode='a',encoding="utf_8")
      archivo.write(f"{lista_citas}\n")
      archivo.close()
      

      # Buscar usuario para extraer datos
      usuario = util.buscar_usuario(tipo, documento, lista_usuarios)
      print("\nEstimado {0} {1} su cita fue asignada correctamente para el día, {2}, a las {3} horas.".format(usuario["nombre"], usuario["apellido"], fecha_cita.strftime("%Y-%m-%d"), fecha_cita.strftime("%H:%M")))
    else:
      print("El usuario no esta registrado...")
  elif (menu ==4):
      
        print("\033[1;33m"+"""
----------------------------------------------------------------------
                  Cargar archivos a listas
----------------------------------------------------------------------
""" "\033[0;m")

        archivo_paciente = open('pacientes.txt','r',encoding="utf-8") 
        archivo_cita = open('citas.txt','r',encoding="utf-8")
        print("1." "\033[1;33m"+ "Cargar el archivo pacientes a la lista pacientes"+ "\033[0;m")
        print("2." "\033[1;33m"+ "Cargar el archivo citas a la lista de citas"+ "\033[0;m")
        opcion = int(input("Ingrese una opcion: "))
        
        if opcion == 1:
            for linea in archivo_paciente:
                diccionario = linea.rstrip("\n")
                diccionario = eval(diccionario)
                lista_usuarios.append(diccionario)
            print(lista_usuarios)
        elif opcion == 2:
            for linea in archivo_cita:
                diccionario = linea.rstrip("\n")
                diccionario = eval(diccionario)
                lista_citas.append(diccionario)
            print(lista_citas)
            
        input("\nOprima tecla enter para continuar...")
  elif (menu == 5):
        print("\033[1;33m"+"""
----------------------------------------------------------------------
                    Busquedas por filtros:
----------------------------------------------------------------------

""" "\033[0;m")
        print("1." "\033[1;33m"+ "Buscar por Tipo de documento"+ "\033[0;m")
        print("2." "\033[1;33m"+ "Buscar por numero de documento"+ "\033[0;m")
        print("3." "\033[1;33m"+ "Buscar por nombre"+ "\033[0;m")
        print("4." "\033[1;33m"+ "Buscar por apellido"+ "\033[0;m")
        print("5." "\033[1;33m"+ "Buscar por correo electronico"+ "\033[0;m")
        print("6." "\033[1;33m"+ "Buscar por telefono"+ "\033[0;m")
        print("7." "\033[1;33m"+ "Buscar por telefono"+ "\033[0;m")
        opcion = int(input("Ingrese una opcion: "))
        
        if opcion == 1:
            tipo= input('Ingrese el tipo de documento, solo se acepta: CC, CE, TI, PA: ')
            print(list(filter(lambda item: item['tipo_documento'] == tipo, lista_usuarios)))
        elif opcion == 2:
            documento= input('Ingrese el numero de documento: ')
            print(list(filter(lambda item: item['numero_documento'] == documento, lista_usuarios)))
        elif opcion == 3:
            nombre= input('Ingrese el nombre: ')
            print(list(filter(lambda item: item['nombre'] == nombre, lista_usuarios)))
        elif opcion == 4:
            apellido= input('Ingrese el apellido: ')
            print(list(filter(lambda item: item['apellido'] == apellido, lista_usuarios)))
        elif opcion == 5:
            email= input('Ingrese el correo electronico: ')
            print(list(filter(lambda item: item['email'] == email, lista_usuarios)))
        elif opcion == 6:
            telefono= input('Ingrese el telefono: ')
            print(list(filter(lambda item: item['telefono'] == telefono, lista_usuarios)))  
        elif opcion == 7:
            rh= input('Ingrese el tipo de rh: ')
            print(list(filter(lambda item: item['rh_grupo'] == rh, lista_usuarios)))
        else:
            print("fuera de los parametros de busqueda establecidos")    
                   
        input("\nOprima tecla enter para continuar...")      
  elif (menu == 6):
    print("Saliendo de la aplicación")
    break
  else:
    print("Opción no válida")
  
  sleep(2)
  util.clear()