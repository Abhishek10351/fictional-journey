FROM python:3
COPY requirements.txt ./
RUN pip install --upgrade pip
RUN pip install -r requirements.txt
COPY . game/
WORKDIR /game
CMD python3 main.py