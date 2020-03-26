import npyscreen
from ui.forms.list_items import ListItemBox
from ui.forms.message_content import MessageContentBox
from ui.forms.statistics import UserMessagesStatistics


class UserForm(npyscreen.FormBaseNew):
    __statistics_width = 30
    __new_message_height = 12

    def create(self):
        self.__draw_messages_box()
        self.__draw_statistics_box()
        self.__new_message_box()

    def __draw_statistics_box(self):
        y, x = self.useable_space()
        self.add(UserMessagesStatistics, name="Statistics", relx=x - self.__statistics_width - 1,
                 width=self.__statistics_width, rely=1, height=y - self.__new_message_height,
                 footer="Press x to select",
                 contained_widget_arguments={"values": ["Option1", "Option2", "Option3", "Option4", "Option5", "Option6"]})

    def __draw_messages_box(self):
        y, x = self.useable_space()
        box = self.add(ListItemBox, name="Messages", relx=1,
                       width=x - self.__statistics_width - 2, rely=1,
                       height=y - self.__new_message_height)
        box.values = ["Hello", "This is a Test", "This is another test", "And here is another line", "asdjasd fasdfdfajsd as dfgasjdfgashfdgasdjfasdfafa  fasdfgdf adfa sdf sdf asdf dfadfas fasd fa df adf asdfa sfadf adfasdfasdf asdf asdfasdfasdf asdf asf asd " ]
        box.footer = "Total messages: %i" % len(box.values)

    def __new_message_box(self):
        y, x = self.useable_space()
        self.add(MessageContentBox, name="New message content", relx=1, width=x - self.__statistics_width - 2,
                 rely=y - self.__new_message_height + 1, height=self.__new_message_height - 5,
                 contained_widget_arguments={"scroll_exit": False}, footer="Characters: 0")
        box = self.add(npyscreen.BoxTitle, name="Recipient", relx=x - self.__statistics_width - 1,
                       width=self.__statistics_width, rely=y - self.__new_message_height + 1,
                       height=self.__new_message_height - 5)
        box.values = ["Hello", "This is a Test", "This is another test", "And here is another line"]
        box.footer = "Total users: %i" % len(box.values)
        button = self.add(npyscreen.ButtonPress, name='Send message'.center(30), relx=x // 2 - 15, rely=y - 3)
        button.whenPressed = self.__send_message

    def __send_message(self):
        pass
