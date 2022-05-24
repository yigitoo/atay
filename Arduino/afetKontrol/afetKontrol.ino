// Import required libraries
#include "deneyap.h"
#include <WiFi.h>
#include <ESPAsyncWebServer.h>
#include <SPIFFS.h>
#include "lsm6dsm.h"

LSM6DSM imu;
// Replace with your network credentials
//WiFi SSID: ATAY
//WiFi
//WiFi Password: nflpycpp0962 -> your home
//
const char* ssid = "ATAY";
const char* password = "12345678";

// Create AsyncWebServer object on port 80
AsyncWebServer server(80);
String buildingStatus = "Yıkılmadı";
String controlBuildingStatus()
{
  if (imu.readFloatGyroX() > 20 || imu.readFloatGyroX() < -20 )
  {
    buildingStatus = "Yıkıldı";
  }
   else if (imu.readFloatGyroY() > 20 || imu.readFloatGyroY() < -20 )
  {
    buildingStatus = "Yıkıldı";
  }
   else if (imu.readFloatGyroZ() > 20 || imu.readFloatGyroZ() < -20 )
  {
    buildingStatus = "Yıkıldı";
  }
  return buildingStatus;
}
String readAccelerometerXAxis() {
  return String(imu.readFloatAccelX());
}

String readAccelerometerYAxis() {
  return String(imu.readFloatAccelY());
}

String readAccelerometerZAxis() {
  return String(imu.readFloatAccelZ());
}

String readGyroXAxis() {
  return String(imu.readFloatGyroX());
}
String readGyroYAxis() {
  return String(imu.readFloatGyroY());
}
String readGyroZAxis() {
  return String(imu.readFloatGyroZ());
}
String readTempC() {
  return String(imu.readTempC());
}
void setup() {  
  // Serial port for debugging purposes
  Serial.begin(115200);
  imu.begin();                                  // IMU ayarlari konfigure edildi

  String gyroX = String(imu.readFloatGyroX());
  String gyroY = String(imu.readFloatGyroY());
  String gyroZ = String(imu.readFloatGyroZ());

  
  
  // Initialize SPIFFS
  if (!SPIFFS.begin()) {
    Serial.println("An Error has occurred while mounting SPIFFS");
    return;
  }

  // Connect to Wi-Fi
  WiFi.begin(ssid, password);
  Serial.print("Connecting to WiFi");
  while (WiFi.status() != WL_CONNECTED)
  {
    delay(1000);
    Serial.print(".");
  }


  // Print Deneyap_Kart Local IP Address
  Serial.println("");
  Serial.println(WiFi.localIP());

  // Route for root / web page
  server.on("/", HTTP_GET, [](AsyncWebServerRequest * request) {
    request->send(SPIFFS, "/anamenu.html");
  });

  server.on("/bina", HTTP_GET, [](AsyncWebServerRequest * request) {
    request->send(SPIFFS, "/index.html");
  });

  server.on("/harita", HTTP_GET, [](AsyncWebServerRequest * request) {
    request->send(SPIFFS, "/map.html");
  });

  server.on("/binaEkle", HTTP_GET, [](AsyncWebServerRequest * request) {
    request->send(SPIFFS, "/binaEkle/index.html");
  });

  server.on("/tempC", HTTP_GET, [] (AsyncWebServerRequest * request){
    request->send_P(200, "text/plain", readTempC().c_str());
  });
  
  server.on("/controlBuildingStatus", HTTP_GET, [](AsyncWebServerRequest * request) {
    request->send_P(200, "text/plain", controlBuildingStatus().c_str());
  });

  server.on("/accelerometerX", HTTP_GET, [](AsyncWebServerRequest * request) {
    request->send_P(200, "text/plain", readAccelerometerXAxis().c_str());
  });

  server.on("/accelerometerY", HTTP_GET, [](AsyncWebServerRequest * request) {
    request->send_P(200, "text/plain", readAccelerometerYAxis().c_str());
  });

  server.on("/accelerometerZ", HTTP_GET, [](AsyncWebServerRequest * request) {
    request->send_P(200, "text/plain", readAccelerometerZAxis().c_str());
  });

  server.on("/gyroX", HTTP_GET, [](AsyncWebServerRequest * request) {
    request->send_P(200, "text/plain", readGyroXAxis().c_str());
  });

  server.on("/gyroY", HTTP_GET, [](AsyncWebServerRequest * request) {
    request->send_P(200, "text/plain", readGyroYAxis().c_str());
  });

  server.on("/gyroZ", HTTP_GET, [](AsyncWebServerRequest * request) {
    request->send_P(200, "text/plain", readGyroZAxis().c_str());
  });

  server.on("/olcumler.txt", HTTP_GET, [](AsyncWebServerRequest * request) {
    request->send(SPIFFS, "/olcumler.txt", String(), true);
  });

  server.on("/highcharts.js", HTTP_GET, [](AsyncWebServerRequest * request) {
    request->send(SPIFFS, "/highcharts.js", "text/javascript");
  });

  
  server.on("/leaflet.js", HTTP_GET, [](AsyncWebServerRequest * request) {
    request->send(SPIFFS, "/leaflet.js", "text/javascript");
  });
  // Start server
  server.begin();
}
void loop() {
//  Serial.println(controlBuildingStatus());
}
