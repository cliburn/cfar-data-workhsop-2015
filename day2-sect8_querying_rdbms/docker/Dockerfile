FROM phusion/baseimage:0.9.17
MAINTAINER Dan Leehr <dan.leehr@duke.edu>

RUN apt-get update && apt-get install -y \
  curl \
  unzip \
  ruby \
  postgresql-client

COPY load_data.sh /bin/
WORKDIR /tmp
CMD ["/bin/load_data.sh"]
