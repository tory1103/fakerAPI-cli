<div align="center">

# What's Faker API?

<img src="https://fakerapi.it/assets/img/symbol.png" width="100px">

Faker API it's a collection of **completely free APIs** that helps web developers and web designers generate **fake data** in a fast and easy way. No registration is required. No tokens, no authentication.

Every resource allows to choose the API language by the "\_locale" parameter and also allows to select the number of rows requested by the "\_quantity" parameter. **Max 1000 rows.**

**Working with API Version: 1.2.0**

</div>

---

# 🏁 Getting started

## Installation

### Using python3 setup.py
```bash
# Clone repository and change directory to it
$ git clone https://github.com/tory1103/fakerAPI-cli.git
$ cd fakerAPI-cli

# Install source code with setup.py
$ python3 setup.py install

# FakerAPI is ready to use. Type: fake --help
$ fake --help
```

### Using docker images and aliases
```bash
# Docker must be installed in machine
# Clone repository and change directory to it
$ git clone https://github.com/tory1103/fakerAPI-cli.git
$ cd fakerAPI-cli

# Create Docker image using Dockerfile
$ docker build -t fakerAPI:latest .

# Using Docker image as entrypoint
$ docker run -it --rm fakerAPI:latest <args>

# Create shell alias to use it anywhere
# If you want it to start with shell session,
# add alias command to shell config file.
$ alias fake='docker run -it --rm fakerAPI:latest'

# FakerAPI is ready to use. Type: fake --help
$ fake --help
```

### Using source code
```bash
# Clone repository and change directory to it
$ git clone https://github.com/tory1103/fakerAPI-cli.git
$ cd fakerAPI-cli/src/fakerapi/

# Run python3 script
$ python3 main.py <args>
```

---

## Documentation
This is an summary documentation. We recommend looking for official docs

> For detailed documentation look at [official page](https://fakerapi.it/en)

### Basic usage

#### FakerAPI resources list:		
- Addresses
- Books
- Companies
- Credit Cards
- Images
- Persons
- Places
- Products
- Texts
- Users
- Custom

#### Function header
```python 
def fake(resource: str, quantity: int = 1, locale: str = "en_US", seed: int = None, **kwargs)
```

#### Some code examples
```bash
# Main program syntax
$ fake <resource> <args_based_on_header>

# Fetching persons data
$ fake persons 10

# Fetching companies data
$ fake companies

# Using extra and custom args
# Additional API parameters are always preceded by an underscore character "_"
# So, this is how it should look like:
$ fake persons 10 --_gender=male
```

