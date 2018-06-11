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

from RGBControlCenter.gui.widgets import LabelWidgetFrame, HorizontalScale


class FanOptionsWindow(Toplevel):
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
    def build_options(fan_mode, settings_class):
        print(fan_mode)
        if fan_mode == 'locked_speed':
            cls = LockedSpeedFanOptionsWindow

        elif fan_mode == 'temp_target':
            cls = TempTargetFanOptionsWindow

        return cls(settings_class)


class LockedSpeedFanOptionsWindow(FanOptionsWindow):
    def _populate_window(self):
        self.fan_speed_frame = LabelWidgetFrame(
            self.contained_frame, 'Fan Speed', HorizontalScale, from_=0, to=100)

    def _read_frame_settings(self):
        self.settings_class.fan_options = {'speed': self.fan_speed_frame.get()}


class TempTargetFanOptionsWindow(FanOptionsWindow):
    def _populate_window(self):
        self.target = LabelWidgetFrame(
            self.contained_frame, 'Temp Target', HorizontalScale, from_=0, to=100)

        self.sensor = LabelWidgetFrame(self.contained_frame, 'Sensor', Entry)

    def _read_frame_settings(self):
        self.settings_class.fan_options = {
            'target': self.target.get(),
            'sensor': self.sensor.get()
        }

