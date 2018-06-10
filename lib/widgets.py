from tkinter import *
from tkinter.ttk import *


class HorizontalScale(LabeledScale):
    orient = HORIZONTAL


class LabelWidgetFrame(Frame):
    def __init__(self, master, _text, widget, **kwargs):
        Frame.__init__(self, master)
        Label(self, text=_text).pack(side='left')

        self.contained_widget = widget(self, **kwargs)

        self.contained_widget.pack(side='right', fill=BOTH, expand=1)
        self.pack(fill=BOTH)

