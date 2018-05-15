#! /usr/bin/env python
""" This class provides a possibility to read data from a serial interface"""

from numpy import array, zeros
from threading import Thread
import logging
import serial

# TODO: Add interface as base class


class SerialInterface():
    """
    This interface gets raw data from serial interface and puts it into a
    buffer with size `chunk_size`.

    Parameters
    ----------
    port : str
        Port to connect to
    baud : int
        Chosen baudrate for this interface
    timeout : int
        Timeout must be set to have a backup when using ``readinto`` method

    Attributes
    ----------
    _port : str
        Port to connect to
    raw_data : None
        lalala
    thread : a
        lalalala
    chunk_size : int
        default chunksize is 1024
    buffer :
        numpy array buffer type

    Raises
    ------
    SerialException
        When port is not available this exception will be thrown

    Example
    -------
    This example tries to open an interface on its default port /dev/ttyUSB0
    with a baudrate of 115200

    >>> from serial_Interface import SerialInterface
    >>> ser = SerialInterface()
    >>> ser.get_buffer()

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
        self.chunk_size = 1024
        self.buffer = zeros(self.chunk_size)
        self.log = logging.getLogger(type(self).__name__)

        try:
            self.ser = serial.Serial(port, baud, timeout)
            self.thread = Thread(target=self.backgroundThread,
                                 name="Serial Thread")
            self.thread.start()
        except serial.SerialException:
            self.log.error("Fehler")

    def get_buffer(self):
        """
        Test
        """
        self.buffer[:-1]

    def backgroundThread(self):
        """
        Collect data in a seperat "background" thread
        """
        self.ser.flushInput()
        while self.ser.isOpen():
            self.ser.readinto(self.raw_data)

    def close(self):
        """
        Close serial interface and and deactivate serial thread
        """
        self.thread.join()
        self.ser.close()

    @property
    def chunk_size(self):
        """
        """
