from cmd import Cmd

class ExitCmd(Cmd,object):
    
    def can_exit(self):
        return True
    
    def onecmd(self, line):
        r = super (ExitCmd, self).onecmd(line)
        if r and (self.can_exit() or
           raw_input('exit anyway ? (yes/no):')=='yes'):
             return True
        return False
    
    def do_exit(self, s):
        return True
    
    def help_exit(self):
        print("Exit MetArticles and go back to the shell.")
        print("You can also use the Ctrl-D shortcut.")
    
    do_EOF = do_exit
    help_EOF= help_exit