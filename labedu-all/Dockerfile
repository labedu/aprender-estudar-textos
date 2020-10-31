FROM python:3.8
WORKDIR /app
COPY ./requirements.txt .
RUN pip install -r requirements.txt
RUN python -m spacy download pt_core_news_md
RUN pip install --upgrade 'sentry-sdk[flask]'
COPY . .

CMD exec gunicorn --bind :5000 --workers 1 --threads 8 --log-level debug flask_app:app
