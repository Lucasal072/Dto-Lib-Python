# DtoLib

DtoLib is a Data Transfer Object (DTO) library developed to simplify data transfer between layers in software projects. This library provides advanced features to facilitate development and increase code maintainability.

## Features

- **Simplified DTO definition**: With DtoLib, it's easy and quick to define the necessary DTO objects for data transfer between system components.

- **Independence from underlying data structure**: DTOs created with DtoLib are independent of the database structure and business entities. This provides greater flexibility and modularity to the project.

- **Automatic data validation**: The library offers built-in data validation features, allowing you to define validation rules for your DTOs and easily check if the data is compliant.

- **Bidirectional mapping between DTOs and business entities**: With DtoLib, you can perform automatic and easy mapping between DTOs and business entities, simplifying data conversion between layers.


## Installation

You can add DtoLib as a dependency in your project using your preferred package manager. For example, with pip:

```shell
pip install DtoLib
```

## Usage

To start using DtoLib in your project, simply import the necessary modules and utilize the functionalities offered by the library. Below is a simple example of how to create and use a DTO with DtoLib:

```python
from DtoLib import AbstractDto,DtoField

# Define a DTO
class UserDTO(AbstractDto):
    username = DtoField[str](required=True,help='invalid username')
    password = DtoField[str](required=True,help='invalid password')

# Create an instance of the DTO
user = UserDTO({"username":"admin","password":"admin"})

# Access DTO data
print(user.name.value)   # 'admin'
print(user.password.value)  # 'admin'
print(user.dict()) # {"username":"admin","password":"admin"}
```

## Contribution

We appreciate your interest in contributing to the development of DtoLib! To contribute, please follow these steps:

1. Fork the repository.
2. Create a branch with the name of your feature: `git checkout -b my-feature`.
3. Make the desired code changes.
4. Commit your changes: `git commit -m 'Implementation of my feature'`.
5. Push to the branch: `git push origin my-feature`.
6. Open a pull request in the original repository.

## License

DtoLib is distributed under the MIT License.
