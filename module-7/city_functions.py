# Kristopher Duda. October 26, 2025. Assignment 7.2: Test Cases.
# Revises the previous 'city_functions.py' file to make language parameter optional.


# city_functions.py

def city_country(city, country, population=None, language=None):
    """
    If all parameters are provided, returns a string formatted as:
    'City, Country - population xxx, Language'
    Otherwise, it will exclude population and/or language parameters if they're not given. 
    
    """
    result = f"{city.title()}, {country.title()}"
    
    if population:
        result += f" - population {population}"
    
    if language:
        # Inserts comma before 'language' if there is additional info included
        if population:
            result += f", {language.title()}"
        else:
            result += f", {language.title()}"
    
    return result


# Call the function at least three times and print the results
print(city_country("london", "england"))
print(city_country("berlin", "germany",67000))
print(city_country("rome", "italy", 1110000,"italian"))
