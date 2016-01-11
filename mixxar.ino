void setup() {
  Serial.begin(9600);
  Serial.println("ARDUINO READY");
}

int valA = 0;
int valB = 0;
int valC = 0;
int valD = 0;
bool OSFound = false;

void loop() {
  while (!OSFound){
    if (Serial.readString() == "OS READY"){
      OSFound = true;
    }
  }
  valA = analogRead(0);
  Serial.println("CON-OK" + "A" + String(valA));
  delay(50);
  valB = analogRead(1);
  Serial.println("CON-OK" + "B" + String(valB));
  delay(50);
  valC = analogRead(2);
  Serial.println("CON-OK" + "C" + String(valC));
  delay(50);
  valD = analogRead(3);
  Serial.println("CON-OK" + "D" + String(valD));
  delay(50);
}
