#!/usr/bin/python3
"""Class HBNBComand a program called console.py
"""

import re
import cmd
import json
from models import storage
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.place import Place
from models.amenity import Amenity
from models.review import Review

classes = {'BaseModel': BaseModel, 'User': User, 'Place': Place,
           'State': State, 'City': City, 'Amenity': Amenity, 'Review': Review}


class HBNBCommand(cmd.Cmd):
    """ hbnb command interpreter """
    prompt = '(hbnb) '

    def do_EOF(self, line):
        """ End of file"""
        return True

    def do_quit(self, line):
        """ exit the program"""
        return True

    def emptyline(self):
        """don´t execute nothing """
        pass

    def do_create(self, line):
        """ Creates a new instance """
        if not (line):
            print("** class name missing **")
        elif line not in HBNBCommand.classes:
            print("** class doesn't exist **")
        else:
            instance = eval[input_line]()
            instance.save()
            print(instance.id)

    def do_show(self, line):
        """ Prints str representation of an instance """
        if not ():
            print("** class name missing **")
        else:
            input_line = line.split()
            if len(input_line) != 2:
                print("** instance id missing **")
            elif input_line[0] not in classes:
                print("** class doesn't exist **")
            else:
                for k, v in storage.all().items():
                    if input_line[1] == v.id:
                        print(v)
                        return
                print("** no instance found **")

    def do_destroy(self, line):
        """ Deletes an instance based on the class name and id """
        input_line = input_line.split()
        if not input_line:
            print("** class name missing **")
            return
        elif len(input_line) < 2:
            print("** instance id missing **")
            return
        if input_line[0] not in classes:
            print("** class doesn't exist **")
            return
        for k, v in storage.all().items():
            if line[1] == v.id:
                del storage.all()[k]
                storage.save()
                return
        print("** no instance found **")

    def do_all(self, line):
        """Prints all string representation of all instances.
        """
        if input_line != "":
            Entry = line_data.split(' ')
            if Entry[0] not in storage.classes():
                print("** class doesn't exist **")
            else:
                nl = [str(obj) for Entry, obj in storage.all().items()
                      if type(obj).__name__ == content[0]]
                print(nl)
        else:
            nlist = [str(obj) for Entry, obj in storage.all().items()]
            print(nlist)

    def do_update(self, line):
        """ Updates an instance based on the class name and id """
        input_line = input_line.split()
        if len(input_line) == 0:
            print("** class name missing **")
            return False
        if input_line[0] in classes:
            if len(input_line) > 1:
                Entry = input_line[0] + '.' + input_line[1]
                if Entry in storage.all():
                    if len(input_line) > 2:
                        if len(input_line) > 3:
                            setattr(storage.all()[Entry], input_line[2], input_line[3])
                            storage.all()[Entry].save()
                        else:
                            print("** value missing **")
                    else:
                        print("** attribute name missing **")
                else:
                    print("** no instance found **")
            else:
                print("** instance id missing **")
        else:
            print("** class doesn't exist **")


if __name__ == '__main__':
    HBNBCommand().cmdloop()
