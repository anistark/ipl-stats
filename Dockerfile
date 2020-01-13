FROM python:3.7.1

LABEL Author="Kumar Anirudha"
LABEL E-mail="mail@anirudha.dev"
LABEL version="0.0.1"

ENV FLASK_APP "ipl/run.py"
ENV FLASK_ENV "production"
ENV FLASK_DEBUG True

RUN mkdir /app
WORKDIR /app

COPY Pip* /app/

RUN pip install --upgrade pip && \
    pip install pipenv && \
    pipenv install --dev --system --deploy --ignore-pipfile

ADD . /app

EXPOSE 8000

CMD flask run --host=0.0.0.0
