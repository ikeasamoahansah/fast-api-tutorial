FROM ubuntu:22.04

COPY requirements.txt ./

# RUN pip install requirements.txt

COPY . .

WORKDIR /sql_app

EXPOSE 8000

CMD [ "python3", "main.py" ]