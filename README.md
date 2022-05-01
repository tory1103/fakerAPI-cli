What's Faker API?
-----------------
Faker Api - Generate Fake data by API requests       

	Faker API it's a collection of **completely free APIs** that helps web developers and web designers generate **fake data** in a fast and easy way. No registration is required. No tokens, no authentication.

	Every resource allows to choose the API language by the "\_locale" parameter and also allows to select the number of rows requested by the "\_quantity" parameter. **Max 1000 rows**.

	Check https://fakerapi.it/en for detailed information

	Current version: 1.2.0

	No registration is required. No tokens, no keys or other types of authentication. Faker API it's a free service for every developer who want to use it.

#### Base URL [#](https://fakerapi.it#base-url)

	https://fakerapi.it/api/v1/{resource}

#### Basic Usage [#](https://fakerapi.it#basic-usage)

	Some resources allow to filter data by GET parameters.  
	The names of these parameters are always preceded by an underscore character "\_", for example:

	https://fakerapi.it/api/v1/images?_width=380

	Data are always wrapped inside a "data" object and are always returned with the total number of rows ("total") and with the Http response "code".

	Every resource accepts 3 common GET parameters:

	* \_quantity
	* \_locale
	* \_seed

##### \_locale [#](https://fakerapi.it#params_locale)

	Default: en\_US

	This parameter means the language of the API response we want to get and accept the locale format "en\_EN". For example:

	https://fakerapi.it/api/v1/persons?_locale=fr_FR

	This example returns people with french names.

##### \_quantity [#](https://fakerapi.it#params_quantity)

	Default: 10

	Min: 1 - Max: 1000

	This parameter means the number of rows we want to obtain and accept only integers. If you request more than 1000 rows (maximum) the system will return 1000 rows anyway. Example:

	https://fakerapi.it/api/v1/companies?_quantity=5

	This example returns 5 companies.

##### \_seed [#](https://fakerapi.it#params_seed)

	Default: null

	This parameter accept an integer and allows to get always the same results. So, executing the same request with \_seed parameter set to the same value (ex. 12345) the results will never change. Example:

	https://fakerapi.it/api/v1/companies?_seed=12456

Changelogs
----------

#### 1.2.0

	Date of release: 08 January 2022

	*   New field "id" added to some resources (Persons, Users, Addresses, Companies, Products, Books)

#### 1.1.1

	Date of release: 30 April 2021

	*   Snake\_case synonyms for some "custom" resources
	*   General fixes

#### 1.1.0

	Date of release: 13 March 2021

	*   Upgrading core technologies

#### 1.0.2

	Date of release: 23 April 2020

	*   Added "pokemon" type to Custom resource
	*   Added Pokémon images to Image resource

#### 1.0.1

	Date of release: 14 April 2020

	*   Added "counter" type to Custom resource

#### 1.0.0

	Date of release: 12 April 2020

	*   First release

	Made for developers by Alessandro Pietrantonio - Contact me - [Cookie Policy](https://www.websitepolicies.com/policies/view/ZmgCERal)

	Sorry, you need Javascript on to email me.

