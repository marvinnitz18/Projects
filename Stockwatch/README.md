# You have to install the following python modules:

import requests
colorama

# Which you can install with these commands:

'python -m install requests'
'python -m install colorama'


# Next

## place the Stocks you want to watch into the file "stocks.txt" like this:

### stocks.txt example
FB,GOOGL,


***
## or if you have only one stock to watch it needs to have a trailing comma:
***

### stocks.txt example
FB,


# Your Api Key must be placed inside the file api.key

## api.key example
86ad4wa56d41w6a4d6wd1d1wa6

# Your folder architecture should look like this:

```
.
├── README.md
├── api.key
├── stocks.txt
└── Stockwatch.py
```
