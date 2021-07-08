## TODO
Simplify loop into one section to limit cpu time (for slower pcs)

# Liquipy.scrape

Reason0x6/Liquipy.scrape is licensed under the

## Mozilla Public License 2.0
Permissions of this weak copyleft license are conditioned on making available source code of licensed files and modifications of those files under the same license (or in certain cases, one of the GNU licenses). Copyright and license notices must be preserved. Contributors provide an express grant of patent rights. However, a larger work using the licensed work may be distributed under different terms and without source code for files added in the larger work.

A python based match data scraper for csgo liquipedia 

## Includes & imports
```
from os import close
import requests
import csv
import re
from bs4 import BeautifulSoup
import json
import ast
import os
import hashlib
```

## Outputs

2 files:
  - upcoming matches
  - completed matches
