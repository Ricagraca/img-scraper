FROM selenium/standalone-firefox

USER root

# # Update before starting
RUN apt-get update -y

# # We need wget to set up the PPA and xvfb to have a virtual screen and unzip to install the Chromedriver
# RUN apt-get install -y wget xvfb unzip

# RUN wget https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb
# RUN apt install -y ./google-chrome-stable_current_amd64.deb

WORKDIR /app

RUN apt-get install -y python3 pip

COPY . .
RUN pip3 install -r requirements.txt

CMD [ "python3", "src/__main__.py"]