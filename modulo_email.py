import requests
import re
import time

def confirmar_registro(token_acceso, max_segundos=240):
    """
    Escucha la bandeja de entrada durante 4 minutos (240s).
    Muestra un contador en pantalla al usuario.
    """
    headers = {
        "Authorization": f"Bearer {token_acceso}",
        "Accept": "application/json"
    }

    inicio_tiempo = time.time()
    print(f"[*] Iniciando escucha. Tiempo máximo: {max_segundos // 60} minutos.")
    
    while (time.time() - inicio_tiempo) < max_segundos:
        # Calcular tiempo restante para el contador
        restante = int(max_segundos - (time.time() - inicio_tiempo))
        minutos = restante // 60
        segundos = restante % 60
        
        # El \r hace que se sobrescriba la misma línea cada vez
        print(f"\r[*] Esperando confirmación... {minutos:02d}:{segundos:02d} restantes", end="", flush=True)

        try:
            response = requests.get("https://api.mail.tm/messages", headers=headers, timeout=5)
            
            if response.status_code == 200:
                datos = response.json()
                lista_correos = datos if isinstance(datos, list) else datos.get("hydra:member", [])

                for correo in lista_correos:
                    asunto = correo.get("subject", "").lower()
                    if "tivify" in asunto:
                        msg_id = correo.get("id")
                        res_msg = requests.get(f"https://api.mail.tm/messages/{msg_id}", headers=headers, timeout=5)
                        
                        if res_msg.status_code == 200:
                            cuerpo = res_msg.json().get("text") or res_msg.json().get("html") or ""
                            patron_url = r'(https?://[^\s<>"]+|www\.[^\s<>"]+)'
                            enlaces = re.findall(patron_url, cuerpo)
                            
                            for link in enlaces:
                                if "tivify" in link and ("confirm" in link or "verify" in link):
                                    print(f"\n[!] ¡Link encontrado! Visitando: {link}")
                                    requests.get(link, timeout=15)
                                    print("✅ ¡Cuenta confirmada correctamente!")
                                    return True
            
            time.sleep(10) # Espera 10 segundos antes de volver a consultar
            
        except Exception as e:
            # Si falla la red momentáneamente, no paramos, solo seguimos contando
            continue
            
    print("\n[!] ERROR: Tiempo agotado. No se recibió el correo de confirmación.")
    return False
