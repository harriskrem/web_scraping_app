# Web Scraping App

Web Scraping nine random vessels from MarineTraffic to a json file. Works only on Chrome browser. The app may break if you have slow internet connection.

## Requirements
- Python <= ***3.9.13***
- A MarineTraffic account

## Installation

```bash
pip install selenium # or py -m pip install selenium
pip install undetected_chromedriver # or py -m pip install undetected_chromedriver
```

## Usage
In the main.py file fill the two variables:
```python
EMAIL = "" # YOUR EMAIL HERE
PASSWORD = "" # YOUR PASSWORD HERE
```

In your terminal:
```bash
python ./main.py
```
or
```bash
py ./main.py
```
