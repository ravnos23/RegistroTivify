import requests
import random
import string
import time

# Listas ampliadas para mayor aleatoriedad
NOMBRES = [
    "Alejandro", "María", "David", "Lucía", "Javier", "Carmen", "Daniel", "Ana", "Carlos", "Laura", 
    "Antonio", "Rocío", "Manuel", "Marta", "José", "Elena", "Francisco", "Isabel", "Luis", "Paula", 
    "Miguel", "Sara", "Ángel", "Raquel", "Pedro", "Beatriz", "Jorge", "Nuria", "Fernando", "Eva", 
    "Pablo", "Sofía", "Rubén", "Alba", "Diego", "Clara", "Iván", "Marina", "Sergio", "Cristina", 
    "Raúl", "Andrea", "Adrián", "Julia", "Marcos", "Irene", "Víctor", "Silvia", "Mario", "Natalia"
]

APELLIDOS = [
    "García", "Rodríguez", "González", "Fernández", "López", "Martínez", "Sánchez", "Pérez", "Gómez", "Martín", 
    "Jiménez", "Ruiz", "Hernández", "Díaz", "Moreno", "Álvarez", "Muñoz", "Romero", "Alonso", "Gutiérrez", 
    "Navarro", "Torres", "Domínguez", "Vázquez", "Ramos", "Gil", "Ramírez", "Serrano", "Blanco", "Molina", 
    "Morales", "Suárez", "Ortega", "Delgado", "Castro", "Ortiz", "Rubio", "Marín", "Sanz", "Núñez", 
    "Iglesias", "Medina", "Garrido", "Cortes", "Castillo", "Santos", "Lozano", "Guerrero", "Cano", "Prieto"
]

# Códigos Postales variados de provincias españolas
CODIGOS_POSTALES = [
    "08001", "28001", "41001", "46001", "50001", "29001", "30001", "11001", "15001", "48001", 
    "25001", "17001", "43001", "33001", "35001", "38001", "10001", "18001", "20001", "21001", 
    "22001", "23001", "24001", "26001", "27001", "31001", "32001", "34001", "36001", "37001", 
    "39001", "40001", "42001", "44001", "45001", "47001", "49001", "01001", "02001", "03001", 
    "04001", "05001", "06001", "07001", "09001", "12001", "13001", "14001", "16001", "19001"
]

def generar_contrasena_segura():
    minusculas = ''.join(random.choices(string.ascii_lowercase, k=4))
    mayusculas = ''.join(random.choices(string.ascii_uppercase, k=3))
    numeros = ''.join(random.choices(string.digits, k=3))
    caracteres_mezclados = list(minusculas + mayusculas + numeros)
    random.shuffle(caracteres_mezclados)
    return ''.join(caracteres_mezclados) + "."

def obtener_dominio_mailtm():
    try:
        response = requests.get("https://api.mail.tm/domains", timeout=10)
        if response.status_code == 200:
            datos = response.json()
            activos = [d["domain"] for d in datos.get("hydra:member", []) if d.get("isActive")]
            return random.choice(activos) if activos else None
    except:
        return None

def generar_perfil():
    """Genera todos los datos necesarios para un registro."""
    dominio = obtener_dominio_mailtm()
    if not dominio:
        return None
    
    password = generar_contrasena_segura()
    usuario = f"tivify_{int(time.time())}_{random.randint(100,999)}"
    correo = f"{usuario}@{dominio}"
    
    # Registro en Mail.tm
    payload = {"address": correo, "password": password}
    registro = requests.post("https://api.mail.tm/accounts", json=payload, timeout=10)
    
    if registro.status_code == 201:
        # Obtener token
        login = requests.post("https://api.mail.tm/token", json=payload, timeout=10)
        token = login.json().get("token") if login.status_code == 200 else None
        
        return {
            "correo": correo,
            "password": password,
            "nombre": random.choice(NOMBRES),
            "apellidos": f"{random.choice(APELLIDOS)} {random.choice(APELLIDOS)}",
            "cp": random.choice(CODIGOS_POSTALES),
            "token": token
        }
    return None
  
