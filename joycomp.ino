// JoyStick Shield pins
const int A_pin = 2, B_pin = 3, C_pin = 4, D_pin = 5;
const int E_pin = 6, F_pin = 7, JoyStick_pin = 8;
const int X_pin = A1, Y_pin = A0;
const int buttons[] = { A_pin, B_pin, C_pin, D_pin, E_pin, F_pin, JoyStick_pin };

void setup() {
  for (int i = 0; i < 7; i++) {
    pinMode(buttons[i], INPUT);
  }
  
  Serial.begin(115200);
}

void loop() {
  int x = analogRead(X_pin) - 512;
  int y = analogRead(Y_pin) - 512;
  
  int buttonStates = 0;

  if (digitalRead(8) == HIGH){
    buttonStates = 64;
  }  else {
    buttonStates = 0;
  }

  Serial.println("S" + String(x) + "," + String(y) + "," + String(buttonStates));

  delay(40);
}
