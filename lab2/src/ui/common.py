import signal
import sys
import npyscreen
from ui.forms.main import MainForm
from ui.forms.login import LoginForm


class App(npyscreen.StandardApp):
    STARTING_FORM = "LOGIN"

    def __init__(self):
        super().__init__()
        signal.signal(signal.SIGINT, self.__handle_interrupt_event)
        self.__program_name = " | Lab 2"

    def onStart(self):
        self.addForm("MAIN", MainForm, name="Main" + self.__program_name)
        self.addForm("LOGIN", LoginForm, name="Login" + self.__program_name)

    def __handle_interrupt_event(self, _sig, _frame):
        self.onCleanExit()
        sys.exit(0)
