
//variable declarations
int RXdata = 0; 

void setup() {
  // put your setup code here, to run once:
  //set pins 2-5 as output for LEDs
  Serial.begin(9600);   //configure serial port to 9600 baud
}

void loop() {
  // put your main code here, to run repeatedly:
int sh = 3;
//  if (Serial.available() > 0){   //check if any data was received
   Serial.write(sh);
   delay(1000);
Serial.println(sh);
//    RXdata = Serial.read();
//    Serial.print(RXdata, DEC);

//  }

}
