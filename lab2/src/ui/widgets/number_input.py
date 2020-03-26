import npyscreen


class NumberInput(npyscreen.TitleText):
    def __init__(self, screen, handler_update, **keywords):
        super().__init__(screen, **keywords)
        self.__handler_update = handler_update

    def when_value_edited(self):
        try:
            val = int(self.value)
            if val <= 0:
                raise Exception("Should be > 0")
        except Exception as e:
            npyscreen.notify_confirm("Please, input only number: %s. Set to 5 as default" % str(e), title="Error")
            self.value = "5"
        self.__handler_update(True)
