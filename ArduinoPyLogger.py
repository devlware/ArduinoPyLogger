#!/usr/bin/python
# -*- coding: utf-8 -*-
# 
# ArduinoPyLogger
# Small script to read Arduino serial data and save to a file. The Arduino sketch
# should wait for a command to start sending data.
#
# Copyright (C) 2013 by Diego W. Antunes <devlware@gmail.com>
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
# THE SOFTWARE.
#

import datetime
import getopt
import serial
import re
import sys
import time

__version__ = "1.0"
__author__ = 'Diego W. Antunes <devlware@gmail.com'
__license__ = 'MIT'

class ArduinoPyLogger:
    def main(self):
        """ Main method, initialize some variables and call the main loop method. """

        numMinutes = None
        serialPort = None
        outFile = None
        outFileName = None
        err = None

        try:
            opts, args = getopt.getopt(sys.argv[1:], "ht:s:o:", ["help", "time=", "serial=", "outfile="])
        except getopt.GetoptError, err:
            print(err)
            print self.usage()
            sys.exit(2)
        for opt, arg in opts:
            if opt in ("-h", "--help"):
                print self.usage()
                sys.exit(0)
            elif opt in ("-t", "--time"):
                numMinutes = int(arg) * 60
            elif opt in ("-s", "--serial"):
                serialPort = arg
            elif opt in ("-o", "--outfile"):
                outFileName = arg                
            else:
                assert False, "unhandled option"
                sys.exit()

        if serialPort == None or numMinutes == None or outFileName == None:
            print self.usage()
            sys.exit(2)

        initTime = time.time()

        try:
            ser = serial.Serial(serialPort, 9600, timeout=0.5, parity=serial.PARITY_NONE)
            time.sleep(3)

            if not ser.isOpen():
                print "Serial port is not opened, please check."
                sys.exit(-1)
        except (serial.SerialException):
            print "Could not open Serial port."
            sys.exit(-1)

        with open(outFileName, 'a') as outFile:
            ser.write('s')
            actualTime = datetime.datetime.now()
            outFile.write(unicode("Starting log...\n"))
            outFile.write(actualTime.ctime())
            outFile.write(unicode("\n"))

            while True:
                line = ser.readline()
                line = re.sub('\r', '', line)
                outFile.write(line)

                if time.time() - initTime > numMinutes:
                    actualTime = datetime.datetime.now()
                    outFile.write(actualTime.ctime())
                    outFile.write(unicode("\nStoping log...\n"))
                    break

    def usage(self):
        """ Returns usage message. """

        return "Usage: %s\n" \
                "-o\t--outfile\tOutput file to save the log\n" \
                "-s\t--serial\tSerial port where Arduino is connected\n" \
                "-t\t--time\t\tNumber of minutes to run the process\n" \
                "-h\t--help\t\tThis help\n" \
                "example: %s -o log1.txt -s '/dev/tty.usbusbmodemXXX' -t 10" % (sys.argv[0], sys.argv[0])

if __name__ == '__main__':
    ArduinoPyLogger().main()
