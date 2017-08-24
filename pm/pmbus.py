#! /usr/bin/env python

""" Module creates PMBus commands to be sent """

import struct

class Pmbus(object):
    """
    This class creates commands for PMBus
    """
    def __init__(self):
        """
        Constructor
        """

    def write_byte(self, slave_addr, command, data):
        """
        Send a data byte over PMBus

        Parameters
        ----------
        slave_addr: device address
        command:
        data:

        Returns
        -------

        """

    def write_word(self, slave_addr, command, data):
        """
        Send two bytes over PMBus

        Parameters
        ----------
        slave_addr: device address
        command:
        data:

        Returns
        -------

        """

    def write_byte_pec(self, slave_addr, command, data):
        """
        Send byte over PMBus

        Parameters
        ----------
        slave_addr: Device address
        command:
        data:

        Returns
        -------

        """
    def write_word_pec(self, slave_addr, command, data):
        """
        Write word with parity error check

        Parameters
        ----------
        slave_addr: Device address
        command:
        data:

        Returns
        -------

        """
    def send_byte(self, slave_addr, command):
        """
        Send byte over PMBus

        Parameters
        ----------
        slave_addr: Device address
        command:

        Returns
        -------

        """
    def send_byte_pec(self, slave_addr, command):
        """
        Send byte with parity error check

        Parameters
        ----------
        slave_addr: Device address
        command:

        Returns
        -------

        """
    def read_word(self, slave_addr, command):
        """
        Read two bytes over PMBus

        Parameters
        ----------
        slave_addr: Device address
        command:

        Returns
        -------

        """
        commands = struct.pack('2B', slave_addr, command)
        print commands
        print (slave_addr, command)
        return command

    def read_word_pec(self, slave_addr, command):
        """
        Read two bytes over PMBus with parity error check

        Parameters
        ----------
        slave_addr: Device address
        command:

        Returns
        -------

        """
    def read_byte(self, slave_addr, command):
        """
        Read byte over PMBus

        Parameters
        ----------
        slave_addr: Device address
        command:

        Returns
        -------

        """
    def read_byte_pec(self, slave_addr, command):
        """
        Read byte over PMBus with parity error check

        Parameters
        ----------
        slave_addr: Device address
        command:

        Returns
        -------

        """
    def read_block(self, slave_addr, command, count):
        """
        Read a block of data

        Parameters
        ----------
        slave_addr: Device address
        command:
        count: Number of bytes to be read

        Returns
        -------

        """
    def read_block_pec(self, slave_addr, command, count):
        """
        Read a block of data woth parity error check

        Parameters
        ----------
        slave_addr: Device address
        command:
        count: Number of bytes to be read

        Returns
        -------

        """
