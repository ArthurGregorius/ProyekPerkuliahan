#include <WiFi.h>
#include "CTBot.h"
CTBot myBot;
String ssid = "mahen";
String pass = "mahen0221";
String token = "6761526499:AAHCAEcoT_HTFpq9WUmdI21WQUGBrv7ILH4";
const int id = 1115751958;

#define Buzzer 5
#define Sensor 2

void adaMaling(){
    digitalWrite(Buzzer, HIGH);
    myBot.sendMessage(id, "WASPADA, GERAKAN TERDETEKSI!!");
}

void setup() {
  Serial.begin(9600);
  Serial.println("Starting TelegramBot...");
  myBot.wifiConnect(ssid, pass);
  myBot.setTelegramToken(token);
  pinMode(Buzzer, OUTPUT);
  pinMode(Sensor, INPUT);
}

void loop() {
  bool sensorValue = digitalRead(Sensor);

  if (sensorValue == 1) {
    adaMaling();
    Serial.println("Gerakan Terdeteksi");
  } else {
    digitalWrite(Buzzer, LOW);
  }

}