################################################################################
##                                                                            ##
##                   Advanced Navigation Python Language SDK                  ##
##                            orientus_device.py                              ##
##                     Copyright 2023, Advanced Navigation                    ##
##                                                                            ##
################################################################################
#                                                                              #
# Copyright (C) 2023 Advanced Navigation                                       #
#                                                                              #
# Permission is hereby granted, free of charge, to any person obtaining        #
# a copy of this software and associated documentation files (the "Software"), #
# to deal in the Software without restriction, including without limitation    #
# the rights to use, copy, modify, merge, publish, distribute, sublicense,     #
# and/or sell copies of the Software, and to permit persons to whom the        #
# Software is furnished to do so, subject to the following conditions:         #
#                                                                              #
# The above copyright notice and this permission notice shall be included      #
# in all copies or substantial portions of the Software.                       #
#                                                                              #
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS      #
# OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,  #
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE  #
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER       #
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING      #
# FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER          #
# DEALINGS IN THE SOFTWARE.                                                    #
################################################################################

from .advanced_navigation_device_serial import (
    AdvancedNavigationDeviceSerial as _AdvancedNavigationDevice,
)
from ..anpp_packets.an_packets import PacketID as _PacketID


class Orientus(_AdvancedNavigationDevice):
    """Orientus object with high level functions for setting and receiving values"""

    valid_baud_rates = [
        2400,
        4800,
        9600,
        19200,
        38400,
        57600,
        115200,
        230400,
        250000,
        460800,
        500000,
        800000,
        921600,
        1000000,
        1250000,
        2000000,
    ]

    def return_device_information_and_configuration_packets(self):
        """Returns Orientus' Device Information and Configuration packets as
        all Advanced Navigation devices have different packets available"""
        return [
            _PacketID.device_information,
            _PacketID.packet_timer_period,
            _PacketID.packets_period,
            _PacketID.baud_rates,
            _PacketID.sensor_ranges,
            _PacketID.installation_alignment,
            _PacketID.filter_options,
            _PacketID.gpio_configuration,
            _PacketID.magnetic_calibration_values,
            _PacketID.magnetic_calibration_status,
        ]