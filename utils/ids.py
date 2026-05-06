import time


def unique_int_id(prefix: int = 91) -> int:
    """
    Gera um inteiro pseudo-único (ex.: 91 + timestamp).

    A Petstore não garante isolamento de dados entre execuções/usuários,
    então evitamos colisões usando tempo em milissegundos.
    """
    return int(f"{prefix}{int(time.time() * 1000)}")

