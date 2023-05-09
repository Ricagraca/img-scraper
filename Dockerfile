FROM selenium/standalone-firefox

USER root

RUN apt-get update -y
RUN apt-get install -y wget

RUN wget -q https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb
RUN apt-get install -y ./google-chrome-stable_current_amd64.deb

WORKDIR /app

RUN apt-get install -y python3 pip

COPY . .
RUN pip3 install -r requirements.txt

CMD [ "python3", "src/__main__.py"]