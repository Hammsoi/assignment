void setup() {
  Serial.begin(9600);

  for (int i = 2; i <= 5; i++) {
    for (int j = 1; j <= 9; j++) {
      Serial.println(String(i) + " x " + String(j) + " = " + String(i * j));
    }
    Serial.println(); 
  }
}

void loop() {
  
}
