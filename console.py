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

        if class_name not in self.__models_classes:
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
        elif args[0] not in self.__models_classes:
            print("** class doesn't exist **")
        elif len(args) < 2:
            print("** instance id missing **")
        else:
            key = "{}.{}".format(args[0], args[1])
            if key not in all_objects:
                print("** no instance found **")
            else:
                print(all_objects[key])

    def do_destroy(self, arg):
        """ destroy instance """
        args = arg.split()
        obj = storage.all()
        if len(args) == 0:
            print("** class name missing **")
        elif args[0] not in self.__models_classes:
            print("** class doesn't exist **")
        elif len(args) == 1:
            print("** instance id missing **")
        elif f"{args[0]}.{args[1]}" not in obj.keys():
            print("** no instance found **")
        else:
            del obj["{}.{}".format(args[0], args[1])]
            storage.save()

    def do_all(self, arg):
        """ prints all strings """
        args = arg.split()
        if len(args) > 0 and args[0] not in self.__models_classes :
            print("** class doesn't exist **")
        else:
            obje = []
            for obj in storage.all().values() :
                if len(args) > 0 and args[0] == obj.__class__.__name__:
                    obje.append(obj.__str__())
                elif len(args) == 0:
                    obje.append(obj.__str__())
            print(obje)            


    def do_update(self, arg):
        args = arg.split()
        obj = storage.all()

        if len(args) == 0:
            print("** class name missing **")
            return False
        if args[0] not in self.__models_classes:
            print("** class doesn't exist **")
            return False
        if len(args) == 1:
            print("** instance id missing **")
            return False
        if "{}.{}".format(args[0], args[1]) not in obj.keys():
            print("** no instance found **")
            return False
        if len(args) == 2:
            print("** attribute name missing **")
            return False
        if len(args) == 3:
            try:
                type(eval(arg[2])) != dict
            except NameError:
                print("** value missing **")
                return False
        if len(args) == 4:
            objc = obj[f"{args[0]}.{args[1]}"]
            if args[2] in objc.__class__.__dict__.keys():
                valType = type(objc.__class__.__dict__[args[2]])
                objc.__dict__[args[2]] = valType(args[3])
            else:
                objc.__dict__[args[2]] = args[3]
        elif type(eval(args[2])) == dict:
            objc = obj[f"{args[0]}.{args[2]}"]
            for key, val in eval(args[2]).items():
                if key in objc.__class__.__dict__.keys() and type() in {str, int, float}:
                    valType = type(objc.__class__.__dict__[key])
                    objc.__dict__[key] = valType(val)
                else:
                    objc.__dict__[key] = val
        storage.save()

if __name__ == "__main__":
    HBNBCommand().cmdloop()