FROM kalilinux/kali-rolling

WORKDIR /root/fakerapi

RUN apt update \
	&& apt install -y python3 python3-pip

COPY . .

RUN python3 setup.py install

ENTRYPOINT ["fake"]
CMD ["--help"]
