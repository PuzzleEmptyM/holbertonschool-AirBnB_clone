![holberton AIRBNB logo](https://github.com/PuzzleEmptyM/holbertonschool-AirBnB_clone/assets/129412985/bf9ea8b2-7337-4575-9ccc-bc244b78920a)
# The AirBnB clone
## This is a simple clone of the AirBNB website, created by Puzzle Moser and Amir Colbert

# Description
This project is a clone of AirBnB on a command line interface that allows the user to manage various AirBnB objects, including places, users, cities, and more. This project is written in Python 3, making use of the cmd module to manage the command line interface.

## Installation
Ensure you have Python 3 installed. Then, simply clone the repository.
```
git clone https://github.com/PuzzleEmptyM/holbertonschool-AirBnB_clone.git
```

## How to start
To start the program, navigate to the directory containing console.py and run the file with python3, 
```
python3 console.py
```
or with the dot-slash command.
```
./console.py
```

# Usage
The command interpreter allows you to manage the objects of your project.

## Commands
* quit or EOF to exit the program.
* create <class name> to create a new instance of the class.
* show <class name> <id> to display the specific instance based on the class name and id.
* destroy <class name> <id> to destroy a specific instance based on the class name and id.
* all <class name> or just all to display all instances of a class or all instances of every class.
* update <class name> <id> <attribute name> <attribute value> to update an instance based on the class name and id by adding or updating attribute.


description of the command interpreter:
    how to start it
    how to use it
    examples
```

## File Structure Visual:

```
.
├── AUTHORS
├── README.md
├── console.py
├── file.json
├── models
│   ├── __init__.py
│   ├── amenity.py
│   ├── base_model.py
│   ├── city.py
│   ├── engine
│   │   ├── __init__.py
│   │   └── file_storage.py
│   ├── place.py
│   ├── review.py
│   ├── state.py
│   └── user.py
└── tests
    ├── __init__.py
    └── test_models
        ├── __init__.py
        ├── test_amenity.py
        ├── test_base_model.py
        ├── test_city.py
        ├── test_engine
        │   ├── __init__.py
        │   └── test_file_storage.py
        ├── test_place.py
        ├── test_review.py
        ├── test_state.py
        └── test_user.py
```
