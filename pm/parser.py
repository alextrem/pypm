#! /usr/bin/env python

import struct
from intelhex import IntelHex

class Parser(object):
    """
    Parser class currently for LT devices ISP hexfile
    """
    record_type = {"PMBUS_WRITE_BYTE": 0x01,
                   "PMBUS_WRITE_WORD": 0x02,
                   "PMBUS_WRITE_BLOCK": 0x03,
                   "PMBUS_READ_BYTE_EXPECT": 0x04,
                   "PMBUS_READ_WORD_EXPECT": 0x05,
                   "PMBUS_READ_BLOCK_EXPECT": 0x06,
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


    def __init__(self):
        """
        """
    def _get_lt_record_type(self, fileobject):
        """
        Interpret what is in the hexfile
        """

    def parse(self):
        """
        Parse the hexfile, yo
        """

