#!/usr/bin/python3
"""This is the console for AirBnB"""
import re
import cmd
import json
from models.base_model import BaseModel
from models import storage 
from models.user import User
from models.state import State
from models.city import City
from models.place import Place
from models.amenity import Amenity
from models.review import Review



class HBNBCommand(cmd.Cmd):
    """this class is entry point of the command interpreter"""
    prompt = "(hbnb) "


    def emptyline(self):
        """Ignores empty spaces"""
        pass

    def do_quit(self, line):
        """Quit command to exit the program"""
        return True

    def do_EOF(self, line):
        """Quit command to exit the program at end of file"""
        return True

    def do_create(self, line):
        """Creates an instance.
        """
        if input_line == "" or input_line is None:
            print("** class name missing **")
        elif input_line not in storage.classes():
            print("** class doesn't exist **")
        else:
            b = storage.classes()[input_line]()
            b.save()
            print(b.id)

    def do_show(self, line):
        """Prints the string representation of an instance
        Exceptions:
            SyntaxError: when there is no args given
            NameError: when there is no object taht has the name
            IndexError: when there is no id given
            KeyError: when there is no valid id given
        """
        if line == "" or line is None:
            print("** class name missing **")
        else:
            words = line.split(' ')
            if words[0] not in storage.classes():
                print("** class doesn't exist **")
            elif len(words) < 2:
                print("** instance id missing **")
            else:
                Entry = "{}.{}".format(words[0], words[1])
                if Entry not in storage.all():
                    print("** no instance found **")
                else:
                    print(storage.all()[Entry])

    def do_destroy(self, line):
        """Deletes an instance based on the class name and id
        Exceptions:
            SyntaxError: when there is no args given
            NameError: when there is no object taht has the name
            IndexError: when there is no id given
            KeyError: when there is no valid id given
        """
        try:
            if not line:
                raise SyntaxError()
            input_line = line.split(" ")
            if input_line[0] not in self.all_classes:
                raise NameError()
            if len(input_line) < 2:
                raise IndexError()
            objects = storage.all()
            Entry = input_line[0] + '.' + input_line[1]
            if Entry in objects:
                del objects[Entry]
                storage.save()
            else:
                raise KeyError()
        except SyntaxError:
            print("** class name missing **")
        except NameError:
            print("** class doesn't exist **")
        except IndexError:
            print("** instance id missing **")
        except KeyError:
            print("** no instance found **")

    def do_all(self, line):
        """Prints all string representation of all instances
        Exceptions:
            NameError: when there is no object taht has the name
        """
        if line:
            args = line.split(" ")
            if args[0] not in self.all_classes:
                print("** class doesn't exist **")
                return
            objects = storage.all(line)
        input_line = []
        if not line:
            objects = storage.all()
            for Entry in objects:
                input_line.append(objects[Entry])
            print(input_line)
            return
        # try:
            # args = line.split(" ")
            # if args[0] not in self.all_classes:
            #     raise NameError()
        for Entry in objects:
            name = Entry.split('.')
            if name[0] == args[0]:
                input_line.append(objects[Entry])
        print(input_line)
        # except NameError:
        #     print("** class doesn't exist **")

    def do_update(self, line):
        """Updates an instance by adding or updating attribute
        Exceptions:
            SyntaxError: when there is no args given
            NameError: when there is no object taht has the name
            IndexError: when there is no id given
            KeyError: when there is no valid id given
            AttributeError: when there is no attribute given
            ValueError: when there is no value given
        """
        try:
            if not line:
                raise SyntaxError()
            input_line = split(line, " ")
            if input_line[0] not in self.all_classes:
                raise NameError()
            if len(input_line) < 2:
                raise IndexError()
            objects = storage.all()
            Entry = input_line[0] + '.' + input_line[1]
            if Entry not in objects:
                raise KeyError()
            if len(input_line) < 3:
                raise AttributeError()
            if len(input_line) < 4:
                raise ValueError()
            v = objects[Entry]
            try:
                v.__dict__[input_line[2]] = eval(input_line[3])
            except Exception:
                v.__dict__[input_line[2]] = input_line[3]
                v.save()
        except SyntaxError:
            print("** class name missing **")
        except NameError:
            print("** class doesn't exist **")
        except IndexError:
            print("** instance id missing **")
        except KeyError:
            print("** no instance found **")
        except AttributeError:
            print("** attribute name missing **")
        except ValueError:
            print("** value missing **")


if __name__ == '__main__':
    HBNBCommand().cmdloop()            
