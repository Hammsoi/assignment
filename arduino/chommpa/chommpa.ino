const int echo=6;
const int trig=7;
const int motor=3;
void setup() {
  Serial.begin(9600);
  pinMode(echo,INPUT);
  pinMode(trig,OUTPUT);
  pinMode(motor,OUTPUT);
}

void loop() {
  float duration, distance;

  digitalWrite(trig,HIGH);
  delay(10);
  digitalWrite(trig,LOW);

  duration=pulseIn(echo,HIGH);
  distance=duration/1000000*34300/2;
  
  if(distance<=10){
    analogWrite(motor, 200);
    Serial.println("ON");
  }else{
    analogWrite(motor, 0);
     Serial.println("OFF");
  }
  Serial.print(distance);
  Serial.println("cm");
  delay(500);
  }