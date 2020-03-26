import npyscreen


class MessageContentBox(npyscreen.BoxTitle):
    _contained_widget = npyscreen.MultiLineEdit

    def when_value_edited(self):
        self.footer = "Characters: %i" % len(self.value)
