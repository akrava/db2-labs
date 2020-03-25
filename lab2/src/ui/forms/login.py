import npyscreen


class LoginForm(npyscreen.FormBaseNew):
    __username = None

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
        username = self.__username.value
        self.parentApp.switchForm("MAIN")
