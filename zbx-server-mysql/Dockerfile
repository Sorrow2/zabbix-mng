FROM zabbix/zabbix-server-mysql:ubuntu-4.4-latest
MAINTAINER pentinam

# Update
RUN apt-get update && apt-get install -y \
  curl \
  python-pip \
  nano \

# Install dependencies
RUN pip install \
  requests \
  sockets
  --upgrade pip
