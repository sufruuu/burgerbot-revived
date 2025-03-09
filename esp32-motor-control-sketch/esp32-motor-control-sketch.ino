/*
  ESP32 Differential Drive with L298N Motor Driver
  Commands via Serial:
    F - Move Forward
    B - Move Backward
    L - Turn Left (stop left motor, right motor runs forward)
    R - Turn Right (stop right motor, left motor runs forward)
    S - Stop
*/

// Motor pin assignments (update these pins based on your wiring)
const int ENA = 5;   // Left motor enable
const int IN1 = 18;  // Left motor input 1
const int IN2 = 19;  // Left motor input 2

const int ENB = 32;  // Right motor enable
const int IN3 = 33;  // Right motor input 1
const int IN4 = 25;   // Right motor input 2

void setup() {
  // Initialize Serial communication at 115200 baud
  Serial.begin(115200);

  // Configure motor control pins as outputs
  pinMode(ENA, OUTPUT);
  pinMode(IN1, OUTPUT);
  pinMode(IN2, OUTPUT);
  pinMode(ENB, OUTPUT);
  pinMode(IN3, OUTPUT);
  pinMode(IN4, OUTPUT);

  // Enable both motors at full speed (digital HIGH since no speed control is used)
  digitalWrite(ENA, HIGH);
  digitalWrite(ENB, HIGH);

  // Ensure motors are stopped at startup
  stopMotors();
}

void loop() {
  // Check if there is serial data available
  if (Serial.available() > 0) {
    char command = Serial.read();

    // Process the command using a switch statement
    switch (command) {
      case 'w': // Move Forward
        moveForward();
        Serial.println("Moving Forward");
        break;
      case 's': // Move Backward
        moveBackward();
        Serial.println("Moving Backward");
        break;
      case 'a': // Turn Left
        turnLeft();
        Serial.println("Turning Left");
        break;
      case 'd': // Turn Right
        turnRight();
        Serial.println("Turning Right");
        break;
      case 'x': // Stop
        stopMotors();
        Serial.println("Stop");
        break;
      default:
        Serial.print("Unknown command: ");
        Serial.println(command);
        break;
    }
  }
}

// Function to drive both motors forward
void moveForward() {
  // Left motor forward: IN1 HIGH, IN2 LOW
  digitalWrite(IN1, HIGH);
  digitalWrite(IN2, LOW);
  
  // Right motor forward: IN3 HIGH, IN4 LOW
  digitalWrite(IN3, HIGH);
  digitalWrite(IN4, LOW);
}

// Function to drive both motors backward
void moveBackward() {
  // Left motor backward: IN1 LOW, IN2 HIGH
  digitalWrite(IN1, LOW);
  digitalWrite(IN2, HIGH);
  
  // Right motor backward: IN3 LOW, IN4 HIGH
  digitalWrite(IN3, LOW);
  digitalWrite(IN4, HIGH);
}

// Function to turn left by stopping the left motor and running the right motor forward
void turnLeft() {
  // Stop left motor
  digitalWrite(IN1, LOW);
  digitalWrite(IN2, LOW);
  
  // Right motor forward
  digitalWrite(IN3, HIGH);
  digitalWrite(IN4, LOW);
}

// Function to turn right by stopping the right motor and running the left motor forward
void turnRight() {
  // Left motor forward
  digitalWrite(IN1, HIGH);
  digitalWrite(IN2, LOW);
  
  // Stop right motor
  digitalWrite(IN3, LOW);
  digitalWrite(IN4, LOW);
}

// Function to stop both motors
void stopMotors() {
  digitalWrite(IN1, LOW);
  digitalWrite(IN2, LOW);
  digitalWrite(IN3, LOW);
  digitalWrite(IN4, LOW);
}
