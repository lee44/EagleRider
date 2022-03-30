from countryinfo import CountryInfo


def getCurrency(country):
    currencies = CountryInfo(country).currencies()
