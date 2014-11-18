from cmd import Cmd

from .cmdexit import ExitCmd
import db_operations

class MetArticlesCLI(ExitCmd):

    def do_add(self, s):
        while s.lower() not in ["n", "r"]:
            s = input("Add a (N)ode or (R)elation? ")
        if s.lower() == "n":
            node_data = {}
            name = None
            while name is None:
                name = input("Name: ")
            node_data['name'] = name
            print("Input property names and values, empty name to end.")
            property_name = None
            while property_name is None:
                property_name = input("Property name: ").lower()
                if property_name != "":
                    property_value = None
                    while property_value is None:
                        property_value = input(property_name + " value: ")
                    node_data[property_name] = property_value
                    property_name = None
            db_operations.add_node(node_data)

    def help_add(self):
        print("Add a new concept in the database.")

    def do_read(self, s):
        print("NOT IMPLEMENTED")

    def help_read(self):
        print("Display the information about a concept.")

    def do_search(self, s):
        print("NOT IMPLEMENTED")

    def help_search(self):
        print("Search the database for a concept.")

    def do_delete(self, s):
        print("NOT IMPLEMENTED")

    def help_delete(self):
        print("Delete a concept from the database.")