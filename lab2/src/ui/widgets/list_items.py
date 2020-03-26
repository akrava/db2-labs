import npyscreen


class ListItemBox(npyscreen.BoxTitle):
    def when_value_edited(self):
        index = self.value
        if index is not None and 0 <= index < len(self.values):
            message = self.values[index]
            npyscreen.notify_confirm(str(message), title="Content")
