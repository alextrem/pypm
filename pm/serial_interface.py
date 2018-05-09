#! /usr/bin/env python

from numpy import array
from threading import Thread
import serial

# TODO: Add interface as base class

class SerialInterface():
    """
    This interface gets raw data from serial interface and puts it into a
    buffer with size `chunk_size`.
    """
    def __init__(self, port='/dev/ttyUSB0', baud='115200', timeout=4):
        """
        port : str
            port to connect to
        baud : int
            Chosen baudrate for interface
        timeout : int
            Timeout must be set to have a backup when using readinto() method
        """
        self._port = port
        self._baud = baud
        self._timeout = timeout
        self.raw_data = None
        self.thread = None

        try:
            self.ser = serial.Serial(port, baud, timeout)
            self.thread = Thread(target=self.backgroundThread)
            self.thread.start()
        except SerialException:
            print "Fehler"

    def backgroundThread(self):
        """
        Collect data in a seperat "background" thread
        """
        self.ser.flushInput()
        while (self.ser.is_open()):
            self.ser.readinto(self.raw_data)

    def close():
        """
        """
        self.thread.join()
        self.ser.close()
