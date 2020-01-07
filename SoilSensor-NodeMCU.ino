const int sensor_pin = A0;  /* Connect Soil moisture analog sensor pin to A0 of NodeMCU */

void setup() {
  Serial.begin(9600); /* Define baud rate for serial communication */
}

void loop() {
  float moisture_percentage;

  moisture_percentage = ( 100.00 - ( (analogRead(sensor_pin)/1023.00) * 100.00 ) );

  Serial.print("Soil Moisture(in Percentage) = ");
  Serial.print(moisture_percentage);
  Serial.println("%");

  delay(1000);
}
