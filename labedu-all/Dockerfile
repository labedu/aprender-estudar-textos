FROM python:3.8
COPY . .
WORKDIR .
RUN pip install -r requirements.txt
RUN python -m spacy download pt_core_news_md
RUN pip install --upgrade 'sentry-sdk[flask]'

CMD exec gunicorn --bind :5000 --workers 1 --threads 8 flask_app:app
