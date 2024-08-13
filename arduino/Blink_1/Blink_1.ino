const int LEDpin=13;
int timeDelay=100;
int value = HIGH;



void setup() {
  // initialize digital pin 13 as an output.
  pinMode(LEDpin, OUTPUT);
  value=1;
}

// the loop function runs over and over again forever
int del=timeDelay*4;
int swi=1;

void loop() {
  swi*=-1;
  if(swi==1){
    int tmp=timeDelay;
    timeDelay=del;
    del=tmp;
  }
  while(del >= timeDelay){
    digitalWrite(LEDpin, HIGH);
    delay(1500);
    digitalWrite(LEDpin,LOW);
    delay(del);
    del+=timeDelay*swi;
  }
}
