import pandas as pd
import sys
import os
import pygal
import webbrowser

pygal.maps.world.World()

args = sys.argv

if "-h" == args[1]:
    print("The world map generator takes in a CSV file that contains data about countries and the maps them onto an SVG map")
    print("The user can select the column from the CSV file that is used to plot data as well as the theme")
    sys.exit()

data = pd.read_csv(sys.argv[1])

countryCodes = {'Andorra': 'ad', 'United Arab Emirates': 'ae', 'Afghanistan': 'af', 'Antigua & Barbuda': 'ag', 'Antigua and Barbuda': 'ag', 'Anguilla': 'ai', 'Albania': 'al', 'Armenia': 'am', 'Netherlands Antilles': 'an', 'Angola': 'ao', 'Antarctica': 'aq', 'Argentina': 'ar', 'American Samoa': 'as', 'Austria': 'at', 'Australia': 'au', 'Aruba': 'aw', 'Azerbaijan': 'az', 'Bosnia and Herzegovina': 'ba', 'Barbados': 'bb', 'Bangladesh': 'bd', 'Belgium': 'be', 'Burkina Faso': 'bf', 'Bulgaria': 'bg', 'Bahrain': 'bh', 'Burundi': 'bi', 'Benin': 'bj', 'Bermuda': 'bm', 'Brunei Darussalam': 'bn', 'Brunei': 'bn', 'Bolivia': 'bo', 'Brazil': 'br', 'Bahama': 'bs', 'The Bahama': 'bs', 'The Bahamas': 'bs', 'Bhutan': 'bt', 'Burma (no longer exists)': 'bu', 'Bouvet Island': 'bv', 'Botswana': 'bw', 'Belarus': 'by', 'Belize': 'bz', 'Canada': 'ca', 'Cocos (Keeling) Islands': 'cc', 'Central African Republic': 'cf', 'Congo': 'cg', 'Republic of the Congo': 'cg','Democratic Republic of the Congo': 'cd', 'Switzerland': 'ch', "Côte D'ivoire (Ivory Coast)": 'ci', "Ivory Coast": 'ci', 'Cook Islands': 'ck', 'Chile': 'cl', 'Cameroon': 'cm', 'China': 'cn', 'Colombia': 'co', 'Costa Rica': 'cr', 'Czechoslovakia (no longer exists)': 'cs', 'Cuba': 'cu', 'Cape Verde': 'cv', 'Christmas Island': 'cx', 'Cyprus': 'cy', 'Czech Republic': 'cz', 'German Democratic Republic (no longer exists)': 'dd', 'Germany': 'de', 'Djibouti': 'dj', 'Denmark': 'dk', 'Dominica': 'dm', 'Dominican Republic': 'do', 'Algeria': 'dz', 'Ecuador': 'ec', 'Estonia': 'ee', 'Egypt': 'eg', 'Western Sahara': 'eh', 'Eritrea': 'er', 'Spain': 'es', 'Ethiopia': 'et', 'Finland': 'fi', 'Fiji': 'fj', 'Falkland Islands (Malvinas)': 'fk', 'Micronesia': 'fm', 'Federated States of Micronesia': 'fm', 'Faroe Islands': 'fo', 'France': 'fr', 'France, Metropolitan': 'fx', 'Gabon': 'ga', 'United Kingdom': 'gb', 'Grenada': 'gd', 'Georgia': 'ge', 'French Guiana': 'gf', 'Ghana': 'gh', 'Gibraltar': 'gi', 'Greenland': 'gl', 'Gambia': 'gm', 'The Gambia': 'gm', 'Guinea': 'gn', 'Guadeloupe': 'gp', 'Equatorial Guinea': 'gq', 'Greece': 'gr', 'South Georgia and the South Sandwich Islands': 'gs', 'Guatemala': 'gt', 'Guam': 'gu', 'Guinea-Bissau': 'gw', 'Guinea0Bissau': 'gw', 'Guyana': 'gy', 'Hong Kong': 'hk', 'Heard & McDonald Islands': 'hm', 'Honduras': 'hn', 'Croatia': 'hr', 'Haiti': 'ht', 'Hungary': 'hu', 'Indonesia': 'id', 'Ireland': 'ie', 'Republic of Ireland': 'ie', 'Israel': 'il', 'India': 'in', 'British Indian Ocean Territory': 'io', 'Iraq': 'iq', 'Islamic Republic of Iran': 'ir', 'Iran': 'ir', 'Iceland': 'is', 'Italy': 'it', 'Jamaica': 'jm', 'Jordan': 'jo', 'Japan': 'jp', 'Kenya': 'ke', 'Kyrgyzstan': 'kg', 'Cambodia': 'kh', 'Kiribati': 'ki', 'Comoros': 'km', 'St. Kitts and Nevis': 'kn', 'Saint Kitts and Nevis': 'kn', "Korea, Democratic People's Republic of": 'kp', "North Korea": 'kp', 'Korea, Republic of': 'kr', 'South Korea': 'kr', 'Kuwait': 'kw', 'Cayman Islands': 'ky', 'Kazakhstan': 'kz', "Lao People's Democratic Republic": 'la', "Laos": 'la', 'Lebanon': 'lb', 'Saint Lucia': 'lc', 'Liechtenstein': 'li', 'Sri Lanka': 'lk', 'Liberia': 'lr', 'Lesotho': 'ls', 'Lithuania': 'lt', 'Luxembourg': 'lu', 'Latvia': 'lv', 'Libyan Arab Jamahiriya': 'ly', 'Libya': 'ly', 'Morocco': 'ma', 'Monaco': 'mc', 'Montenegro':'me', 'Moldova, Republic of': 'md', 'Moldova': 'md', 'Madagascar': 'mg', 'Marshall Islands': 'mh', 'Mali': 'ml', 'Mongolia': 'mn', 'Myanmar': 'mm', 'Macau': 'mo', 'Northern Mariana Islands': 'mp', 'Serbia':'rs', 'Martinique': 'mq', 'Mauritania': 'mr', 'Monserrat': 'ms', 'Montserrat': 'ms', 'Malta': 'mt', 'Mauritius': 'mu', 'Maldives': 'mv', 'Malawi': 'mw', 'Mexico': 'mx', 'Malaysia': 'my', 'Mozambique': 'mz', 'Namibia': 'na', 'New Caledonia': 'nc', 'Niger': 'ne', 'Norfolk Island': 'nf', 'Nigeria': 'ng', 'Nicaragua': 'ni', 'Netherlands': 'nl', 'Norway': 'no', 'Nepal': 'np', 'Nauru': 'nr', 'Neutral Zone (no longer exists)': 'nt', 'Niue': 'nu', 'New Zealand': 'nz', 'Oman': 'om', 'Panama': 'pa', 'Peru': 'pe', 'French Polynesia': 'pf', 'Papua New Guinea': 'pg', 'Philippines': 'ph', 'Pakistan': 'pk', 'Poland': 'pl', 'St. Pierre & Miquelon': 'pm', 'Pitcairn': 'pn', 'Puerto Rico': 'pr', 'Portugal': 'pt', 'Palau': 'pw', 'Paraguay': 'py', 'Qatar': 'qa', 'Réunion': 're', 'Romania': 'ro', 'Russian Federation': 'ru', 'Russia': 'ru', 'Rwanda': 'rw', 'Saudi Arabia': 'sa', 'Solomon Islands': 'sb', 'Seychelles': 'sc', 'Sudan': 'sd', 'Sweden': 'se', 'Singapore': 'sg', 'St. Helena': 'sh', 'Slovenia': 'si', 'Svalbard & Jan Mayen Islands': 'sj', 'Slovakia': 'sk', 'Sierra Leone': 'sl', 'San Marino': 'sm', 'Senegal': 'sn', 'Somalia': 'so', 'Suriname': 'sr', 'Sao Tome & Principe': 'st', 'Union of Soviet Socialist Republics (no longer exists)': 'su', 'Palestinian National Authority':'ps', 'El Salvador': 'sv', 'Syrian Arab Republic': 'sy', 'Syria': 'sy', 'Swaziland': 'sz', 'Eswatini': 'sz', 'Turks & Caicos Islands': 'tc', 'Turks and Caicos Islands': 'tc', 'Chad': 'td', 'French Southern Territories': 'tf', 'Togo': 'tg', 'Thailand': 'th', 'Tajikistan': 'tj', 'Tokelau': 'tk', 'Turkmenistan': 'tm', 'Tunisia': 'tn', 'Tonga': 'to', 'East Timor': 'tp', 'Turkey': 'tr', 'Trinidad & Tobago': 'tt', 'Trinidad and Tobago': 'tt', 'Tuvalu': 'tv', 'Taiwan, Province of China': 'tw', 'Tanzania, United Republic of': 'tz', 'Tanzania': 'tz', 'Ukraine': 'ua', 'Uganda': 'ug', 'United States Minor Outlying Islands': 'um', 'United States': 'us', 'Uruguay': 'uy', 'Uzbekistan': 'uz', 'Vatican City State': 'va', 'Vatican City': 'va', 'St. Vincent & the Grenadines': 'vc', 'Saint Vincent and the Grenadines': 'vc', 'Venezuela': 've', 'British Virgin Islands': 'vg', 'United States Virgin Islands': 'vi', 'Viet Nam': 'vn', 'Vietnam': 'vn', 'Vanuatu': 'vu', 'Wallis & Futuna Islands': 'wf', 'Samoa': 'ws', 'Democratic Yemen (no longer exists)': 'yd', 'Yemen': 'ye', 'Mayotte': 'yt', 'Yugoslavia': 'yu', 'South Africa': 'za', 'Zambia': 'zm', 'Zaire': 'zr', 'Zimbabwe': 'zw', 'North Macedonia':'mk', 'South Sudan':'ss', 'Unknown or unspecified country': 'zz'}

nameCountriesCol = ""
numCountries = ""
colName = ""
dataType = ""
mapName = ""
colorScheme = ""
outputName = ""

def dashboard():
    os.system('cls' if 'nt' == os.name else 'clear')
    print("File has been loaded in. Fill in info to generate map")
    print(f"|File Name            |{sys.argv[1]}")
    print(f"|Name of Countries Col|{nameCountriesCol}")
    print(f"|Identified Countries |{numCountries}")
    print(f"|Data Column name     |{colName}")
    print(f"|Data type            |{dataType}")
    print(f"|Map Name             |{mapName}")
    print(f"|Map Style            |{colorScheme}")
    print(f"|Output file Name     |{outputName}")


dashboard()
validInput = 0
while validInput != 1:
    nameCountriesCol = input("input the name of the countries column. Input list for list of columns:")
    if "list" == nameCountriesCol:
        print("\n".join(data.columns))
    if nameCountriesCol in data.columns:
        validInput = 1
numCountries = len(data.index)

dashboard()
validInput = 0
while validInput != 1:
    colName = input("input the name of the column that you want to map. Input list for list of columns:")
    if "list" == colName:
        print("\n".join(data.columns))
    elif colName in data.columns:
        validInput = 1

dashboard()
validInput = 0
while validInput != 1:
    dataType = input("input wether the data is in a range (R) or if data points are unique (U):").upper()
    if dataType == "U" or dataType == "R":
        validInput = 1

dashboard()
mapName = input("input Map Name:")

dashboard()
validColorSchemes = ["default","dark","neon","dark solarized","light solarized","light","clean","red blue","dark colorized","light colorized","turquoise","light green","dark green","dark green blue","blue"]
validInput = 0
while validInput != 1:
    colorScheme = input("input a valid map style. input list for style list:")
    if "list" == colorScheme:
        print("\n".join(validColorSchemes))
    elif colorScheme in validColorSchemes:
        validInput = 1

dashboard()
validInput = 0
while validInput != 1:
    outputName = input("input the name of the output file (do not include .svg):").upper()
    if "." not in outputName:
        validInput = 1

dashboard()
validInput = 0
while validInput != 1:
    check = input("create map (y/n):").upper()
    if "Y" == check or "N" == check:
        validInput = 1

unrecognizedCountries = []
for index, row in data.iterrows():
    try:
        data.at[index,nameCountriesCol] = countryCodes[row[nameCountriesCol]]
    except:
        unrecognizedCountries.append(row[nameCountriesCol])

worldMap = pygal.maps.world.World()
worldMap.title = mapName

if "R" == dataType:
    dataToAdd = {}
    for index, row in data.iterrows():
        if 2 == len(data.at[index,nameCountriesCol]):
            dataToAdd[data.at[index,nameCountriesCol]] = data.at[index,colName]
        
    worldMap.add(colName,dataToAdd)
else:
    dataToAdd = {}
    for index, row in data.iterrows():
        if dataToAdd.get(data.at[index,colName]) is not None and 2 == len(data.at[index,nameCountriesCol]):
            dataToAdd[data.at[index,colName]].append(data.at[index,nameCountriesCol])
        elif 2 == len(data.at[index,nameCountriesCol]):
            dataToAdd[data.at[index,colName]] = [(data.at[index,nameCountriesCol])]
    
    print(dataToAdd)

    for i in dataToAdd:
        worldMap.add(i,dataToAdd[i])



if "default" == colorScheme: 
    worldMap.style = pygal.style.DefaultStyle
if "dark" == colorScheme: 
    worldMap.style = pygal.style.DarkStyle
if "neon" == colorScheme: 
    worldMap.style = pygal.style.NeonStyle
if "dark solarized" == colorScheme: 
    worldMap.style = pygal.style.DarkSolarizedStyle
if "light solarized" == colorScheme: 
    worldMap.style = pygal.LightSolarizedStyle
if "light" == colorScheme: 
    worldMap.style = pygal.LightStyle
if "clean" == colorScheme: 
    worldMap.style = pygal.CleanStyle
if "red blue" == colorScheme: 
    worldMap.style = pygal.RedBlueStyle
if "dark colorized" == colorScheme: 
    worldMap.style = pygal.DarkColorizedStyle
if "light colorized" == colorScheme: 
    worldMap.style = pygal.LightColorizedStyle
if "turquoise" == colorScheme: 
    worldMap.style = pygal.TurquoiseStyle
if "light green" == colorScheme: 
    worldMap.style = pygal.LightGreenStyle
if "dark green" == colorScheme: 
    worldMap.style = pygal.DarkGreenStyle
if "dark green blue" == colorScheme: 
    worldMap.style = pygal.DarkGreenBlueStyle
if "blue" == colorScheme: 
    worldMap.style = pygal.BlueStyle


worldMap.render_to_file(f'{outputName}.svg')

webbrowser.open(f'{outputName}.svg')

dashboard()
print(f"countries not found: {' | '.join(unrecognizedCountries)}")