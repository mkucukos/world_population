# Scrape data from HTML tables into a DataFrame using BeautifulSoup,
# Pandas and requests

import pandas as pd
import requests  # this module helps us to download a web page
from bs4 import BeautifulSoup  # this module helps in web scrapping.
#
# The below url contains html tables with data about world population.
url = "https://en.wikipedia.org/wiki/World_population"

# get the contents of the webpage in text format and store
# in a variable called data
data = requests.get(url).text

print(data)

soup = BeautifulSoup(data, "html.parser")

# find all html tables in the web page
# in html table is represented by the tag <table>
tables = soup.find_all('table')

# we can see how many tables were found by checking
# the length of the tables list
len(tables)

for index, table in enumerate(tables):
    if ("10 most densely populated countries" in str(table)):
        table_index = index
print(table_index)

print(tables[table_index].prettify())


# The <td> tag defines the standard cells in the table
# which are displayed as normal-weight, left-aligned text.
# The <tr> tag defines the table rows.
population_data = pd.DataFrame(
    columns=["Rank", "Country", "Population", "Area", "Density"])

for row in tables[table_index].tbody.find_all("tr"):
    col = row.find_all("td")
    if (col != []):
        rank = col[0].text
        country = col[1].text
        population = col[2].text.strip()
        area = col[3].text.strip()
        density = col[4].text.strip()
        population_data = population_data.append(
            {"Rank": rank, "Country": country, "Population": population,
             "Area": area, "Density": density}, ignore_index=True)

population_data
