ArduinoPyLogger
===============

Arduino sketch that reads three analog pins (A0, A1, A2) and send data to
python script in CSV format.

Example of output file:

Starting log...
Sun May 19 16:43:26 2013
406;338;310;
170;168;167;
173;171;170;
176;175;173;
180;179;178;
185;183;181;
Sun May 19 16:44:23 2013
Stoping log...

Usage: ./ArduinoPyLogger.py
-o	--outfile	Output file to save the log
-s	--serial	Serial port where Arduino is connected
-t	--time		Number of minutes to run the process
-h	--help		This help
example: ./ArduinoPyLogger.py -o log1.txt -s '/dev/tty.usbmodemXXX' -t 10

If you want to know which serial port Arduino is using, run:
% ls /dev/tty.usbmodem on Linux os Mac OS.
It should print the available options, choose the one best fits your device.

Remember, the sketch just sends over Serial the value converted to digital, (0-1023).
There is no unit in this data, you may convert to temperature (C or F) or any
other unit.

The script was tested on OS X, if you plan to run on Windows change the Serial
name to ComXYX or something like that.
