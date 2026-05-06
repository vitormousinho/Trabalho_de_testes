import time


def unique_int_id(prefix: int = 91) -> int:
    # API pública/compartilhada: timestamp reduz colisão de IDs entre execuções.
    return int(f"{prefix}{int(time.time() * 1000)}")

