int trig = 12;
int echo = 11;
long lecture_echo;
long cm;
long limit;
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

  limit = 125; // set custom distances depending on your desk setup
  
  if (cm < limit) { 
    int sh = 3;
    Serial.write(sh);
    delay(1000);
    Serial.println(sh);
  }
  delay(1000);
}
