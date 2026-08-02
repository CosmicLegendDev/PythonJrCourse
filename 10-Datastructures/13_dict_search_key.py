# We have a dictionary of county and capital, we need a 
# a program to search for country and corresponding capital.

#variable declaration
country_capital = {
    "America": "WashingtonDC",
    "India": "NewDelhi",
    "Australia": "Canberra",
    "China": "Beijing",
    "Russia": "Mascow",
    "SouthAfrica": "Pretoria",
    "Brazil": "Brasilla",
    "Canada": "Ottawa",
    "France": "Paris",
    "Japan": "Tokyo",
    "Indonesia": "Jakarta"
}

# Search for country in the dictionary

country_input = input("Enter Country Name: ").capitalize()
print(f"Searching for country: {country_input}")

is_capital_found = False

for k, v in country_capital.items():
    if k == country_input:
        is_capital_found = True
        break
    
if is_capital_found:
    print(f"Capital of {country_input} is {country_capital.get(country_input)}")  
else:
    print(f"Country {country_input} is not listed")

# Option 2:
print("---- Option 2------")
if country_capital.__contains__(country_input):
    print(f"Capital of {country_input} is {country_capital.get(country_input)}")
else:
    print("Country in not listed.")





