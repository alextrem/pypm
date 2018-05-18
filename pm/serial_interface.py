#! /usr/bin/env python
""" This class provides a possibility to read data from a serial interface"""

from numpy import array, zeros, int16
from threading import Thread
import collections
import logging
import serial
import struct

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
    def __init__(self, port='/dev/ttyUSB0', baud='115200', timeout=4.):
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
        self.raw_data = bytearray(2)
        self.thread = None
        self.chunk_size = 1024
        # self.buffer = zeros(self.chunk_size, dtype=int16)
        self.buffer = collections.deque([0] * self.chunk_size,
                                        maxlen=self.chunk_size)
        self.log = logging.getLogger(type(self).__name__)

        try:
            self.ser = serial.Serial(port, baud, timeout=timeout)
            self.log.info("Connected to serial port " +self._port)
            self.thread = Thread(target=self.background_thread,
                                 name="Serial Thread")
            self.thread.start()
        except serial.SerialException:
            self.log.error("Unable to open " +self._port)

    def get_buffer(self):
        """
        Provide buffer for further analysis
        """
        self.buffer[:-1]

    def background_thread(self):
        """
        Collect data in a seperat "background" thread
        """
        self.ser.flushInput()
        while self.ser.isOpen():
            self.ser.readinto(self.raw_data)
            # Shift buffer one item to the left and assign received data
            data, = struct.unpack('H', self.raw_data)
            self.buffer.append(data)
            # self.buffer[-1] = data
            # self.buffer[:-1] = self.buffer[1:]
            print self.buffer

    def close(self):
        """
        Close serial interface and and deactivate serial thread
        """
        self.thread.join()
        self.ser.close()
        self.log.info("Closing serial connection on" +self._port)

    @property
    def chunk_size(self):
        """
        """

if __name__ == '__main__': 
    ser = SerialInterface(port='/dev/tty.usbserial-FT9I6BLV', baud=921600)
