import folium

# Create a map centered on Europe
m = folium.Map(location=[52.52, 13.41], zoom_start=5)

# Define a dictionary of European capitals
capitals = {
    'Albania': 'Tirana',
    'Austria': 'Vienna',
    'Belarus': 'Minsk',
    'Belgium': 'Brussels',
    'Bosnia and Herzegovina': 'Sarajevo',
    'Bulgaria': 'Sofia',
    'Croatia': 'Zagreb',
    'Cyprus': 'Nicosia',
    'Czech Republic': 'Prague',
    'Denmark': 'Copenhagen',
    'Estonia': 'Tallinn',
    'Finland': 'Helsinki',
    'France': 'Paris',
    'Germany': 'Berlin',
    'Greece': 'Athens',
    'Hungary': 'Budapest',
    'Iceland': 'Reykjavík',
    'Ireland': 'Dublin',
    'Italy': 'Rome',
    'Latvia': 'Riga',
    'Lithuania': 'Vilnius',
    'Luxembourg': 'Luxembourg City',
    'Macedonia': 'Skopje',
    'Malta': 'Valletta',
    'Moldova': 'Chisinau',
    'Monaco': 'Monaco',
    'Montenegro': 'Podgorica',
    'Netherlands': 'Amsterdam',
    'Norway': 'Oslo',
    'Poland': 'Warsaw',
    'Portugal': 'Lisbon',
    'Romania': 'Bucharest',
    'Russia': 'Moscow',
    'San Marino': 'San Marino',
    'Serbia': 'Belgrade',
    'Slovakia': 'Bratislava',
    'Slovenia': 'Ljubljana',
    'Spain': 'Madrid',
    'Sweden': 'Stockholm',
    'Switzerland': 'Bern',
    'Turkey': 'Ankara',
    'Ukraine': 'Kyiv',
    'United Kingdom': 'London'
}

for country, capital in capitals.items():
    # Use the full address of the capital instead of geocoding
    address = f'{capital}, Europe'
    folium.Marker(location=folium.Geocoder.geocode(address)[0]["location"], popup=country).add_to(m)

# Display the map
m