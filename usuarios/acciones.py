import usuarios.usuario as modelo
import notas.acciones


class Acciones:

    def registro(self):
        print("\nOk¡¡ Vamos a registrarte en el sistema...")

        nombre = input("¿Cual es tu nombre?: ")
        apellido = input("¿Cuales son tus apellidos?: ")
        email = input("Introduce tu email: ")
        password = input("Introduce tu contraseña: ")

        usuario = modelo.Usuario(nombre, apellido, email, password)
        registro = usuario.registrar()

        if registro[0] >= 1:
            print(f"\nPerfecto {registro[1].nombre} te has registrado con el email {registro[1].email}")
        else:
            print("\nNo te has registrado correctamente!!!")

    def login(self):
        print("\nJoya¡¡ Identificate en el sistema...")
        try:
            email = input("Introduce tu email: ")
            password = input("Introduce tu contraseña: ")

            usuario = modelo.Usuario('','', email, password)
            login = usuario.identificar()

            if email == login[3]:
                print(f"\nBienvenido {login[1]}, te has registrado en el sistema el {login[5]}")
                self.proximasAcciones(login)

        except Exception as e:
            #print(type(e))
            #print(type(e).__name__)
            print(f"Login incorrecto!! Intentalo más tarde")

    def proximasAcciones(self, usuario):
        print("""
        Acciones disponibles:
        - Crear nota (crear)
        - Mostrar tus notas (mostrar)
        - Eliminar nota (eliminar)
        - Salir (salir)
        """)
        try:
                
            accion = input("¿Qué quieres ahacer?: ")
            hazEl = notas.acciones.Acciones()

            if accion == "crear":
                hazEl.crear(usuario)
                print("vamos a crear")
                self.proximasAcciones(usuario)

            elif accion == "mostrar":
                hazEl.mostrar(usuario)
                print("vamos a mostrar")
                self.proximasAcciones(usuario)

            elif accion == "eliminar":
                hazEl.borrar(usuario)
                self.proximasAcciones(usuario)

            elif accion == "salir":
                print(f"Ok {usuario[1]}, hasta pronto")
                exit()
        except Exception as e:
            print(type(e))
            print(type(e).__name__)
            print(f"no se pudo eliminar satifactoriamente")            
