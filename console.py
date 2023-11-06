#!/usr/bin/python3
"""defines the HBNBCommand class"""
import cmd
from models import storage
from models.base_model import BaseModel
from models.user import User

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
    
    def do_quit(self, arg):
        """Quit command to exit the program"""
        return True
    
    def do_EOF(self, argu):
        """EOF command to exit the program"""
        print("")
        return True

    def emptyline(self):
        """Empty line shouldn't execute anything"""
        pass

    def do_create(self, arg):
        """Create a new instance of BaseModel and save it"""
        args = arg.split()

        if not args:
            print("** class name missing **")
            return

        class_name = args[0]
        all_objects = storage.all()

        if class_name not in HBNBCommand.__models_classes:
            print("** class doesn't exist **")
        else:
            new_instance = eval(class_name)()
            new_instance.save()
            print(new_instance.id)

    def do_show(self, arg):
        """Show the string representation of an instance"""
        args = arg.split()
        all_objects = storage.all()

        if len(args) == 0:
            print("** class name missing **")
        elif args[0] not in HBNBCommand.__models_classes:
            print("** class doesn't exist **")
        elif len(args) < 2:
            print("** instance id missing **")
        else:
            key = "{}.{}".format(args[0], args[1])
            if key not in all_objects:
                print("** no instance found **")
            else:
                print(all_objects[key])


if __name__ == "__main__":
    HBNBCommand().cmdloop()