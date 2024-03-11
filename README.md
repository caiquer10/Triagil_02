# Desafio Triagil: API PokeTeam

Esta é uma API REST simples baseada em Flask para gerenciar times de Pokémon. Ela permite aos usuários criar, visualizar e recuperar times de Pokémon.

## Instalação

1. Clone o repositório:

```
git clone https://github.com/your_username/PokeTeam-API.git
```

2. Instale as dependências necessárias:

```
pip install -r requirements.txt
```

3. Execute a aplicação Flask:

```
python app.py
```

## Uso

### Obter Todos os Times

```
GET /api/teams
```

Recupera todos os times de Pokémon.

### Obter Time por Usuário

```
GET /api/teams/<user>
```

Recupera o time de Pokémon de um usuário específico.

### Criar Time

```
POST /api/teams
```

Cria um novo time de Pokémon. Requer dados JSON no seguinte formato:

```json
{
    "user": "nome_do_usuario",
    "pokemons": ["pokemon1", "pokemon2", ...]
}
```

## Exemplo

Para criar um novo time de Pokémon para o usuário "ash", faça uma requisição POST para `/api/teams` com o seguinte payload JSON:

```json
{
    "user": "ash",
    "pokemons": ["pikachu", "charizard", "bulbasaur"]
}
```

## Dependências

- Flask
- Requests

## Créditos

Gostei de fazer parte do Desafio Triagil.
