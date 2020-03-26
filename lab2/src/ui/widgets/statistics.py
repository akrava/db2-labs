import npyscreen
import weakref


class UserMessagesStatistics(npyscreen.BoxTitle):
    _contained_widget = npyscreen.MultiSelect

    def __init__(self, screen, contained_widget_arguments=None, *args, **keywords):
        self.__options_changed = contained_widget_arguments['handler']
        self._my_widgets = []
        super().__init__(screen, contained_widget_arguments, *args, **keywords)
        self.entry_widget = weakref.proxy(self._my_widgets[1])

    def make_contained_widget(self, contained_widget_arguments=None):
        _rel_y = self.rely + 1
        _rel_x = self.relx + 2
        self._my_widgets.append(npyscreen.MultiLineEdit(self.parent,
                                                        rely=_rel_y, relx=_rel_x,
                                                        width=self.width - 4,
                                                        height=4,
                                                        value="To count your messages,\nselect categories:"
                                                        ))
        self._my_widgets.append(self._contained_widget(self.parent,
                                                       rely=_rel_y + 2, relx=_rel_x,
                                                       width=self.width - 4, height=self.height - 5,
                                                       **contained_widget_arguments
                                                       ))
        self._my_widgets.append(npyscreen.MultiLineEdit(self.parent,
                                                        rely=_rel_y + self.height - 3, relx=_rel_x,
                                                        width=self.width - 4,
                                                        height=1,
                                                        value="Total: 0"
                                                        ))
        self.entry_widget = weakref.proxy(self._my_widgets[1])
        self._my_widgets[1].when_value_edited = self.when_value_edited

    def when_value_edited(self):
        selected_indexes = self.value
        count = self.__options_changed(selected_indexes)
        self._my_widgets[2].value = "Total: %i" % count
        self._my_widgets[2].update()
