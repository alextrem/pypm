#!/usr/bin/env python

"""
Parse the file for programming Linears Power Management devices
"""

import struct
from intelhex import IntelHex


class Parser(object):
    """
    Parser class currently for LT devices ISP hexfile

    It convertes the encoded instruction in the hexfile into CSV.
    As a result we can use the CSV to program the device

    Attributes
    ----------
    record_length : hex
        Defines the length of the record in half word
    record_type : byte
        Linear Technologies defined record types
    address : byte
        Address to write to PM device
    command : byte
        TBD
    data : byte
        TBD
    """
    lt_record_type = {"PMBUS_WRITE_BYTE": 0x01,
                      "PMBUS_WRITE_WORD": 0x02,
                      "PMBUS_WRITE_BLOCK": 0x03,
                      "PMBUS_READ_BYTE_EXPECT": 0x04,
                      "PMBUS_READ_WORD_EXPECT": 0x05,
                      "PMBUS_READ_BLOCK_EXPECT": 0x06,
                      "DEVICE_ADDRESS": 0x07,
                      "PACKING_CODE": 0x08,
                      "NVM_DATA": 0x09,
                      "PMBUS_READ_BYTE_LOOP_MASK": 0x0A,
                      "PMBUS_READ_WORD_LOOP_MASK": 0x0B,
                      "PMBUS_POLL_UNTIL_ACK_NOPEC": 0x0C,
                      "DELAY_MS": 0x0D,
                      "PMBUS_SEND_BYTE": 0x0E,
                      "PMBUS_WRITE_BYTE_NOPEC": 0x0F,
                      "PMBUS_WRITE_WORD_NOPEC": 0x10,
                      "PMBUS_WRITE_BLOCK_NOPEC": 0x11,
                      "PMBUS_READ_BYTE_EXPECT_NOPEC": 0x12,
                      "PMBUS_READ_WORD_EXPECT_NOPEC": 0x13,
                      "PMBUS_READ_BLOCK_EXPECT_NOPEC": 0x14,
                      "PMBUS_READ_BYTE_LOOP_MASK_NOPEC": 0x15,
                      "PMBUS_READ_WORD_LOOP_MASK_NOPEC": 0x16,
                      "PMBUS_SEND_BYTE_NOPEC": 0x17,
                      "EVENT": 0x18,
                      "PMBUS_READ_BYTE_EXPECT_MASK_NOPEC": 0x19,
                      "PMBUS_READ_WORD_EXPECT_MASK_NOPEC": 0x1A,
                      "VARIABLE_META_DATA": 0x1B,
                      "MODIFY_WORD_NOPEC": 0x1C,
                      "MODIFY_BYTE_NOPEC": 0x1D,
                      "PMBUS_WRITE_EE_DATA": 0x1E,
                      "PMBUS_READ_AND_VERIFY_EE_DATA": 0x1F,
                      "PMBUS_MODIFY_BYTE": 0x20,
                      "PMBUS_MODIFY_WORD": 0x21
            }

    lt_record_event = {"BEFORE_BEGIN": 0x00,
                       "BEFORE_INSYSTEM_PROGRAMMING_BEGIN": 0x10,
                       "SYSTEM_BEFORE_PROGRAMMING": 0x01,
                       "INSYSTEM_CHIP_BEFORE_PROGRAM": 0x11,
                       "SYSTEM_BEFORE_VERIFY": 0x02,
                       "INSYSTEM_CHIP_BEFORE_VERIFY": 0x12,
                       "INSYSTEM_CHIP_AFTER_VERIFY": 0x13,
                       "SYSTEM_AFTER_VERIFY": 0x04,
                       "AFTER_DONE": 0x03}


    def __init__(self, hexfile):
        """
        Constructor
        """
        self.hf = IntelHex(hexfile)
        self.record_length = None
        self.record_type = None
        self.address = None
        self.command = None
        self.data = None
        self.payload = []

    def _get_lt_record_type(self, position):
        """
        Interpret what is in the hexfile
        """
        i = position

        # Get the number of bytes for the defined record
        self.record_length = struct.unpack('<H', struct.pack('2B',
                                                             self.hf[i],
                                                             self.hf[i+1]))[0]

        # Record
        self.record_type = struct.unpack('<H', struct.pack('2B',
                                                           self.hf[i+2],
                                                           self.hf[i+3]))[0]

        # When there is an event inform us
        if self.record_type == self.lt_record_type["EVENT"]:
            print "Event triggered"
            self._get_lt_payload(i)
            #for n in self.lt_record_event is self.data
        elif self.record_type == self.lt_record_type["PMBUS_WRITE_BYTE"]:
            self._get_lt_payloadheader(i)
            self._get_lt_payload(i)
            self.payload.append([self.address, self.command, self.data])
        elif self.record_type == self.lt_record_type["PMBUS_WRITE_BYTE_NOPEC"]:
            self._get_lt_payloadheader(i)
            self._get_lt_payload(i)
            self.payload.append([self.address, self.command, self.data])
        elif self.record_type == self.lt_record_type["PMBUS_WRITE_WORD"]:
            self._get_lt_payloadheader(i)
            self._get_lt_payload(i)
            self.payload.append([self.address, self.command, self.data])
        elif self.record_type == self.lt_record_type["PMBUS_WRITE_WORD_NOPEC"]:
            self._get_lt_payloadheader(i)
            self._get_lt_payload(i)
            self.payload.append([self.address, self.command, self.data])
        elif self.record_type == self.lt_record_type["PMBUS_READ_BYTE_LOOP_MASK"]:
            self._get_lt_payloadheader(i)
            self._get_lt_payload(i)
            self.payload.append([self.address, self.command, self.data])
        elif self.record_type == self.lt_record_type["NVM_DATA"]:
            self._get_lt_payloadheader(i)
            self._get_lt_payload(i)
            self.payload.append([self.address, self.command, self.data])


        return self.record_length

    def _get_lt_payloadheader(self, position):
        """
        Extract payloadheader
        """
        # Assume LT record and payload header need to byte each
        i = position + 4

        self.address = struct.unpack('<H', struct.pack('2B', self.hf[i],
                                                             self.hf[i+1]))[0]
        # Find how much we need to parse
        self.command = struct.unpack('B', struct.pack('B', self.hf[i+2]))[0]

    def _get_lt_payload(self, position):
        """
        Extract payload

        Parameters
        ----------
        position : int
            position in hexfile
        """
        i = position + 7

        if self.record_type == self.lt_record_type["EVENT"]:
            i = position +4
            print "Position %d" % i
            self.data = struct.unpack('<H', struct.pack('2B', self.hf[i+1],
                                                              self.hf[i+2]))[0]
            print "Data %d" % self.data
        elif self.record_type == self.lt_record_type["PMBUS_WRITE_BYTE"]:
            self.data = struct.unpack('B', struct.pack('B', self.hf[i+1]))[0]
        elif self.record_type == self.lt_record_type["PMBUS_WRITE_BYTE_NOPEC"]:
            self.data = struct.unpack('B', struct.pack('B', self.hf[i]))[0]
        elif self.record_type == self.lt_record_type["PMBUS_WRITE_WORD"]:
            self.data = struct.unpack('<H', struct.pack('2B', self.hf[i+1],
                                                              self.hf[i+2]))[0]
        elif self.record_type == self.lt_record_type["PMBUS_WRITE_WORD_NOPEC"]:
            self.data = struct.unpack('<H', struct.pack('2B', self.hf[i],
                                                              self.hf[i+1]))[0]
        elif self.record_type == self.lt_record_type["PMBUS_READ_BYTE_LOOP_MASK"]:
            self.data = struct.unpack('<H', struct.pack('2B', self.hf[i+1],
                                                              self.hf[i+2]))[0]

    def parse(self, hexfile="ltctest.isphex"):
        """
        Parse the hexfile, yo

        Parameters
        ----------
        hexfile : str
            hexfile which should be parsed
        """
        i = 0
        while i < self.hf.__len__():
            i += self._get_lt_record_type(i)
            print i

        print self.payload


p = Parser("pm/ltctest.isphex")
p.parse()
