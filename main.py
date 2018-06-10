from tkinter import *
from tkinter.ttk import *

from lib.widgets import HorizontalScale, LabelWidgetFrame


class ComponentSettings(Frame):
    @staticmethod
    def say_hi():
        print("hi there, everyone!")

    @staticmethod
    def _btn_light_mode_options():
        ComponentSettings.say_hi()

    def _btn_save(self):
        pass

    def _btn_reset(self):
        pass

    def __init__(self, master=None):
        Frame.__init__(self, master)
        light_modes = ['rgb spectrum', 'static', 'temp']
        fan_modes = ['static', 'temp']

        self.brightness_frame = LabelWidgetFrame(self, 'Brightness', HorizontalScale, from_=0, to=100)
        self.light_mode_frame = LabelWidgetFrame(self, 'Light Mode', Combobox, values=light_modes)
        self.light_mode_options_frame = LabelWidgetFrame(self, '', Button, text='Light mode Options', command=self._btn_light_mode_options)
        self.light_speed_frame = LabelWidgetFrame(self, 'Light Speed (seconds)', Entry)
        self.fan_mode_frame = LabelWidgetFrame(self, 'Fan Mode', Combobox, values=fan_modes)
        self.fan_speed_frame = LabelWidgetFrame(self, 'Fan Speed', HorizontalScale, from_=0, to=100)

        Button(self, text='Exit', command=self.quit).pack(side='right')
        Button(self, text='Reset', command=self._btn_reset).pack(side='right')
        Button(self, text='Save', command=self._btn_save).pack(side='right')

        self.pack()

root = Tk()

hello = ComponentSettings.say_hi

menu = {
    'File': [{'Open': hello}, {'Save': hello}, {'Exit': hello}],
    'Edit': [{'Cut': hello}, {'Copy': hello}, {'Paste': hello}],
    'Help':[{'About': hello}]
}

menubar = Menu(root)
for menu_label, submenus in menu.items():
    menu = Menu(menubar, tearoff=0)
    for submenu in submenus:
        for label, func in submenu.items():
            menu.add_command(label=label, command=func)
    menubar.add_cascade(label=menu_label, menu=menu)

# display the menu
root.config(menu=menubar)

app = ComponentSettings(master=root)
app.mainloop()
root.destroy()
