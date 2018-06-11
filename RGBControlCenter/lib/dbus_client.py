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
import dbus as dbus

OPATH = '/org/thermaltake/Daemon'
IFACE = 'org.thermaltake.Daemon'
BUS_NAME = IFACE


class DbusClient:

    def __init__(self):
        self.bus = dbus.SessionBus()
        self.service = self.bus.get_object(BUS_NAME, OPATH)

    def set_lighting_controller(self, _type: str, **kwargs):
        service = self.service.set_lighting_controller
        if _type == 'rgb_spectrum':
            service(_type)

        elif _type == 'spinning_rgb_spectrum':
            service(_type)

        elif _type == 'alternating':
            even = [int(v) for v in kwargs.get('even')]
            odd = [int(v) for v in kwargs.get('odd')]
            service(_type, even, odd)

        elif _type == 'static':
            value = [int(v) for v in kwargs.get('value')]
            service(_type, *value)

        elif _type == 'temperature':
            sensor = kwargs.get('sensor')
            hot = kwargs.get('hot')
            target = kwargs.get('target')
            cold = kwargs.get('cold')
            service(_type, sensor, hot, target, cold)

    def set_fan_controller(self, _type: str, **kwargs):
        service = self.service.set_fan_controller
        if _type == 'locked_speed':
            service(_type, kwargs.get('speed'))

        elif _type == 'temp_target':
            service(_type, kwargs.get('target'), kwargs.get('sensor'))

    def set_lighting_brightness(self, brightness: int):
        service = self.service.set_lighting_brightness
        service(int(brightness))

    def set_lighting_msec(self, msec: float):
        service = self.service.set_lighting_msec
        service(float(msec))


if __name__ == "__main__":
    a = DbusClient()
    a.set_lighting_controller('temperature', sensor='k10temp')
    a.set_lighting_brightness(15)
    a.set_lighting_msec(100)

