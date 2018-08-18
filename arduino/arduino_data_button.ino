int person_button = 3;
int dog_button =4;
int dog_counter = 0;
int person_counter = 0;
int buttonStateP;
int lastButtonStateP =LOW;
unsigned long lastTimeP = 0;
unsigned long delayTimeP = 80;
int buttonStateD;
int lastButtonStateD =LOW;
unsigned long lastTimeD = 0;
unsigned long delayTimeD = 80;


void setup() {
  // put your setup code here, to run once:
  Serial.begin(9600);
  pinMode(person_button, INPUT_PULLUP);
  pinMode(dog_button, INPUT_PULLUP);
  analogReference(INTERNAL);

}

void loop() {
  // put your main code here, to run repeatedly:
  int button_readD = digitalRead(dog_button);
  int button_readP = digitalRead(person_button);
  bool person = false;
  bool dog = false;
  if(button_readD == LOW){
    dog = true;
  }
  if(button_readP == LOW){
    person = true;
  }
  if(dog != lastButtonStateD){
    lastTimeD = millis();
  }
  if((millis() - lastTimeD) > delayTimeD){
    if(dog != buttonStateD){
      buttonStateD = dog;
    }
    if(buttonStateD == true){
        dog_counter+=1;
        Serial.print("Dog Count:");
        Serial.println(dog_counter);
    }
    
    lastButtonStateD = button_readD;
  }
  if(person != lastButtonStateP){
    lastTimeP = millis();
  }
  if((millis() - lastTimeP) > delayTimeP){
    if(person != buttonStateP){
      buttonStateP = person;
    }
    if(buttonStateP == true){
        person_counter+=1;
        Serial.print("Person Count:");
        Serial.println(person_counter);
    }
    
    lastButtonStateP = button_readP;
  }
  
}



