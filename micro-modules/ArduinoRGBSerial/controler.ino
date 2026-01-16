// Create by @IamRezaMousavi

#define RED 11
#define GREEN 10
#define BLUE 9

int r, g, b;

void setup() {
  Serial.begin(9600);
  
  pinMode(RED, OUTPUT);
  pinMode(GREEN, OUTPUT);
  pinMode(BLUE, OUTPUT);
}

void loop() {
  while (Serial.available())
  {
    r = Serial.parseInt();
    g = Serial.parseInt();
    b = Serial.parseInt();
    Serial.print("BLUE=");
    Serial.println(b);
  }

  analogWrite(RED, r);
  analogWrite(GREEN, g);
  analogWrite(BLUE, b);
}
