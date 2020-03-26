import npyscreen


class ListItemBox(npyscreen.BoxTitle):
    def when_value_edited(self):
        index = self.value
        if index is not None:
            message = self.values[index]
            npyscreen.notify_confirm(message, title="Content")
