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

from RGBControlCenter.gui.widgets import LabelWidgetFrame


class LightOptionsWindow(Toplevel):
    def __init__(self, settings_class):
        Toplevel.__init__(self)
        self.settings_class = settings_class
        self.contained_frame = Frame(self)
        self.contained_frame.pack()
        self._populate_window()
        self._add_buttons()

    def _btn_ok(self):
        self._read_frame_settings()
        self.destroy()

    def _read_frame_settings(self):
        raise NotImplementedError()

    def _populate_window(self):
        raise NotImplementedError()

    def _add_buttons(self):
        Button(self.contained_frame, text='Exit', command=self.destroy).pack(side='right')
        Button(self.contained_frame, text='Ok', command=self._btn_ok).pack(side='right')

    @staticmethod
    def build_options(light_mode, settings_class):
        print(light_mode)
        if light_mode == 'temperature':
            cls = TemperatureLightOptionsWindow

        elif light_mode == 'static':
            cls = StaticLightOptionsWindow

        elif light_mode == 'alternating':
            cls = AlternatingLightOptionsWindow
        else:
            return

        return cls(settings_class)


class TemperatureLightOptionsWindow(LightOptionsWindow):
    def _read_frame_settings(self):
        self.settings_class.light_options = {'sensor': self.sensor_frame.get(),
                                             'hot': self.hot_temp.get(),
                                             'target': self.target_temp.get(),
                                             'cold': self.cold_temp.get()}

    def _populate_window(self):
        self.sensor_frame = LabelWidgetFrame(self.contained_frame, 'Temperature Sensor', Entry)
        self.hot_temp = LabelWidgetFrame(self.contained_frame, 'Hot Temp', Entry)
        self.target_temp = LabelWidgetFrame(self.contained_frame, 'Target Temp', Entry)
        self.cold_temp = LabelWidgetFrame(self.contained_frame, 'Cold Temp', Entry)


class StaticLightOptionsWindow(LightOptionsWindow):
    def _populate_window(self):
        self.r_frame = LabelWidgetFrame(self.contained_frame, 'R', Entry)
        self.g_frame = LabelWidgetFrame(self.contained_frame, 'G', Entry)
        self.b_frame = LabelWidgetFrame(self.contained_frame, 'B', Entry)

    def _read_frame_settings(self):
        self.settings_class.light_options = {'value': [self.r_frame.get(),
                                                       self.g_frame.get(),
                                                       self.b_frame.get()]}


class AlternatingLightOptionsWindow(LightOptionsWindow):
    def _populate_window(self):
        self.even_frame = LabelFrame(self.contained_frame, text='Even')
        self.even_frame.pack()
        self.even = [LabelWidgetFrame(self.even_frame, 'R', Entry),
                     LabelWidgetFrame(self.even_frame, 'G', Entry),
                     LabelWidgetFrame(self.even_frame, 'B', Entry)]

        self.odd_frame = LabelFrame(self.contained_frame, text='Odd')
        self.odd_frame.pack()
        self.odd = [LabelWidgetFrame(self.odd_frame, 'R', Entry),
                    LabelWidgetFrame(self.odd_frame, 'G', Entry),
                    LabelWidgetFrame(self.odd_frame, 'B', Entry)]

    def _read_frame_settings(self):
        self.settings_class.light_options = {'even': [v.get() for v in self.even],
                                             'odd': [v.get() for v in self.odd]}
