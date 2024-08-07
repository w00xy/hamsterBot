FROM python:3.12

WORKDIR /bot
COPY req.txt req.txt
RUN pip3 install -r req.txt
RUN chmod 755 .
COPY .. .
