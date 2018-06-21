'''
Poniżej znajduje się implementacja CLI (command line interface) do modułu
turtle, czyli Pythonowego odpowiednika LOGO. Wykorzystano tutaj wzorzec Template
Method (metoda szablonowa).

W pierwszym, obowiązkowym zadaniu, należy dodać wsparcie dla makr, tak aby można
było nagrać ciąg komend, a następnie odtworzyć ten sam ciąg przy pomocy
komendy "playback". W tym celu, należy dodać następujące komendy: 

- record -- rozpoczyna nagrywanie makra
- stop -- kończy nagrywanie makra
- playback -- wykonuje makro, tzn. wszystkie komendy po komendzie "record", aż
  do komendy "stop". 

Podpowiedź: Użyj wzorca Command (polecenie).

W drugim, nieobowiązkowym zadaniu, zastanów się, jak można zastosować wzorzec
Composite (kompozyt) do tych makr i spróbuj zastosować go.

Rozwiązania wysyłamy tak samo, jak prework, tylko że w jednym Pull Requeście.
'''

import cmd, sys
import turtle


class Command(object):
    def __init__(self, function, args):
        self.function = function
        self.args = args

    def execute(self):
        self.function(*self.args)

class TurtleShell(cmd.Cmd):
    intro = 'Welcome to the turtle shell.   Type help or ? to list commands.\n'
    prompt = '(turtle) '

    def __init__(self):
        super().__init__()
        self.macro = []
        self.recording = False

    # ----- basic turtle commands -----
    def do_forward(self, arg):
        self.run_command(Command(turtle.forward, self.parse(arg)))


    def do_right(self, arg):
        self.run_command(Command(turtle.right, self.parse(arg)))

    def do_left(self, arg):
        self.run_command(Command(turtle.left, self.parse(arg)))

    def do_home(self, arg):
        self.run_command(Command(turtle.home))

    def do_circle(self, arg):
        self.run_command(Command(turtle.circle, self.parse(arg)))

    def do_record(self, arg):
        'Start recording macro.'
        self.is_recording = True
        self.macro = []

    def do_stop(self, arg):
        'Stop recording macro.'
        self.is_recording = False

    def do_playback(self, arg):
        'Execute macro.'
        for cmd in self.macro:
            cmd.execute()

    #def do_position(self, arg):
    #    print('Current position is %d %d\n' % turtle.position())

    # def do_heading(self, arg):
    #    print('Current heading is %d\n' % (turtle.heading(),))

    def do_reset(self, arg):
        turtle.reset()

    def do_bye(self, arg):
        print('Thank you for using Turtle')
        turtle.bye()
        return

    def run_command(self, command):
        if self.is_recording:
            self.macro.append(command)
        command.execute()

    def parse(self, arg):
        return tuple(map(int, arg.split()))


if __name__ == '__main__':
    TurtleShell().cmdloop()    
