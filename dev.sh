#!/bin/bash
imageName='scraper'

docker build -t $imageName .
docker run -it --rm -p 80:80 -v $(PWD):/usr/src/app --name scraperCtnr $imageName bash