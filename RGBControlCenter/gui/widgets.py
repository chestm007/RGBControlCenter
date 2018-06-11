"""
RGBControlCenter
GUI frontend for linux_thermaltake_rgb
Copyright (C) 2018  Max Chesterfield (chestm007@hotmail.com)

This program is free software; you can redistribute it and/or
modify it under the terms of the GNU General Public License
as published by the Free Software Foundation; either version 2
of the License, or (at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program; if not, write to the Free Software
Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston, MA  02110-1301, USA.
"""
from tkinter import *
from tkinter.ttk import *


class HorizontalScale(LabeledScale):
    orient = HORIZONTAL

    def __init__(self, *args, **kwargs):
        self._var = IntVar()
        super(HorizontalScale, self).__init__(variable=self._var, *args, **kwargs)

    def get(self):
        return self._var.get()


class LabelWidgetFrame(Frame):
    def __init__(self, master, _text, widget, **kwargs):
        Frame.__init__(self, master)
        Label(self, text=_text).pack(side='left')

        self.contained_widget = widget(self, **kwargs)

        self.contained_widget.pack(side='right', fill=BOTH, expand=1)
        self.pack(fill=BOTH)

    def get(self):
        return self.contained_widget.get()

