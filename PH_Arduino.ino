#include <Adafruit_MLX90614.h>
#include <Wire.h>
#define USE_ARDUINO_INTERRUPTS true    // Set-up low-level interrupts for most acurate BPM math.
#include <PulseSensorPlayground.h>     // Includes the PulseSensorPlayground Library.   
Adafruit_MLX90614 mlx = Adafruit_MLX90614(); 


//  Variables
const int PulseWire = 0;       // PulseSensor PURPLE WIRE connected to ANALOG PIN 0
const int LED13 = 13;          // The on-board Arduino LED, close to PIN 13.
int Threshold = 550;  
unsigned long currentMillis;
float T=0;
int B=0;

PulseSensorPlayground pulseSensor; 

void setup() {
  pinMode(4,INPUT);
  pinMode(3,INPUT);
  Serial.begin(9600);
  mlx.begin();  
  pulseSensor.analogInput(PulseWire);   
  pulseSensor.blinkOnPulse(LED13);       //auto-magically blink Arduino's LED with heartbeat.
  pulseSensor.setThreshold(Threshold);   

  // Double-check the "pulseSensor" object was created and "began" seeing a signal. 
  if (pulseSensor.begin()) {
    //Serial.println("0|0");  //This prints one time at Arduino power-up,  or on Arduino reset.  
  }

}

void loop() {
  
  if((digitalRead(3)==1)||(digitalRead(4)==1)){
    Serial.println("Null");  
  }
  
  else 
  {
    currentMillis=millis();
    while(millis()-currentMillis<=15000UL)
    { 
      int Beat=analogRead(A1);
      Serial.println(String(Beat));
      delay(100);
    }
    Serial.println("-1");
    Serial.println("-1");
    while(true)
    {
      T=mlx.readObjectTempF();
      //Serial.println("test temp"); 
      int myBPM = pulseSensor.getBeatsPerMinute();  // Calls function on our pulseSensor object that returns BPM as an "int".
                                               // "myBPM" hold this BPM value now. 

      if (pulseSensor.sawStartOfBeat()) {            // Constantly test to see if "a beat happened".                     // Print phrase "BPM: " 
        B=myBPM;   
        if (B<40)
        {
          B=0;         
        }
        if (B>200)// Print the value inside of myBPM.
        {
          B=0; 
        }
      }
      
      Serial.println(String(T)+"|"+String(B));
      delay(100);
    }
      


  }
  delay(10);
  Serial.end();
  delay(10);
}

