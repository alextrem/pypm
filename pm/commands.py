#! /usr/bin/env python

from pmbus import Pmbus

class Commands(Pmbus):
    """
    This class collects all commands needed to communicate with LT devices.
    The class acts as a command generator to write an read data over I2C Bus.

    Typical usage:

    >>> from commands im port Commands

    >>> c = Commands()
    """
    pmbus_commands = {"Page": 0x00,
                      "Operation": 0x01,
                      "On_Off_Config": 0x02,
                      "Clear_Faults": 0x03,
                      "Write_Protect": 0x10,
                      "Store_User_All": 0x15,
                      "Restore_User_All": 0x16,
                      "Capability": 0x19,
                      "Vout_Mode": 0x20,
                      "Vout_Command": 0x21,
                      "Vout_Max": 0x24,
                      "Vout_Margin_High": 0x25,
                      "Vout_Margin_Low": 0x26,
                      "Vin_On": 0x35,
                      "Vin_Off": 0x36,
                      "Vout_OV_Fault_Limit": 0x40,
                      "Vout_OV_Fault_Response": 0x41,
                      "Vout_OV_Warn_Limit": 0x42,
                      "Vout_UV_Warn_Limit": 0x43,
                      "Vout_UV_Fault_Limit": 0x44,
                      "Vout_UV_Fault_Response": 0x45,
                      "OT_Fault_Limit": 0x4F,
                      "OT_Fault_Response": 0x50,
                      "OT_Warn_Limit": 0x51,
                      "UT_Warn_Limit": 0x52,
                      "UT_Fault_Limit": 0x53,
                      "UT_FAULT_Response": 0x54,
                      "Vin_OV_Fault_Limit": 0x55,
                      "Vin_OV_Fault_Response": 0x56,
                      "Vin_OV_Warn_Limit": 0x57,
                      "Vin_UV_Warn_Limit": 0x58,
                      "Vin_UV_Fault_Limit": 0x59,
                      "Vin_UV_Fault_Response": 0x5A,
                      "Power_Good_On": 0x5E,
                      "Power_Good_Off": 0x5F,
                      "Ton_Delay": 0x60,
                      "Ton_Rise": 0x61,
                      "Ton_Max_Fault_Limit": 0x62
            }

    linear_technology_devices = {"LTC2977": (8),
                                 "LTM2987": (16)
            }

    maxim_devices = {}

    def __init__(self):
        """
        """
