FROM python:3

WORKDIR /usr/src/app

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

COPY config ./config
COPY scrape.py ./

CMD [ "python", "./scrape.py" ]