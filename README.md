# AirBnB_clone 
![Flowchart](https://imgur.com/xuoucfD.png)
 Built in python3, this project emulates the functioning of the AirBnB website.
 This version is called The Holberton B&B, and it is a project for [Holberton School Medellín](https://www.holbertonschool.com/co/campus_life/medellin).
 
## Flowchart
We will develop the backend as well as the frontend part of the website. Here is a diagram of the project and a hint of the technologies we used.
 
 ![Flowchart](https://imgur.com/3rCP5Fx.png)
 
 ## The Console
 There is a built-in command line interpreter (console) that provides a way to interact with the Storage-engine.
 
 Thru the console is possible to: 
* Create a new object (ex: a new User or a new Place)
* Retrieve an object from a file, a database etc…
* Do operations on objects (count, compute stats, etc…)
* Update attributes of an object
* Destroy an object

## Getting started

First. Clone this repository in your machine.
```sh
$ https://github.com/carlosz22/AirBnB_clone
```
Go to the repo.

```sh
$ cd AirBnB_clone
```
After that, it is all set to start using the console like this

```sh
$ ./console.py
```

## Usage

After running the last command (./console.py), you will see a prompt.

```sh
(hbnb) 
```

This means, the console is ready to get some commands ;).

### Available Commands
| Command | Arguments | Description |
| ------ | ------ | ------ |
| `create` | `<class name>` | Creates a new class from the available class-list ||
| `show` | `<class name> <id>` | Prints the string representation of an instance based on the class name and id. |
| `destroy` | `<class name> <id>` | Deletes an instance based on the class name and id (save the change into the JSON file). |
| `all` | `[ <class name>]` | Prints all string representation of all instances based or not on the class name |
| `update` | `<class name> <id> <attribute name> "<attribute value>"`  | Updates an instance based on the class name and id by adding or updating attribute (save the change into the JSON file |
| `.all()`| `<class name>.all()` | Retrieves all instances of a class |
| `.count()` | `<class name>.count()` | Retrieves the number of instances of a class |
| `.show(<id>)` | `<class name>.show(<id>`) | Retrieves an instance based on its ID |
| `.destroy(<id>)` | `<class name>.destroy(<id>)` | Destroys an instance based on his ID |
| `.update(<id>, <attr name>, <attr value>)` | `<class name>.update(<id>, <attr name>, <attr value>)` | Updates an instance based on his ID |
| `.dupdate(<id>, <dict repr>)` | `<class name>.update(<id>, <dictionary representation>)` | Updates an instance based on his ID with a dictionary |

## Available Classes
To get the power of the console. It is necessary to describe the classes that we have developed to create Hbnb website.

| Class | Descripion| Attributes|
| ------ | ------ | ------ |
| `BaseModel()` | Defines all common attributes/methods for other classes, that will inherit from | id, created_at, updated_at|
| `User()` | Inherits from BaseModel and represents an user  | `email`, `password`, `first_name`, `last_name`  |
| `State()` | Inherits from BaseModel and represents a geographic point  | `name` |
| `City()` | Inherits from BaseModel  | `state_id`, `name` |
| `Amenity()` | Inherits from BaseModel and represents desirable or useful feature of the place | `name` |
| `Place()` | Inherits from BaseModel | `city_id`, `user_id`, `name`, `description`, `number_rooms`, `number_bathrooms`, `max_guest`, `latitude`, `longitude`, `amenity_ids`|
| `Review()` | Inherits from BaseModel, takes reviews from guests | `place_id`, `user_id`, `text` |
| `FileStorage()` | Serializes instances to a JSON file and deserializes JSON file to instances. Works as an engine to manage all the data | `__objects`, `__file_path` |
## Examples of Use:
The console is very powerful since it allows the developer to manage the data when the server is off, giving him the chance to work with the command line

The console has the mentioned built-in commands. Here is an example of how to use it.

### Create an User

```sh
(hbnb) create User
2f9fa3f9-4de5-4d1b-863a-1d1a140d5868
```
The command create retrieves an Id that will be super useful to use the other commands

### Show a previously created object

With the Id we already have, we can look for the User we have created
```sh
(hbnb) show User 2f9fa3f9-4de5-4d1b-863a-1d1a140d5868
[User] (2f9fa3f9-4de5-4d1b-863a-1d1a140d5868) {'id': '2f9fa3f9-4de5-4d1b-863a-1d1a140d5868', 'created_at': datetime.datetime(2019, 11, 13, 13, 58, 14, 530494), 'updated_at': datetime.datetime(2019, 11, 13, 13, 58, 14, 530515)}
```

### Destroy an object

It is also useful to delete non necessary objects
```sh 
(hbnb) destroy User 2f9fa3f9-4de5-4d1b-863a-1d1a140d5868
(hbnb) show User 2f9fa3f9-4de5-4d1b-863a-1d1a140d5868
*** instance not found ***
```

Enjoy! :)

# Authors
* Othman  Salahi [X](https://x.com/othmansalahi) [LinkedIn](https://www.linkedin.com/in/othmansalahi)
* Mohamed Dani [X](https://twitter.com/mohameddani_1) [LinkedIn](www.linkedin.com/in/mohamed-dani-2a8065152)