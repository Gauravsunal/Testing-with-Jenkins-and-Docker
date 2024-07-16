FROM python:latest
LABEL Maintainer="gaurav"
WORKDIR /usr/app/src
COPY test.py ./
CMD [ "python", "./test.py"]
