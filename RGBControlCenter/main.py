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

from RGBControlCenter.lib.dbus_client import DbusClient
from RGBControlCenter.gui.fan_options_window import FanOptionsWindow
from RGBControlCenter.gui.light_options_window import LightOptionsWindow
from RGBControlCenter.gui.widgets import HorizontalScale, LabelWidgetFrame


class ComponentSettings:
    light_options = {}
    fan_options = {}

    def __init__(self, brightness=None, lightmode=None,
                 lightspeed=None, fanmode=None):
        self.brightness=brightness
        self.lightmode=lightmode
        self.lightspeed = lightspeed
        self.fanmode = fanmode


class ComponentSettingsFrame(Frame):

    def _read_frame_settings(self):
        brightness = self.brightness_frame.get()
        lightmode = self.get_light_mode()
        lightspeed = self.light_speed_frame.get()
        fanmode = self.get_fan_mode()
        return ComponentSettings(
            brightness=brightness,
            lightmode=lightmode,
            lightspeed=lightspeed,
            fanmode=fanmode)

    def get_light_mode(self):
        return self.light_mode_frame.get()

    def get_fan_mode(self):
        return self.fan_mode_frame.get()

    @staticmethod
    def say_hi():
        print("hi there, everyone!")

    def _btn_light_mode_options(self):
        LightOptionsWindow.build_options(self.get_light_mode(), ComponentSettings)

    def _btn_fan_mode_options(self):
        FanOptionsWindow.build_options(self.get_fan_mode(), ComponentSettings)

    def _btn_save(self):
        pass

    def _btn_apply(self):
        settings = self._read_frame_settings()
        if settings.fanmode:
            self.dbus_client.set_fan_controller(settings.fanmode, **settings.fan_options)

        if settings.lightmode:
            self.dbus_client.set_lighting_controller(settings.lightmode, **settings.light_options)

        if settings.brightness:
            self.dbus_client.set_lighting_brightness(settings.brightness)

        if settings.lightspeed:
            print(settings.lightspeed)
            self.dbus_client.set_lighting_msec(settings.lightspeed)

    def __init__(self, master=None, dbus_client=None):
        assert dbus_client is not None
        assert master is not None

        self.dbus_client = dbus_client  # type: DbusClient

        Frame.__init__(self, master)
        light_modes = ['rgb_spectrum',
                       'spinning_rgb_spectrum',
                       'alternating',
                       'static',
                       'temperature']

        fan_modes = ['locked_speed',
                     'temp_target']

        self.brightness_frame = LabelWidgetFrame(
            self, 'Brightness', HorizontalScale, from_=0, to=100)

        self.light_mode_frame = LabelWidgetFrame(
            self, 'Light Mode', Combobox, values=light_modes)

        self.light_mode_options_frame = LabelWidgetFrame(
            self, '', Button, text='Light mode Options', command=self._btn_light_mode_options)

        self.light_speed_frame = LabelWidgetFrame(
            self, 'Light Speed (seconds)', Entry)

        self.fan_mode_frame = LabelWidgetFrame(
            self, 'Fan Mode', Combobox, values=fan_modes)

        self.fan_mode_options_frame = LabelWidgetFrame(
            self, '', Button, text='Fan mode Options', command=self._btn_fan_mode_options)

        Button(self, text='Exit', command=self.quit).pack(side='right')
        Button(self, text='Apply', command=self._btn_apply).pack(side='right')
        Button(self, text='Save', command=self._btn_save).pack(side='right')

        self.pack()


dbus_client = DbusClient()
root = Tk()

hello = ComponentSettingsFrame.say_hi

menu = {
    'File': [{'Settings': hello}],
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

app = ComponentSettingsFrame(master=root, dbus_client=dbus_client)
app.mainloop()
root.destroy()
