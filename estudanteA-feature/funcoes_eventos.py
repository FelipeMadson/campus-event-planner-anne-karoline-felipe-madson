# Função construtora de evento
def evento(id, nome, data, local, categoria, participado):
    return {
        "id": id,
        "nome": nome,
        "data": data,
        "local": local,
        "categoria": categoria,
        "participado": participado,
    }


# Lista global para armazenar eventos
eventos = []

# Cria um novo evento (dicionário) e adiciona à lista `eventos`. Retorna o evento criado.


def criar_evento(id, nome, data, local, categoria, participado):
    novo_evento = evento(id, nome, data, local, categoria, participado)
    eventos.append(novo_evento)
    return novo_evento


# b = criar_evento(1, "jose", "aaaa", "ali", "lá", True)
# print(b)

# Lista os eventos já criados
# eventos_criado = [b]

"""def listar_eventos():
    for novo_evento in b:
        print(eventos) """


def listar_eventos():
    for evento_item in eventos:
        print(evento_item)


# a = listar_eventos()
# print(a)

# Função pra procurar evento por nome


def buscar_nome_evento(nome, substring=False):
    nome_processado = nome.lower().strip
    if substring:
        resultados = list(
            filter(lambda e: nome_processado in e["nome"].lower(), eventos)
        )
    else:
        resultador = list(
            filter(lambda e: e["nome"].lower() == nome_processado, eventos)
        )
    return resultados


# Função para deletar evento por 'id'
# Vai remover o primeiro evento com id == id_evento da lista `eventos`.
# Retornando o dicionário do evento removido, ou None.


def deletar_evento(id_evento):
    for i, evento in enumerate(eventos):
        if evento.get("id") == id_evento:
            return eventos.pop(i)
    return None


# Função para validar data (não pode ser uma data anterior a hoje)
# Formato padrão: "%d/%m/%Y" (ex.: "20/12/2025").
def validar_data(data_str, formato="%d/%m/%Y", permitir_passado=True):

    from datetime import datetime, date  # Isso não deve dar problema.

    if not isinstance(data_str, str):
        return False

    try:
        dt = datetime.strptime(data_str, formato).date()
    except (ValueError, TypeError):
        return False

    if not permitir_passado and dt < date.today():
        return False

    return True
