void setup() {
  // put your setup code here, to run once:
  Serial.begin(9600);
  
}

int valA = 0;
int valB = 0;
int valC = 0;
int valD = 0;

void loop() {
  // put your main code here, to run repeatedly:
  valA = analogRead(0);
  Serial.println("A" + String(valA));
  delay(50);
  valB = analogRead(1);
  Serial.println("B" + String(valB));
  delay(50);
  valC = analogRead(2);
  Serial.println("C" + String(valC));
  delay(50);
  valD = analogRead(3);
  Serial.println("D" + String(valD));
  delay(50);
}
