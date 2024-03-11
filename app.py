# Importando as bibliotecas necessárias
from flask import Flask, request, jsonify
import requests
import uuid

# Inicializando a aplicação Flask
app = Flask(__name__)

# Dicionário para armazenar os times de Pokémon
teams = {}

# Função para obter informações de um Pokémon específico da PokeAPI
def get_pokemon_info(pokemon):
    # Converte o nome do Pokémon para minúsculas
    pokemon = pokemon.lower()
    # URL da API do Pokémon
    url = f'https://pokeapi.co/api/v2/pokemon/{pokemon}'
    # Faz uma solicitação GET para a API
    response = requests.get(url)

    # Verifica se a resposta foi bem-sucedida
    if response.status_code == 200 and response.text.strip():
        # Converte a resposta em JSON
        data = response.json()
        # Retorna um dicionário com as informações do Pokémon
        return {
            'id': data["id"],
            'name': data["name"],
            'weight': data["weight"],
            'height': data["height"]
        }
    else:
        # Se a resposta não foi bem-sucedida, retorna None
        return None

# Rota para obter todos os times de Pokémon
@app.route('/api/teams', methods=['GET'])
def get_teams():
    # Retorna um JSON com todos os times
    return jsonify(teams)

# Rota para obter um time de Pokémon específico de um usuário
@app.route('/api/teams/<user>', methods=['GET'])
def get_team(user):
    # Verifica se o usuário tem um time
    if user in teams:
        # Retorna o time do usuário
        return jsonify(teams[user])
    else:
        # Se o usuário não tem um time, retorna um erro
        return jsonify({'error': 'Time não encontrado'}), 404

# Rota para criar um novo time de Pokémon
@app.route('/api/teams', methods=['POST'])
def create_team():
    # Obtém os dados enviados na solicitação
    data = request.get_json()

    team = []
    # Para cada Pokémon na lista de Pokémons enviada
    for pokemon in data['pokemons']:
        # Obtém as informações do Pokémon
        pokemon_info = get_pokemon_info(pokemon)
        # Se as informações do Pokémon não foram encontradas, retorna um erro
        if pokemon_info is None:
            return jsonify({'error': f'Pokémon {pokemon} não encontrado'}), 400
        # Adiciona as informações do Pokémon ao time
        team.append(pokemon_info)

    # Gera um ID único para o time
    team_id = str(uuid.uuid4())
    # Adiciona o time ao dicionário de times
    teams[data['user']] = {
        'owner': data['user'],
        'id': team_id,
        'pokemons': team
    }

    # Retorna uma mensagem de sucesso e o ID do time
    return jsonify({'message': 'Time criado com sucesso', 'id': team_id}), 201

# Inicia a aplicação Flask
if __name__ == '__main__':
    app.run(debug=True)
