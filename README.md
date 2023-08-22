# cbs_hist_downloader

A Python-based tool using Selenium to download books to your harddrive rather than accessing the pictures through the API at historisch.cbs.nl

## Dependencies

Selenium (`pip install selenium`), time, os, webdriver-manager (`pip install webdriver-manager`)

## Example how to use:

In the console:

```
pip install cbs_hist_downloader
```

After installation, in a python environment, you start off with the first URL of the book/volume you want to download:

```{python}
import cbs_hist_downloader as chd

url = "https://historisch.cbs.nl/detail.php?nav_id=2-1&index=10&id=395291474"

chd.scrape_book(url)
```

The files will be downloaded to your Downloads folder. 


## Suggestions / Comments

a dot h dot machielsen at uu dot nl
