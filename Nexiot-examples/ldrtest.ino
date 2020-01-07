int LDR=A0;//analog pin 
int LDRvalue=0;//anlaog pin value 
int light_sensitivity=800;

void setup() {
  // put your setup code here, to run once:
   Serial.begin(9600); // Uno and PC //baudrate 
   pinMode(13,OUTPUT);

}


void loop() { LDRvalue=analogRead(LDR); // 0-5V convert 0-1023 
Serial.print("LDR value is:"); 
Serial.println(LDRvalue); 
delay(1000);//1000 mili sec 
if(LDRvalue<light_sensitivity) 
{
  digitalWrite(13,HIGH);// night 
  }
  else 
  {
    digitalWrite(13,LOW); //Daytime
    }
   }
