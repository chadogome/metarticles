from cmd import Cmd

class AddCmd(Cmd,object):
    
    def do_add(self, s):
        return True
    
    def help_add(self):
        print("Add a new concept in the database.")
        