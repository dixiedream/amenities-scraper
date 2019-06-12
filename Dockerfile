FROM python:3

WORKDIR /usr/src/app

RUN echo "deb  http://deb.debian.org/debian stretch main contrib non-free" >> /etc/apt/sources.list
RUN echo "deb-src  http://deb.debian.org/debian stretch main contrib non-free" >> /etc/sources.list

RUN apt update && apt install -y chromium chromedriver

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

COPY scrape.py ./
#COPY chromedriver /usr/bin/

#RUN chmod a+x /usr/bin/chromedriver

CMD [ "python", "./scrape.py" ]