#! /usr/bin/env python

from pmbus import Pmbus

class Commands(Pmbus):
    """
    This class collects all commands needed to communicate with Powermanagement devices.
    The class acts as a command generator to write an read data over I2C Bus.

    Typical usage:

    >>> from commands import Commands

    >>> c = Commands()

    All commands contain a key, value pair
    """
    pmbus_commands = {"PAGE": (0x00, False),
                      "OPERATION": (0x01, True),
                      "ON_OFF_CONFIG": (0x02, True),
                      "CLEAR_FAULTS": (0x03, True),
                      "WRITE_PROTECT": (0x10, True),
                      "STORE_USER_ALL": 0x15,
                      "RESTORE_USER_ALL": 0x16,
                      "CAPABILITY": 0x19,
                      "VOUT_MODE": 0x20,
                      "VOUT_COMMAND": 0x21,
                      "VOUT_MAX": 0x24,
                      "VOUT_MARGIN_HIGH": 0x25,
                      "VOUT_MARGIN_LOW": 0x26,
                      "VIN_ON": 0x35,
                      "VIN_OFF": 0x36,
                      "VOUT_OV_FAULT_LIMIT": 0x40,
                      "VOUT_OV_FAULT_RESPONSE": 0x41,
                      "VOUT_OV_WARN_LIMIT": 0x42,
                      "VOUT_UV_WARN_LIMIT": 0x43,
                      "VOUT_UV_FAULT_LIMIT": 0x44,
                      "VOUT_UV_FAULT_RESPONSE": 0x45,
                      "OT_FAULT_LIMIT": 0x4F,
                      "OT_FAULT_RESPONSE": 0x50,
                      "OT_WARN_LIMIT": 0x51,
                      "UT_WARN_LIMIT": 0x52,
                      "UT_FAULT_LIMIT": 0x53,
                      "UT_FAULT_RESPONSE": 0x54,
                      "VIN_OV_FAULT_LIMIT": 0x55,
                      "VIN_OV_FAULT_RESPONSE": 0x56,
                      "VIN_OV_WARN_LIMIT": 0x57,
                      "VIN_UV_WARN_LIMIT": 0x58,
                      "VIN_UV_FAULT_LIMIT": 0x59,
                      "VIN_UV_FAULT_Response": 0x5A,
                      "POWER_GOOD_ON": 0x5E,
                      "POWER_GOOD_OFF": 0x5F,
                      "TON_DELAY": 0x60,
                      "TON_RISE": 0x61,
                      "TON_MAX_FAULT_LIMIT": 0x62,
                      "TON_MAX_FAULT_RESPONSE": 0x63,
                      "TOFF_DELAY": (0x64, True),
                      "STATUS_BYTE": (0x78, True),
                      "STATUS_WORD": (0x79, True),
                      "STATUS_VOUT": (0x7A, True),
                      "STATUS_INPUT": (0x7C, True),
                      "STATUS_TEMPERATURE": (0x7D, True),
                      "STATUS_CML": (0x7E, True),
                      "STATUS_MFR_SPECIFIC": (0x80, True),
                      "READ_VIN": (0x88, False),
                      "READ_VOUT": (0x8B, True),
                      "READ_TEMPERATURE": (0x8D, False),
                      "PMBUS_REVISION": (0x98, False),
                      "USER_DATA_00": (0xB0, False),
                      "USER_DATA_01": (0xB1, True),
                      "USER_DATA_02": (0xB2, False),
                      "USER_DATA_03": (0xB3, True),
                      "USER_DATA_04": (0xB4, False),
                      "MFR_LTC_RESERVED_1": (0xB5, True),
                      "MFR_STATUS_2": (0xB7, True),
                      "MFR_LTC_RESERVED_2": (0xBC, True),
                      "MFR_EE_UNLOCK": (0xBD, False),
                      "MFR_EE_DATA": (0xBF, False),
                      "MFR_COMMAND_PLUS": (0xC0, False),
                      "MFR_DATA_PLUS0": (0xC1, False),
                      "MFR_DATA_PLUS1": (0xC2, False),
                      "MFR_TELEMETRY": (0xCF, False),
                      "MFR_CONFIG_LTC2977": (0xD0, False),
                      "MFR_CONFIG_ALL_LTC2977": (0xD1, False),

            }

    analog_devices = {}
    linear_technology_devices = {"LTC2977": (8),
                                 "LTM2987": (16)
            }

    maxim_devices = {}

    def __init__(self):
        """
        """
