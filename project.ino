int trig = 12; 
int echo = 11; 
long lecture_echo; 
long cm;
void setup() 
{ 
  pinMode(trig, OUTPUT); 
  digitalWrite(trig, LOW); 
  pinMode(echo, INPUT); 
  Serial.begin(9600); 
}
void loop() 
{ 
  digitalWrite(trig, HIGH); 
  delayMicroseconds(10); 
  digitalWrite(trig, LOW); 
  lecture_echo = pulseIn(echo, HIGH); 
  cm = lecture_echo / 58; 
  Serial.print("Distance in cm : "); 
  Serial.println(cm); 
  if(cm < 100){//about 3ft
    //insert code
  }
  delay(1000); 
}
