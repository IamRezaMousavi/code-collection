// Create by @IamRezaMousavi

#define red 11
#define green 10
#define blue 9

int r, g, b;

void setup() {
  Serial.begin(9600);
  
  pinMode(red, OUTPUT);
  pinMode(green, OUTPUT);
  pinMode(blue, OUTPUT);
}

void loop() {
  while (Serial.available())
  {
    r = Serial.parseInt();
    g = Serial.parseInt();
    b = Serial.parseInt();
    Serial.print("Blue=");
    Serial.println(b);
  }

  analogWrite(red, r);
  analogWrite(green, g);
  analogWrite(blue, b);
}
