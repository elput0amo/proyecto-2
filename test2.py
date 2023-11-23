import socket

def obtener_ip():
    try:
        # Obtener el nombre del host
        host_name = socket.gethostname()
        # Obtener la dirección IP del host
        host_ip = socket.gethostbyname(host_name)
        return host_ip
    except socket.error as e:
        print(f"No se pudo obtener la dirección IP: {e}")
        return None
    
ip=obtener_ip()
print(ip)
