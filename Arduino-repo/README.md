# Getting Started with Arduino

## Contents:

1. Blinking internal LED of an Arduino UNO
2. [Home automation using NodeMCU](https://github.com/Ikarthikmb/Hardware-Codes/blob/master/Arduino-repo/Adafruit-Led-NodeMCU.ino)
3. [Making a Server Access Point with NodeMCU, commecting it to the Wi-Fi](https://github.com/Ikarthikmb/Hardware-Codes/blob/master/Arduino-repo/Server-AP-mode.ino)
4. [Creating a Server using NodeMCU](https://github.com/Ikarthikmb/Hardware-Codes/blob/master/Arduino-repo/server-code-AP.ino)

>

## 1. Blinking internal LED of an Arduino UNO

To begin with Arduino open the Arduino IDE open ` File → New `. This will create a new sketch. To import our LED blink program go to ` File → Examples → 01.Basics → Blink `

> [ArduinoUNO internal led blink Image](https://drive.google.com/file/d/1GEBBNadbKFdoJK1YAXTP2Pm20Hu1KAiR/view)

This will load the LED blink code. All you have to do is connect the Arduino to pc using the cable. 

To verify the code hit ` Ctrl + R ` or you will find the tick symbol below the menu bar. Verify then Compile and ` Run ` the code. 

If the code shows zero errors then the orange LED of Arduino starts blinking. Further you can even run other examples from the Examples section in the File menu.

### The Code

    // the setup function runs once when you press reset or power the board
    void setup() {
      // initialize digital pin LED_BUILTIN as an output.
      pinMode(LED_BUILTIN, OUTPUT);
    }

    // the loop function runs over and over again forever
    void loop() {
      digitalWrite(LED_BUILTIN, HIGH);   // turn the LED on (HIGH is the voltage level)
      delay(1000);                       // wait for a second
      digitalWrite(LED_BUILTIN, LOW);    // turn the LED off by making the voltage LOW
      delay(1000);                       // wait for a second
    }
