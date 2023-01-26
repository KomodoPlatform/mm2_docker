FROM ubuntu:latest
RUN apt update
RUN apt install python3 python3-venv python3-pip openssl ca-certificates python3-dev wget python3-setuptools bash curl jq unzip python3-dotenv -y

WORKDIR /mm2_api
COPY . /mm2_api/
RUN python3 -m venv /mm2_api
RUN pip3 install -r requirements.txt

ENV userpass=${userpass}
ENV PATH=/app:/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin
CMD ./init.sh