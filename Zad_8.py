import requests
import argparse


class Brewery:
    def __init__(
        self,
        id,
        name,
        brewery_type,
        address_1,
        address_2,
        address_3,
        city,
        state_province,
        state,
        postal_code,
        country,
        longitude,
        latitude,
        phone,
        website_url,
    ):
        self.id = id
        self.name = name
        self.brewery_type = brewery_type
        self.address_1 = address_1
        self.address_2 = address_2
        self.address_3 = address_3
        self.city = city
        self.state_province = state_province
        self.state = state
        self.postal_code = postal_code
        self.country = country
        self.longitude = longitude
        self.latitude = latitude
        self.phone = phone
        self.website_url = website_url

    def __str__(self):
        return (
            f"{self.name} ({self.brewery_type}) - {self.city}, {self.state}, {self.country}"
        )


parser = argparse.ArgumentParser()
parser.add_argument("--city")
args = parser.parse_args()

base_url = "https://api.openbrewerydb.org/v1/breweries"

if args.city:
    url = f"{base_url}?per_page=20&by_city={args.city}"
else:
    url = f"{base_url}?per_page=20"

response = requests.get(url)
data = response.json()   # lista słowników z API [file:1]

breweries = []

for item in data:
    brewery = Brewery(
        item.get("id"),
        item.get("name"),
        item.get("brewery_type"),
        item.get("address_1"),
        item.get("address_2"),
        item.get("address_3"),
        item.get("city"),
        item.get("state_province"),
        item.get("state"),
        item.get("postal_code"),
        item.get("country"),
        item.get("longitude"),
        item.get("latitude"),
        item.get("phone"),
        item.get("website_url"),
    )
    breweries.append(brewery)

for b in breweries:
    print(b)