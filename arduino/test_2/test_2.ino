const int LEDpin=8;
int value=HIGH;

int arr[10][5]={
  {600,600,600,600,600},
  {300,600,600,600,600},
  {300,300,600,600,600},
  {300,300,300,600,600},
  {300,300,300,300,600},
  {300,300,300,300,300},
  {600,300,300,300,300},
  {600,600,300,300,300},
  {600,600,600,300,300},
  {600,600,600,600,300}
};

void setup() {
  //pinMode(7, OUTPUT);
  Serial.begin(9600);
}

void loop() {
  while(Serial.available() > 0){
    int input=Serial.read()-'0';
    for(int i=0; i < 5; i++){
      digitalWrite(7,HIGH);
      delay(arr[input][i]);
      digitalWrite(7,LOW);
      delay(500);
    }
    delay(500);
  }
}


