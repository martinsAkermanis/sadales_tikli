FROM python:3.6

COPY . /app

EXPOSE 5000

WORKDIR /app

RUN pip install -r requirements.txt
RUN sleep 15

CMD python app.py
