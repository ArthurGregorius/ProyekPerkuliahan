#include <LiquidCrystal_I2C.h>

LiquidCrystal_I2C lcd(0x27, 16, 2);
const int LM35Pin = A0; // Pin analog tempat LM35 terhubung
const int Relay = 2;

void setup() {
  Serial.begin(9600);
  lcd.init();
  lcd.backlight();
  lcd.setCursor(0, 0);
  lcd.print(" ALAT PENGERAM ");
  lcd.setCursor(0, 1);
  lcd.print(" TELUR OTOMATIS ");
  delay(5000)
  lcd.clear();
  pinMode(Relay, OUTPUT);
  digitalWrite(Relay, LOW);
}
void loop() {
  int sensorValue = analogRead(LM35Pin); // Baca nilai analog dari LM35
  float temperatureC = (sensorValue * 5.0 / 1023.0) * 100.0; // Konversi nilai bacaan analog ke suhu dalam derajat Celcius
  lcd.setCursor(0, 0);
  lcd.print("Suhu: ");
  lcd.print(temperatureC);
  lcd.print((char)223);
  lcd.print("C ");
  delay(5000);

  if (temperatureC < 37.5) {
  digitalWrite(Relay, HIGH);
  }

  if (temperatureC > 39.5) {
  digitalWrite(Relay, LOW);
  }
}