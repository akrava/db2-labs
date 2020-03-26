import npyscreen
from ui.widgets.list_items import ListItemBox
from ui.widgets.message_content import MessageContentBox
from ui.widgets.statistics import UserMessagesStatistics


class UserForm(npyscreen.FormBaseNew):
    __statistics_width = 30
    __new_message_height = 12

    def create(self):
        self.__draw_messages_box()
        self.__draw_statistics_box()
        self.__new_message_box()

    def __draw_statistics_box(self):
        y, x = self.useable_space()
        self.__statistics = self.add(UserMessagesStatistics, name="Statistics", relx=x - self.__statistics_width - 1,
                                     width=self.__statistics_width, rely=1, height=y - self.__new_message_height,
                                     footer="Press x to select",
                                     contained_widget_arguments={
                                         "values": ["created", "in queue", "processing", "blocked", "send",
                                                    "delivered"],
                                         "handler": self.handle_statistics},
                                     )

    def __draw_messages_box(self):
        y, x = self.useable_space()
        self.__messages = self.add(ListItemBox, name="Messages", relx=1,
                                   width=x - self.__statistics_width - 2, rely=1,
                                   height=y - self.__new_message_height)

    def __new_message_box(self):
        y, x = self.useable_space()
        self.__message_writer = self.add(MessageContentBox, name="New message content", relx=1,
                                         width=x - self.__statistics_width - 2,
                                         rely=y - self.__new_message_height + 1, height=self.__new_message_height - 5,
                                         contained_widget_arguments={"scroll_exit": False}, footer="Characters: 0")
        self.__all_users = self.add(npyscreen.BoxTitle, name="Recipient", relx=x - self.__statistics_width - 1,
                                    width=self.__statistics_width, rely=y - self.__new_message_height + 1,
                                    height=self.__new_message_height - 5)
        button = self.add(npyscreen.ButtonPress, name='Send message'.center(30), relx=x // 2 - 15, rely=y - 3)
        button.whenPressed = self.__send_message

    def __send_message(self):
        username = self.parentApp.current_username
        if self.__all_users.value is None:
            npyscreen.notify_confirm("Please, select receiver", title="Error")
            return
        dest = self.__all_users.values[self.__all_users.value]
        message = self.__message_writer.value
        try:
            self.parentApp.message_controller.send_message(message, username, dest)
        except Exception as e:
            npyscreen.notify_confirm(str(e), title="Error")
            return
        npyscreen.notify_confirm("Successfully send in queue", title="Success")
        self.__message_writer.value = ""
        self.__all_users.value = None
        self.__message_writer.update()
        self.__message_writer.footer = "Characters: 0"
        self.__all_users.update()

    def handle_statistics(self, options: []):
        return self.parentApp.message_controller.count_messages_by_statuses(self.parentApp.current_username, options)

    def username_was_set_hook(self, username: str):
        self.__filter_users_on_user_form(username)
        self.__load_messages(username)

    def __load_messages(self, username: str):
        self.__messages.values = self.parentApp.message_controller.read_messages(username)
        self.__messages.footer = "Total messages: %i" % len(self.__messages.values)

    def __filter_users_on_user_form(self, username: str):
        self.__all_users.values = [username for username in self.parentApp.client_controller.get_all_users()]
        list_users = [user for user in self.__all_users.values if user != username]
        self.__all_users.values = list_users
        self.__all_users.footer = "Total users: %i" % len(list_users)
