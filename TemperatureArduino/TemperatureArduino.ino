#include <SoftwareSerial.h>
#include <LiquidCrystal.h>
#include <DHT.h>

#define DHTPIN A2
#define DHTTYPE DHT11

SoftwareSerial sim800Serial(7, 8); // RX, TX
LiquidCrystal lcd(2, 3, 4, 5, 11, 12);


DHT dht(DHTPIN, DHTTYPE);


int lm35Pin = A0; // LM35 sensor connected to analog pin A0
int hr202lPin = A1; // HR202L sensor connected to analog pin A1
int lm35Value = 0;
int hr202lValue = 0;
float temperature = 0, humidity = 0;
int n = 0;
int x = 40, y = 10, l = 60, h = 10;
char sended = 0;

void setup() {
  sim800Serial.begin(115200); // Start the software serial communication with SIM800 module
  lcd.begin(16, 2); // Set up the LCD's number of columns and rows
  dht.begin();
  Serial.begin(115200);
}

void loop() {
  n = 10;
  while (n) {
    lm35Value += analogRead(lm35Pin);  
    n--;
    delay(50);
  }
  lm35Value /= 10;
  temperature = (lm35Value * 5.0 * 100.0) / 1024.0;

  n = 10;
  while (n) {
    humidity += dht.readHumidity(); 
    n--;
    delay(50);
  }
  humidity /= 10;

  Serial.println(temperature);
  Serial.println(humidity);
  
  lcd.clear();
  lcd.setCursor(0, 0);
  lcd.print("Temp: ");
  lcd.print(temperature);
  lcd.print(" C");
  lcd.setCursor(0, 1);
  lcd.print("Humidity: ");
  lcd.print(humidity);
  lcd.print("%");

  if (temperature > x || temperature < y) { //x = high temp, y = low temp
    SMS(0, temperature);
    delay(2000);
  }
  if (humidity > l || humidity < h) { //l = high humidity, h = low humidity
    SMS(1, humidity);
    delay(2000);
  }

  if (sended < 1) {
    SMS(0, temperature);
    delay(3000);
    SMS(1, humidity);
    delay(1000);
    sended++;
  }
}

void SMS(bool f, float value) {
  // Send the temperature and humidity data via SMS
  sim800Serial.println("AT");
  sim800Serial.println("AT+CREG=1");
  sim800Serial.println("AT+CMGF=1"); // Set the SMS mode to text
  delay(1000);
  sim800Serial.println("AT+CMGS=\"09934418679\""); // Replace with the phone number to send the SMS to
  delay(1000);
  if (!f) {
    sim800Serial.print("Temperature: ");
    sim800Serial.print(value);
    sim800Serial.print(" C");
  } else {
    sim800Serial.print("Humidity: ");
    sim800Serial.print(humidity);
  }
  sim800Serial.write(26); // End the SMS with Ctrl+Z
  delay(1000);
}
