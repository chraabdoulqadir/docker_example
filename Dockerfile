FROM ubuntu:20.04

RUN apt update && apt install -y python python3-pip

RUN apt update

COPY requirements.txt /docker_example/requirements.txt
WORKDIR /docker_example
COPY . /docker_example
RUN pip3 install --no-cache-dir -r requirements.txt
ENV FLASK_APP="/docker_example/app.py"
EXPOSE 3000
CMD python3 ./app.py

