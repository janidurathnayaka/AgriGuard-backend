FROM python:3.14.0b3-alpine3.21
WORKDIR /app/
COPY . /app/
RUN pip install -r requiremnts.txt
EXPOSE 8000

CMD [ "fastapi","run" ]