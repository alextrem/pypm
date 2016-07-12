#! /usr/bin/env python

class Pmbus():
    """
    """
    def __init__(self):
        """
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
        """

    def write_byte_pec(self, slave_addr, command, data):
        """
        """
    def write_word_pec(self, slave_addr, command, data):
        """
        """
    def send_byte(self, slave_addr, command):
        """
        """
    def send_byte_pec(self, slave_addr, command):
        """
        """
    def read_word(self, slave_addr, command):
        """
        """
    def read_word_pec(self, slave_addr, command):
        """
        """
    def read_byte(self, slave_addr, command):
        """
        """
    def read_byte_pec(self, slave_addr, command):
        """
        """
    def read_block(self, slave_addr, command, count):
        """
        """
    def read_block_pec(self, slave_addr, command, count):
        """
        """
