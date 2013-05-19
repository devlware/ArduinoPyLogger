/************************************************************************************
* Name: ArduinoPyLogger
* Description: Simple sketch to read three analog pins and send data over Serial port,
* data is sent after python script sent 's' command.
*
* Permission is hereby granted, free of charge, to any person obtaining a copy
* of this software and associated documentation files (the "Software"), to deal
* in the Software without restriction, including without limitation the rights
* to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
* copies of the Software, and to permit persons to whom the Software is
* furnished to do so, subject to the following conditions:
*
* The above copyright notice and this permission notice shall be included in
* all copies or substantial portions of the Software.
*
* THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
* IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
* FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
* AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
* LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
* OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
* THE SOFTWARE.
*
*************************************************************************************/

/************************************************************************************
* Constants
************************************************************************************/
#define version "1.0"
#define author  "Diego W. Antunes <diego@gmail.com>"
#define license "MIT"

/************************************************************************************
* Prototypes
************************************************************************************/
void readAndPrintTemp(void);

/************************************************************************************
* Function: void setup(void)
* Description: Function where pins are defined as Input, Serial port initialized.
* Notes: 
************************************************************************************/
void setup(void)
{
    Serial.begin(9600);

    pinMode(A0, INPUT);
    pinMode(A1, INPUT);
    pinMode(A2, INPUT);
}

/************************************************************************************
* Function: void loop(void)
* Description: Where the fun stuff goes.
* Notes: Arduino waits until it receives the 's' command.
************************************************************************************/
void loop(void)
{
    int cmd = 0;
    
    if (Serial.available() > 0) {
        cmd = Serial.read();
    }

    if (cmd == (char)'s') {
        while (true) {
            readAndPrintTemp();
            delay(100);
        }
    }
}

/************************************************************************************
* Function: void readAndPrintTemp(void)
* Description: Print data in CSV format so it can be imported in a spreadsheet.
* Notes: 
************************************************************************************/
void readAndPrintTemp(void)
{
    int t1, t2, t3;
    t1 = analogRead(A0);
    t2 = analogRead(A1);
    t3 = analogRead(A2);

    Serial.print(t1); Serial.print(";");
    Serial.print(t2); Serial.print(";");
    Serial.print(t3); Serial.println(";");    
}
