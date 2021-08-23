################################################################################
##                                                                            ##
##                   Advanced Navigation Python Language SDK                  ##
##                                 packet_0.py                                ##
##                     Copyright 2021, Advanced Navigation                    ##
##                                                                            ##
################################################################################
#                                                                              #
# Copyright (C) 2021 Advanced Navigation                                       #
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

""" Acknowledge Packet 0, as defined in Advance Navigation Reference Manuals """

from enum import Enum
from struct import unpack
from dataclasses import dataclass
from anpp_packets.packets.an_packet_protocol import AN_Packet
from anpp_packets.packets.anpp_packets import PacketID

class AcknowledgeResult():
    class AcknowledgeResult(Enum):
        success = 0
        failure_crc = 1
        failure_length = 2
        failure_range = 3
        failure_flash = 4
        failure_not_ready = 5
        failure_unknown_packet = 6


class AcknowledgePacket():
    @dataclass()
    class AcknowledgePacket:
        packet_id: PacketID.PacketID = 0
        packet_crc: int = 0
        acknowledge_result: AcknowledgeResult.AcknowledgeResult = 0

        def decode(self, an_packet: AN_Packet):
            if((an_packet.id == PacketID.PacketID.acknowledge.value) and (len(an_packet.data) == 4)):
                self.packet_id = an_packet.data[0]
                self.packet_crc = unpack('<H', bytes(an_packet.data[1:3]))[0]
                self.acknowledge_result = AcknowledgeResult.AcknowledgeResult(an_packet.data[3])
                return 0
            else:
                return 1