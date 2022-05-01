from requests import get
from fire import Fire

class FakerAPI:
    """
    Faker API it's a collection of completely free APIs that helps web developers and web designers generate fake data in a fast and easy way.
    No registration is required. No tokens, no authentication.
    Every resource allows to choose the API language by the "_locale" parameter and also allows to select the number of rows requested by the "_quantity" parameter. Max 1000 rows.

    For more information about how to use FakerAPI type: 
        python3 main.py fake --help

    Some examples:
        - python3 main.py fake persons 10
        - python3 main.py fake companies
        - python3 main.py fake custom customParam=customValue

    Author  : Adrian Toral
    Program : Faker API Handler
    Update  : 1-05-2022
    Version : 1.2.0.fakerapi (08-01-2022)
    """

    def __request(self, resource: str, **kwargs): return get("https://fakerapi.it/api/v1/{resource}".format(resource=resource), params=kwargs).text

    def fake(self, resource: str, quantity: int = 1, locale: str = "en_US", seed: int = None, **kwargs):
        """
        Fake function return the generated data from fakerapi.it as json object

        Resource param must be some of these options:
            - addresses
            - books
            - companies
            - credit_cards
            - images
            - persons
            - places
            - products
            - texts
            - users
            - custom

        Some of these resources have extra parameters.
        For more information look FakerAPI Docs: https://fakerapi.it/en

        :param resource: Resource to fetch data from
        :param quantity: Amount of data to fetch
        :param locale: Custom location for the data 
        :param seed: Custom seed for fetching the data
        :param **kwargs: Extra parameters for API
        """

        return self.__request(
                resource, 
                _quantity=quantity,
                _locale=locale,
                _seed=seed,
                **kwargs
                )

def main():
    """
    Main program entry-point
    """

    Fire(FakerAPI().fake)

if __name__ == "__main__": main()

