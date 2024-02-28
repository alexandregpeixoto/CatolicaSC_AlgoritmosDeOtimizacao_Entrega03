import redis

# Conectar ao servidor Redis (certifique-se de ter um servidor Redis em execução)
redis_client = redis.StrictRedis(host='localhost', port=6379, db=0)

def calcular_fatorial(n):
    # Verificar se o resultado está no cache
    cache_key = f'fatorial:{n}'
    cached_result = redis_client.get(cache_key)

    if cached_result is not None:
        # Se estiver no cache, retornar o resultado
        return int(cached_result)

    # Se não estiver no cache, calcular o fatorial
    resultado = fatorial(n)

    # Armazenar o resultado no cache
    redis_client.set(cache_key, resultado)

    return resultado

def fatorial(n):
    # Função recursiva para calcular o fatorial
    if n == 0 or n == 1:
        return 1
    else:
        return n * fatorial(n - 1)

# Solicitar ao usuário o número para calcular o fatorial
numero = int(input("Digite um número para calcular o fatorial: "))

# Calcular e exibir o resultado
resultado = calcular_fatorial(numero)
print(f'O fatorial de {numero} é: {resultado}')