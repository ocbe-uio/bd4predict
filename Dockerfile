FROM python:3.10-slim-buster

LABEL maintainer="Mauricio Moreira Soares <phydev@protonmail.ch>"

# creates /code if the folder does not exist and set as workdir
WORKDIR /code

# Set our app folder as a volume
VOLUME ["/code"]

# Install dependencies:
COPY requirements.txt .
RUN pip install --no-cache-dir --upgrade -r requirements.txt

EXPOSE 8000

COPY . .

CMD ["python3", "-m", "app.main"]
