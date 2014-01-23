from cmd import Cmd

from .cmdexit import ExitCmd

class MetArticlesCLI(ExitCmd):

    def do_add(self, s):
        print("NOT IMPLEMENTED")

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