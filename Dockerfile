# Use uma imagem oficial do Python como base
FROM python:3.8-slim-buster

# Define o diretório de trabalho no contêiner
WORKDIR /app

# Copia os arquivos de requisitos para o contêiner
COPY requirements.txt .

# Instala as dependências
RUN pip install --no-cache-dir -r requirements.txt

# Copia o código para o contêiner
COPY . .

# Expõe a porta que a aplicação vai rodar
EXPOSE 5000

# Comando para iniciar a aplicação
CMD ["python", "app.py"]
