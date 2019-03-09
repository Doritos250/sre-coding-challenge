FROM python:3

MAINTAINER theophileds@gmail.com

WORKDIR /app

COPY . .

RUN pip install -r requirements.txt

ENTRYPOINT ["python", "manage.py"]

CMD ["runserver"]