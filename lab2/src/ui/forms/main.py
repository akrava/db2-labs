import npyscreen


class MainForm(npyscreen.FormBaseNew):
    def create(self):
        y, x = self.useable_space()
        self.add(npyscreen.TitleDateCombo, name="Date:", max_width=x // 2)
        obj = [1, 2]
        self.add(npyscreen.TitleMultiSelect, relx=x // 2 + 1, rely=2, value=obj, name="Pick Several", values=["Option1", "Option2", "Option3"], scroll_exit=True)
        self.add(npyscreen.TitleFilename, name="Filename:", rely=-5)
