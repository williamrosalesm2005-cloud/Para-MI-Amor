"""Servidor local para ver la página desde esta PC y la red Wi-Fi local."""
import os
import socket
from http.server import SimpleHTTPRequestHandler, ThreadingHTTPServer


def get_local_ip():
    """Devuelve la dirección de esta PC en la red local, si está disponible."""
    try:
        with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as connection:
            connection.connect(("8.8.8.8", 80))
            return connection.getsockname()[0]
    except OSError:
        return "IP-DE-ESTA-PC"


if __name__ == "__main__":
    port = int(os.environ.get("PORT", "8000"))
    address = ("0.0.0.0", port)
    print(f"En esta PC: http://127.0.0.1:{port}")
    print(f"En otra PC conectada al mismo Wi-Fi: http://{get_local_ip()}:{port}")
    ThreadingHTTPServer(address, SimpleHTTPRequestHandler).serve_forever()
