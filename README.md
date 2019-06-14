# Amenities scraper

Python utility for scraping amenities with the OpenStreetMap API

# Getting Started

### Choose what to scrape

Create your whatToScrape.yml file like the example and place the file in the config folder

### Prerequisites

Docker

### Install and usage

Run the script

```
sh ./setup.sh
```

or manually 

```
$ docker build -t amenitiesScraper .
$ docker run -it --rm --name scraper amenitiesScraper
```

Your results will be placed in the data folder

### Run in a test environment

```
sh ./dev.sh
```

## Authors

* **Alessandro Lucarini** - *Initial work* - [dixiedream](https://github.com/dixiedream)

## Reference

[OverPass-Turbo API](http://overpass-turbo.eu)