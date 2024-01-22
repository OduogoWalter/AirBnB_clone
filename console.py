#!/usr/bin/python3

import cmd
from models import storage
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review


class HBNBCommand(cmd.Cmd):
    prompt = '(hbnb) '

    def do_create(self, args):
        """Creates a new instance of BaseModel"""
        args = args.split()
        if not args:
            print("** class name missing **")
            return
        class_name = args[0]
        if class_name not in ["BaseModel", "State",
                              "City", "Amenity", "Place", "Review"]:
            print("** class doesn't exist **")
            return
        new_instance = eval(class_name)()
        new_instance.save()
        print(new_instance.id)

    def do_show(self, args):
        """Prints the string representation of an instance"""
        args = args.split()
        if not args:
            print("** class name missing **")
            return
        if args[0] not in ["BaseModel", "State",
                           "City", "Amenity", "Place", "Review"]:
            print("** class doesn't exist **")
            return
        if len(args) < 2:
            print("** instance id missing **")
            return
        key = "{}.{}".format(args[0], args[1])
        all_objs = storage.all()
        if key in all_objs:
            print(all_objs[key])
        else:
            print("** no instance found **")

    def emptyline(self):
        """Called when an empty line is entered"""
        pass

    def do_quit(self, arg):
        """Quit command to exit the program"""
        return True

    def do_EOF(self, arg):
        """EOF command to exit the program"""
        print("")
        return True

    def do_all(self, args):
        """Prints all string representation
        of all instances based on the class name"""
        args = args.split()
        if not args:
            print("** class name missing **")
            return
        class_name = args[0]
        if class_name not in ["BaseModel", "State",
                              "City", "Amenity",
                              "Place", "Review", "User"]:
            print("** class doesn't exist **")
            return
        all_instances = storage.all().values()
        class_instances = [str(obj) for obj in
                           all_instances if
                           type(obj).__name__ == class_name]
        print(class_instances)

    def do_count(self, args):
        """Retrieve the number of instances of a class"""
        args = args.split()
        if not args:
            print("** class name missing **")
            return
        class_name = args[0]
        if class_name not in ["BaseModel", "State",
                              "City", "Amenity",
                              "Place", "Review", "User"]:
            print("** class doesn't exist **")
            return
        all_instances = storage.all().values()
        class_count = len([obj for obj
                           in all_instances if
                           type(obj).__name__ == class_name])
        print(class_count)

    def do_destroy(self, args):
        """Destroy instance based on ID"""
        args = args.split()
        if not args:
            print("** class name missing **")
            return
        class_name = args[0]
        if class_name not in ["BaseModel",
                              "State", "City", "Amenity",
                              "Place", "Review", "User"]:
            print("** class doesn't exist **")
            return
        if len(args) < 2:
            print("** instance id missing **")
            return
        instance_id = args[1]
        key = "{}.{}".format(class_name, instance_id)
        all_instances = storage.all()
        instance = all_instances.get(key, None)
        if instance:
            del all_instances[key]
            storage.save()
        else:
            print("** no instance found **")

    def do_update(self, args):
        """Update instance based on ID with a dictionary"""
        args = args.split()
        if not args:
            print("** class name missing **")
            return
        class_name = args[0]
        if class_name not in ["BaseModel", "State", "City", "Amenity", "Place", "Review", "User"]:
            print("** class doesn't exist **")
            return
        if len(args) < 2:
            print("** instance id missing **")
            return
        instance_id = args[1]
        key = "{}.{}".format(class_name, instance_id)
        all_instances = storage.all()
        instance = all_instances.get(key, None)
        if instance:
            if len(args) < 3:
                print("** dictionary missing **")
                return
            try:
                dictionary = eval(args[2])
            except:
                print("** invalid dictionary **")
                return
            if not isinstance(dictionary, dict):
                print("** invalid dictionary **")
                return
            for key, value in dictionary.items():
                setattr(instance, key, value)
            instance.save()
        else:
            print("** no instance found **")


if __name__ == '__main__':
    HBNBCommand().cmdloop()
