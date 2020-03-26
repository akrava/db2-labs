import npyscreen
from rs.controller.clients import Clients


class LoginForm(npyscreen.FormBaseNew):
    __username = None
    y, x = 0, 0

    def create(self):
        y, x = self.useable_space()
        self.add(npyscreen.FixedText, value="To login, please enter your username".center(self.columns - 2),
                 editable=False, rely=y // 2 - 4)
        self.add(npyscreen.FixedText, value="If user with such username is not exist, we will register it"
                 .center(self.columns - 2), editable=False)
        self.__username = self.add(npyscreen.TitleText, begin_entry_at=12, name="Username:",
                                   relx=x // 2 - 20, rely=y // 2)
        button = self.add(npyscreen.ButtonPress, name='Login', relx=x // 2 - 2, rely=y // 2 + 3)
        self.add(npyscreen.FixedText, value="To exit press CTRL + C. To move use TAB. To select press ENTER"
                 .center(self.columns - 2), editable=False, rely=y - 3)
        button.whenPressed = self.on_login

    def on_login(self):
        client_controller: Clients = self.parentApp.client_controller
        username = self.__username.value
        if not Clients.validate_username(username):
            npyscreen.notify_confirm("Username is not valid: use only `a-zA-Z0-9_`, "
                                     "minimal length is 4", title='Error')
            return

        result = client_controller.login_client(username)
        if result is None:
            message_to_display = "Such client with username `%s` hasn't been registered yet. " \
                                 "We will register you with such username. If you want to be a " \
                                 "regular user, proceed with `No`, if you want to be admin - " \
                                 "choose `Yes`" % username
            register_as_admin = npyscreen.notify_yes_no(message_to_display, title='Registration')
            try:
                client_controller.register_client(username, register_as_admin)
            except Exception as e:
                npyscreen.notify_confirm('Error occurred: %s' % str(e), title='Error')
                return
            npyscreen.notify_confirm('Successfully registered %s with username `%s`' %
                                     ('admin' if register_as_admin else 'user', username), title='Result')
            result = register_as_admin

        if result is True:
            self.parentApp.switchForm("ADMIN")
        else:
            self.parentApp.current_username = username
            self.parentApp.getForm('USER').username_was_set_hook(username)
            self.parentApp.switchForm("USER")
