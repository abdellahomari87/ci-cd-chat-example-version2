# Utilise une image de base Python
FROM python:3.12-slim

# Définit le répertoire de travail
WORKDIR /app

# Copie les fichiers nécessaires dans l'image
COPY requirements.txt ./
COPY chat ./chat

# Installe les dépendances
RUN pip install --no-cache-dir -r requirements.txt

# Copie les tests
COPY chat/tests ./chat/tests

# Définit la commande à exécuter
CMD ["pytest", "--cov=chat", "--cov-fail-under=80", "chat/tests/"]
