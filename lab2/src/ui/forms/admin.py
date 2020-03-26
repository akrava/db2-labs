import npyscreen
from ui.widgets.list_items import ListItemBox
from ui.widgets.number_input import NumberInput
from rs.wrappers.pub_sub import PubSub
from rs.settings import JOURNAL_ACTIVITIES_NAME


class AdminForm(npyscreen.FormBaseNew):
    __journal_pub_sub = PubSub(JOURNAL_ACTIVITIES_NAME)

    def create(self):
        self.__draw_journal()
        self.__draw_users_online()
        self.__draw_n_input()
        self.__draw_users_rate()
        self.__draw_spamers()
        self.__journal_pub_sub.subscribe()
        self.__draw_values(True)

    def __draw_journal(self):
        y, x = self.useable_space()
        self.__journal = self.add(ListItemBox, name="Journal activities", relx=1,
                                  width=x // 2 - 1, rely=1, height=y // 2 - 1)

    def __draw_users_online(self):
        y, x = self.useable_space()
        self.__users_online = self.add(ListItemBox, name="Users online", relx=1,
                                       width=x // 2 - 1, rely=y // 2, height=y // 2 - 1)

    def __draw_n_input(self):
        y, x = self.useable_space()
        self.__n = self.add(NumberInput, handler_update=self.__draw_values, value="5", begin_entry_at=12,
                            name="Enter N:", rely=1, relx=x // 2 + 3)

    def __draw_users_rate(self):
        y, x = self.useable_space()
        self.__users_rate = self.add(ListItemBox, name="Rate of N active senders", relx=x // 2,
                                     width=x // 2, rely=2, height=y // 2 - 2)

    def __draw_spamers(self):
        y, x = self.useable_space()
        self.__spamers_rate = self.add(ListItemBox, name="Rate of N active spamers", relx=x // 2,
                                       width=x // 2 - 1, rely=y // 2, height=y // 2 - 1)

    def while_waiting(self):
        self.__draw_values()

    def __draw_values(self, init: bool = False):
        if self.__read_all_messages_in_journal_and_display() or init:
            self.__users_online.values = self.parentApp.client_controller.get_all_users_online()
            self.__users_online.footer = "Total users: %i" % len(self.__users_online.values)
            self.__users_online.update()

            self.__users_rate.values = self.parentApp.client_controller.get_active_users(int(self.__n.value))
            self.__users_rate.update()

            self.__spamers_rate.values = self.parentApp.client_controller.get_active_spamers(int(self.__n.value))
            self.__spamers_rate.update()

    def __read_all_messages_in_journal_and_display(self):
        messages = []
        message = self.__journal_pub_sub.get_message()
        while message is not None:
            messages.append(message)
            message = self.__journal_pub_sub.get_message()
        if len(messages) == 0:
            return False
        for x in messages:
            if isinstance(x['data'], bytes):
                self.__journal.values.append(x['data'].decode("utf-8"))
        self.__journal.footer = "Total messages: %i" % len(self.__journal.values)
        self.__journal.update()
        return True
