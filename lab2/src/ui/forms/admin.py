import npyscreen
from ui.forms.list_items import ListItemBox


class AdminForm(npyscreen.FormBaseNew):
    def create(self):
        self.__draw_journal()
        self.__draw_users_online()
        self.__draw_n_input()
        self.__draw_users_rate()
        self.__draw_spamers()

    def __draw_journal(self):
        y, x = self.useable_space()
        box = self.add(ListItemBox, name="Journal activities", relx=1,
                       width=x // 2 - 1, rely=1, height=y // 2 - 1)
        box.values = ["Hello", "This is a Test", "This is another test", "And here is another line",
                      "asdjasd fasdfdfajsd as dfgasjdfgashfdgasdjfasdfafa  fasdfgdf adfa sdf sdf asdf dfadfas fasd fa df adf asdfa sfadf adfasdfasdf asdf asdfasdfasdf asdf asf asd "]
        box.footer = "Total messages: %i" % len(box.values)

    def __draw_users_online(self):
        y, x = self.useable_space()
        box = self.add(ListItemBox, name="Users online", relx=1,
                       width=x // 2 - 1, rely=y // 2, height=y // 2 - 1)
        box.values = ["Hello", "This is a Test", "This is another test", "And here is another line",
                      "asdjasd fasdfdfajsd as dfgasjdfgashfdgasdjfasdfafa  fasdfgdf adfa sdf sdf asdf dfadfas fasd fa df adf asdfa sfadf adfasdfasdf asdf asdfasdfasdf asdf asf asd "]
        box.footer = "Total users: %i" % len(box.values)

    def __draw_n_input(self):
        y, x = self.useable_space()
        self.__n = self.add(npyscreen.TitleText, begin_entry_at=12, name="Enter N:", rely=1, relx=x // 2 + 3)

    def __draw_users_rate(self):
        y, x = self.useable_space()
        box = self.add(ListItemBox, name="Rate of N active senders", relx=x // 2,
                       width=x // 2, rely=2, height=y // 2 - 2)
        box.values = ["Hello", "This is a Test", "This is another test", "And here is another line",
                      "asdjasd fasdfdfajsd as dfgasjdfgashfdgasdjfasdfafa  fasdfgdf adfa sdf sdf asdf dfadfas fasd fa df adf asdfa sfadf adfasdfasdf asdf asdfasdfasdf asdf asf asd "]

    def __draw_spamers(self):
        y, x = self.useable_space()
        box = self.add(ListItemBox, name="Rate of N active spamers", relx=x // 2,
                       width=x // 2 - 1, rely=y // 2, height=y // 2 - 1)
        box.values = ["Hello", "This is a Test", "This is another test", "And here is another line",
                      "asdjasd fasdfdfajsd as dfgasjdfgashfdgasdjfasdfafa  fasdfgdf adfa sdf sdf asdf dfadfas fasd fa df adf asdfa sfadf adfasdfasdf asdf asdfasdfasdf asdf asf asd "]
