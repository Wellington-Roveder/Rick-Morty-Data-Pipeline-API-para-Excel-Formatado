from api.client import APIClient

api = APIClient("https://rickandmortyapi.com/api")

def traduz_status(s):
    return {"Alive": "Vivo", "Dead": "Morto", "unknown": "Desconhecido"}.get(s, s)

def traduz_genero(g):
    if not g: return "Desconhecido"
    return {"male": "Masculino", "female": "Feminino", "genderless": "Sem gênero"}.get(g.lower(), "Desconhecido")

def traduz_especie(s):
    return {"Human": "Humano", "Alien": "Alienígena"}.get(s, s)

def tratar_linha(dados):
    origin = dados.get("origin", {})
    location = dados.get("location", {})
    return {
        "id": dados.get("id"),
        "nome": dados.get("name"),
        "status": traduz_status(dados.get("status")),
        "especie": traduz_especie(dados.get("species")),
        "genero": traduz_genero(dados.get("gender")),
        "origem": traduz_status(origin.get("name")),
        "localizacao": location.get("name"),
        "episodios": len(dados.get("episode", []))
    }

def buscar_personagens(ids):
    dados = api.get(f"character/{','.join(map(str, ids))}")
    if not dados: return []
    return [tratar_linha(p) for p in dados] if isinstance(dados, list) else [tratar_linha(dados)]