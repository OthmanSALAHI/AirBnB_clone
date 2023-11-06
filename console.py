#!/usr/bin/python3
"""defines the HBNBCommand class"""
import cmd
from models import storage
from models.base_model import BaseModel

class HBNBCommand(cmd.Cmd):
    """represents the entry point of the command interpreter"""

    prompt = "(hbnb) "
    
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
        if not arg:
            print("** class name missing **")
            return
        try:
            new_instance = eval(arg)()
            new_instance.save()
            print(new_instance.id)
        except NameError:
            print("** class doesn't exist **")
if __name__ == "__main__":
    HBNBCommand().cmdloop()