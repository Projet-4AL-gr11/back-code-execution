FROM alpine
ENV PYTHONUNBUFFERED=1

COPY sandbox.py /sandbox.py
WORKDIR .
RUN apk add --update --no-cache python3 && ln -sf python3 /usr/bin/python
RUN python3 -m ensurepip
RUN pip3 install --no-cache --upgrade pip setuptools
RUN apk add --update nodejs
ENTRYPOINT ["python", "sandbox.py"]