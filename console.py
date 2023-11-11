#!/usr/bin/python3
"""defines the HBNBCommand class"""
import cmd
import re
from shlex import split
import os
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.review import Review
from models.place import Place
from models import storage


def parse_arg(arg):
    curly_braces = re.search(r"\{(.*?)\}", arg)
    brackets = re.search(r"\[(.*?)\]", arg)
    if curly_braces is None:
        if brackets is None:
            return [i.strip(",") for i in split(arg)]
        else:
            lexer = split(arg[: brackets.span()[0]])
            retl = [i.strip(",") for i in lexer]
            retl.append(brackets.group())
            return retl
    else:
        lexer = split(arg[: curly_braces.span()[0]])
        retl = [i.strip(",") for i in lexer]
        retl.append(curly_braces.group())
        return retl


class HBNBCommand(cmd.Cmd):
    """represents the entry point of the command interpreter"""

    prompt = "(hbnb) "
    __models_classes = {
        "BaseModel",
        "User",
        "State",
        "City",
        "Place",
        "Amenity",
        "Review",
    }

    def emptyline(self):
        """empty argu + ENTER shouldn’t execute anything"""
        pass

    def default(self, argu):
        """
        default commands
            usage: <class name>.<command>(<id>)
        """
        if argu.endswith(".all()"):
            """
            Check if the command matches
            <class_name>.all()
            """
            class_name = argu[:-6].strip()
            if class_name:
                self.do_all(class_name)
        elif argu.endswith(".count()"):
            """
            Check if the command matches
            <class_name>.count()
            """
            class_name = argu[:-8].strip()
            if class_name in self.__models_classes:
                num_obj = sum(1 for key in storage.all() if class_name in key)
                print(num_obj)
            else:
                print("** class doesn't exist **")
        elif ".show(" in argu and argu.endswith(")"):
            """
            Check if the command matches
            <class_name>.show(<id>)
            """
            match = re.search(r"(\w+)\.show\((.*)\)", argu)
            if match:
                class_name = match.group(1)
                instance_id = match.group(2)
                self.do_show(f"{class_name} {instance_id}")
        elif ".destroy(" in argu and argu.endswith(")"):
            """
            Check if the command matches
            <class_name>.destroy(<id>)
            """
            match = re.search(r"(\w+)\.destroy\((.*)\)", argu)
            if match:
                class_name = match.group(1)
                instance_id = match.group(2)
                self.do_destroy(f"{class_name} {instance_id}")
        elif ".update(" in argu and argu.endswith(")"):
            match = re.search(r"(\w+)\.update\((.*)\)", argu)
            if match:
                class_name = match.group(1)
                args = match.group(2)
                if "{" in args and args.endswith("}"):
                    id = args.split(", ")[0]
                    str_dict = "{" + args.split("{")[1]
                    dictionary = dict(eval(str_dict))
                    string = f"{class_name} {id}"
                    for attr, value in dictionary.items():
                        self.do_update(
                            f'{string} {attr} "{str(value)}"'
                        )
                else:
                    string = class_name
                    for elm in args.split(", "):
                        string += " " + elm
                    self.do_update(string)
        else:
            print("*** Unknown syntax: {}".format(argu))
            return False

    def do_quit(self, argu):
        """Quit command to exit the program"""
        return True

    def do_EOF(self, argu):
        """EOF command to exit the program"""
        print("")  # ! print new line at the end of file
        return True

    def do_create(self, arg):
        """Create a new instance of BaseModel and print the id"""
        model = parse_arg(arg)
        if len(model) == 0:
            print("** class name missing **")
        elif model[0] not in HBNBCommand.__models_classes:
            print("** class doesn't exist **")
        else:
            print(eval(model[0])().id)
            storage.save()

    def do_show(self, arg):
        """show the string representation of an instance"""
        arg = parse_arg(arg)
        obj = storage.all()
        if len(arg) == 0:
            print("** class name missing **")
        elif arg[0] not in HBNBCommand.__models_classes:
            print("** class doesn't exist **")
        elif len(arg) == 1:
            print("** instance id missing **")
        elif "{}.{}".format(arg[0], arg[1]) not in obj:
            print("** no instance found **")
        else:
            print(obj["{}.{}".format(arg[0], arg[1])])

    def do_destroy(self, arg):
        """destroy an instance"""
        arg = parse_arg(arg)
        print(arg)
        obj = storage.all()
        if len(arg) == 0:
            print("** class name missing **")
        elif arg[0] not in self.__models_classes:
            print("** class doesn't exist **")
        elif len(arg) == 1:
            print("** instance id missing **")
        elif "{}.{}".format(arg[0], arg[1]) not in obj.keys():
            print("** no instance found **")
        else:
            del obj["{}.{}".format(arg[0], arg[1])]
            storage.save()

    def do_all(self, arg):
        """show all instances"""
        argu = parse_arg(arg)
        if len(argu) > 0 and argu[0] not in HBNBCommand.__models_classes:
            print("** class doesn't exist **")
        else:
            objl = []
            for obj in storage.all().values():
                if len(argu) > 0 and argu[0] == obj.__class__.__name__:
                    objl.append(obj.__str__())
                elif len(argu) == 0:
                    objl.append(obj.__str__())
            print(objl)

    def do_update(self, arg):
        """methode that update instance"""
        arg = parse_arg(arg)
        obj = storage.all()
        if len(arg) == 0:
            print("** class name missing **")
            return False
        if arg[0] not in HBNBCommand.__models_classes:
            print("** class doesn't exist **")
            return False
        if len(arg) == 1:
            print("** instance id missing **")
            return False
        if "{}.{}".format(arg[0], arg[1]) not in obj.keys():
            print("** no instance found **")
            return False
        if len(arg) == 2:
            print("** attribute name missing **")
            return False
        if len(arg) == 3:
            try:
                type(eval(arg[2])) != dict
            except NameError:
                print("** value missing **")
                return False
        if len(arg) == 4:
            ob = obj["{}.{}".format(arg[0], arg[1])]
            if arg[2] in ob.__class__.__dict__.keys():
                valuetyp = type(ob.__class__.__dict__[arg[2]])
                ob.__dict__[arg[2]] = valuetyp(arg[3])
            else:
                ob.__dict__[arg[2]] = arg[3]
        elif type(eval(arg[2])) == dict:
            ob = obj["{}.{}".format(arg[0], arg[1])]
            for key, value in eval(arg[2]).items():
                if key in ob.__class__.__dict__.keys() and type(
                    ob.__class__.__dict__[key]
                ) in {str, int, float}:
                    valuetyp = type(ob.__class__.__dict__[key])
                    ob.__dict__[key] = valuetyp(value)
                else:
                    ob.__dict__[key] = value
        storage.save()

    def do_count(self, arg):
        """count the number of instances"""
        arg = parse_arg(arg)
        obj = storage.all()
        if len(arg) == 0:
            print("** class name missing **")
        elif arg[0] not in HBNBCommand.__models_classes:
            print("** class doesn't exist **")
        else:
            count = 0
            for key in obj.values():
                if arg[0] == key.__class__.__name__:
                    count += 1
            print(count)


if __name__ == "__main__":
    HBNBCommand().cmdloop()
