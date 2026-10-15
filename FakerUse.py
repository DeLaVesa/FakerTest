# *****************************************************************************************
# DESARROLLO DE APLICACIONES EN LENGUAJE PYTHON - IES 'Muralla Romana'
# TAREA UD04: 
# ALUMNO: Marcos De Vega y De Vega
# *****************************************************************************************
# Editado y testado con: 
# MS Visual Studio Code v1.140
# Python v3.14.7 
# ==============================================================================
# Este programa simula un sistema para procesar las facturas mensuales
# Debe limpiar los datos corruptos, calcular los precios finales con descuentos, ordenar a los clientes por prioridad y,
# finalmente, enviar las notificaciones de cobro de forma recursiva

from faker import Faker
import random

def usuarios_ficticios(cantidad=15):
    # Inicializamos Faker configurado para locale 'es_ES' (España) para obter datos en castelán/galego
    # Se queres datos específicamente en galego, Faker non ten un locale 'gl_ES' oficial moi completo,
    # polo que 'es_ES' é a mellor opción para nomes e formatos cercanos.
    fake = Faker('es_ES')
    
    usuarios = {}

    print(f"--- Xerando {cantidad} usuarios ficticios ---\n")

    for i in range(1, cantidad + 1):
        # Xeramos os datos individuais
        nome = fake.name()
        direccion = fake.address().replace('\n', ', ')  # Unificamos a dirección nunha liña
        email = fake.email()
        telefono = fake.phone_number()

        # Creamos o dicionario para o usuario actual
        datos_usuario = {
            "nome": nome,
            "direccion": direccion,
            "correo": email,
            "telefono": telefono
        }

        # Gardamos no dicionario principal usando 'i' como clave (1 ao 15)
        usuarios[i] = datos_usuario

    return usuarios

def mostrar_usuarios(usuarios):
    print("LISTADO DE USUARIOS XERADOS:")
    print("-" * 60)
    # Iteramos sobre as claves (códigos) e valores (datos) do dicionario
    for codigo, datos in usuarios.items():
        print(f"Código {codigo}:")
        print(f"  Nome:     {datos['nome']}")
        print(f"  Dirección:{datos['direccion']}")
        print(f"  Email:    {datos['correo']}")
        print(f"  Teléfono: {datos['telefono']}")
        print("-" * 30)

def seleccionar_ganador(usuarios):
    # Seleccionamos unha clave aleatoria do dicionario (entre 1 e 15)
    codigo_ganador = random.choice(list(usuarios.keys()))
    nome_ganador = usuarios[codigo_ganador]['nome']
    
    print("\n" + "=" * 60)
    print(f"O usuario chamado {nome_ganador} foi o afortunado!")
    print("=" * 60)

# --- Execución do programa ---
if __name__ == "__main__":
    # 1. Xerar os datos
    base_de_datos_usuarios = usuarios_ficticios(15)
    
    # 2. Mostrar todos os usuarios
    mostrar_usuarios(base_de_datos_usuarios)
    
    # 3. Seleccionar e mostrar o gañador
    seleccionar_ganador(base_de_datos_usuarios)
