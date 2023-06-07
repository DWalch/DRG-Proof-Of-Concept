#include <Wire.h>
#include <Adafruit_MLX90614.h>
//create The temperature sensor object and assign emmisivity value
//Important Emmisivity Values
//Ashphalt: 0.93
//Gravel: 0.28
//Dirt: 0.90 - 0.95
//Snow: 0.96 - 0.98
//Ice smooth: 0.966
//Ice rough: 0.985
Adafruit_MLX90614 mlx = Adafruit_MLX90614();


//run initial setup script for the arduino
//Tell Arduino to begin Serial reading and to check the temperature sensor if it is initialized
void setup() {
  Serial.begin(9600);
  mlx.begin();
}
//This is the main arduino loop that will run until the arduino is shut off or loses power
void loop() {
  //Read the object temperature and ambient temperature in celcius
  float temp = mlx.readObjectTempC();
  float temp2 = mlx.readAmbientTempC();
  //Print the temperatures in serial
  Serial.print(temp);
  Serial.print(","); // separate temperature data by comma
  Serial.print(temp2);
  Serial.print("\n");
  delay(10000); // wait for 10 seconds to read data again

  
}