import cmd

class HBNBCommand(cmd.Cmd):
    """
    Command interpreter for the HBNB project.
    """
    prompt = '(hbnb) '

    def do_quit(self, args):
        """Quit command to exit the program"""
        print("Goodbye!")
        return True

    def do_EOF(self, args):
        """EOF command to exit the program"""
        print("Goodbye!")
        return True

    def emptyline(self):
        """Called when an empty line is entered in response to the prompt"""
        pass

if __name__ == '__main__':
    HBNBCommand().cmdloop()
