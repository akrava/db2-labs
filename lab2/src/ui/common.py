import signal
import sys
import npyscreen
from ui.forms.user import UserForm
from ui.forms.admin import AdminForm
from ui.forms.login import LoginForm
from rs.controller.clients import Clients


class App(npyscreen.StandardApp):
    STARTING_FORM = "LOGIN"

    def __init__(self):
        super().__init__()
        signal.signal(signal.SIGINT, self.__handle_interrupt_event)
        self.__program_name = " | Lab 2"
        self.client_controller = Clients()
        self.current_username = None

    def onStart(self):
        self.addForm("USER", UserForm, name="Your chat" + self.__program_name)
        self.addForm("ADMIN", AdminForm, name="Admin dashboard" + self.__program_name)
        self.addForm("LOGIN", LoginForm, name="Login" + self.__program_name)

    def __handle_interrupt_event(self, _sig, _frame):
        self.onCleanExit()
        sys.exit(0)
