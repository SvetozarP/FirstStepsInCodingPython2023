from countryinfo import CountryInfo

country = input("Enter country name: ")

while country != "Stop":

    country_info = CountryInfo(country)

    print(f"Country Information:")
    print(f"Country name: ", country_info.name())
    print(f"Capital: ", country_info.capital())
    print(f"Population: ", country_info.population())
    print(f"Provinces: ", country_info.provinces())
    print(f"Currencies: ", country_info.currencies())
    print(f"Other names: ", country_info.alt_spellings())
    print(f"Calling code: ", country_info.calling_codes())
    print(f"Borders: ", country_info.borders())
    print(f"Timezones: ", country_info.timezones())
    print(f"Native name: ", country_info.native_name())
    print(f"Language(s) spoken: ", country_info.languages())
    print(f"Area: ", country_info.area())
    print(f"Region(s): ", country_info.region())
    print(f"Subregion(s): ", country_info.subregion())

    country = input("Enter country name: ")
