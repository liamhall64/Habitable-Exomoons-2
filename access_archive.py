import requests 
import pandas as pd

url = "https://exoplanetarchive.ipac.caltech.edu/TAP/sync?query=select+*+from+pscomppars&format=csv"

archive = requests.get(url)
archive = pd.read_csv(url)
archive = archive.fillna(0) # Fill NaN values with 0

#print(archive)