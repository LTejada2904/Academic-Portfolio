#include <LiquidCrystal.h>

// Traffic Light 1
#define red 13
#define yellow 12
#define green 11
#define cross 10
#define button 3
#define a 4
#define b 1
#define c 5
#define d 6
#define e 7
#define f 8
#define g 9

// Traffic Light 2
#define cross2 17
#define red2 14
#define yellow2 15
#define green2 16
#define button_2 2
#define a2 33
#define b2 35
#define c2 31
#define d2 29
#define e2 27
#define f2 25
#define g2 23

#define Delay_time 500
#define Countdown 100
#define Green_time 5
#define Yellow_time 3
#define Red_time 5

volatile int button_state = 0;
int i = 0;
int Flag;
int Flag2;
int Light_State;

LiquidCrystal lcd(8, 9, 4, 5, 6, 7); // Declare the lcd object

void setup() {
  pinMode(cross, OUTPUT);
  pinMode(red, OUTPUT);
  pinMode(yellow, OUTPUT);
  pinMode(green, OUTPUT);
  pinMode(cross2, OUTPUT);
  pinMode(red2, OUTPUT);
  pinMode(yellow2, OUTPUT);
  pinMode(green2, OUTPUT);

  pinMode(a, OUTPUT);
  pinMode(b, OUTPUT);
  pinMode(c, OUTPUT);
  pinMode(d, OUTPUT);
  pinMode(e, OUTPUT);
  pinMode(f, OUTPUT);
  pinMode(g, OUTPUT);
  pinMode(a2, OUTPUT);
  pinMode(b2, OUTPUT);
  pinMode(c2, OUTPUT);
  pinMode(d2, OUTPUT);
  pinMode(e2, OUTPUT);
  pinMode(f2, OUTPUT);
  pinMode(g2, OUTPUT);

  pinMode(button, INPUT);
  pinMode(button_2, INPUT);
  attachInterrupt(0, SetFlag, CHANGE); // Attached the Interrupt subroutine
  attachInterrupt(1, SetFlag2, CHANGE); // Attached the Interrupt subroutine
  Serial.begin(9600);
  Flag = 0;
  Flag2 = 0;

  lcd.begin(16, 2); // Adjust these parameters based on your LCD configuration
  lcd.clear();
  lcd.print("Traffic Light");
}

void loop() {
  LOOP:
  // Set the state flag, 1=green, 2=yellow, and 3=red
  // Set Green ON, ref, and Yellow OFF
  // Green State for the first traffic light
  digitalWrite(red, LOW);
  digitalWrite(yellow, LOW);
  digitalWrite(green, HIGH);
  digitalWrite(cross, LOW);

  // red State for the second traffic light
  digitalWrite(red2, HIGH);
  digitalWrite(yellow2, LOW);
  digitalWrite(green2, LOW);
  digitalWrite(cross2, LOW);

  for (i = 0; i <= Green_time; i++) {
    delay(Delay_time);
    if (Flag == 1 || Flag2 == 1) {
      Light_State = 1;
      Pedestian();
      goto LOOP;
    }
  }

  // Yellow State just for the first traffic light
  digitalWrite(green, LOW);
  digitalWrite(yellow, HIGH);

  for (i = 0; i <= Yellow_time; i++) {
    delay(Delay_time);
    if (Flag == 1 || Flag2 == 1) {
      Light_State = 2;
      Pedestian();
      goto LOOP;
    }
  }

  // Red State just for the first traffic light
  digitalWrite(yellow, LOW);
  digitalWrite(red, HIGH);

  for (i = 0; i <= Red_time; i++) {
    delay(Delay_time);
    if (Flag == 1 || Flag2 == 1) {
      Light_State = 3;
      Pedestian();
      goto LOOP;
    }
  }

  // Green State for the second traffic light
  digitalWrite(red2, LOW);
  digitalWrite(green2, HIGH);

  for (i = 0; i <= Green_time; i++) {
    delay(Delay_time);
    if (Flag == 1 || Flag2 == 1) {
      Light_State = 4;
      Pedestian();
      goto LOOP;
    }
  }

  // Yellow State for the second traffic light
  digitalWrite(green2, LOW);
  digitalWrite(yellow2, HIGH);

  for (i = 0; i <= Red_time; i++) {
    delay(Delay_time);
    if (Flag == 1 || Flag2 == 1) {
      Light_State = 5;
      Pedestian();
      goto LOOP;
    }
  }

  // Red State for the second traffic light
  digitalWrite(yellow2, LOW);
  digitalWrite(red2, HIGH);

  for (i = 0; i <= Red_time; i++) {
    delay(Delay_time);
    if (Flag == 1 || Flag2 == 1) {
      Light_State = 6;
      Pedestian();
      goto LOOP;
    }
  }
}

void SetFlag(void) {
  Flag = 1;
}

void SetFlag2(void) {
  Flag2 = 1;
}

void Pedestian(void) {
  switch (Light_State) {
    case 1: { // Green state
      if (Flag2 == 1) {
        lcd.clear();
        lcd.print("Traffic Light");
        lcd.setCursor(0, 1);
        lcd.print("Do not cross yet");
        break;
      } else if (Flag == 1) {
        lcd.clear();
        lcd.print("Traffic Light");
        lcd.setCursor(0, 1);
        lcd.print("Stop Pedestrian");
        digitalWrite(green, LOW); // off Green set Yellow
        digitalWrite(yellow, HIGH);
        delay(2000);
        // Set Red on in the first traffic light and Pedestrian on
        lcd.clear();
        lcd.print("Traffic Light");
        lcd.setCursor(0, 1);
        lcd.print("Stop Pedestrian");
        digitalWrite(yellow, LOW); // off Green set Yellow
        digitalWrite(red, HIGH);

        digitalWrite(red2, LOW);
        digitalWrite(green2, HIGH);
        digitalWrite(cross, HIGH);
        delay(5000);
        break;
      }
    }
    case 2: { // Yellow state
      if (Flag2 == 1) {
        lcd.clear();
        lcd.print("Traffic Light");
        lcd.setCursor(0, 1);
        lcd.print("Wait Pedestrian");
        break;
      } else if (Flag == 1) {
        delay(500);
        delay(1000);
        // Set Red on and Pedestrian on
        lcd.clear();
        lcd.print("Traffic Light");
        lcd.setCursor(0, 1);
        lcd.print("Stop Pedestrian");
        digitalWrite(yellow, LOW); // off Green set Yellow
        digitalWrite(red, HIGH);
        digitalWrite(cross, HIGH);
        digitalWrite(red2, LOW);
        digitalWrite(green2, HIGH);
        delay(5000);
        break;
      }
    }
    case 3: { // Pedestrian on, red on
      if (Flag2 == 1) {
        lcd.clear();
        lcd.print("Traffic Light");
        lcd.setCursor(0, 1);
        lcd.print("Now you can cross");
        digitalWrite(cross2, HIGH);
        delay(2000);
        digitalWrite(green2, LOW); // off Green set Yellow for the second traffic light
        digitalWrite(yellow2, HIGH);
        delay(2000);
        digitalWrite(yellow2, LOW);
        digitalWrite(red2, HIGH);
        digitalWrite(red, LOW);
        digitalWrite(green, HIGH);
        delay(2000);
        break;
      } else if (Flag == 1) {
        lcd.clear();
        lcd.print("Traffic Light");
        lcd.setCursor(0, 1);
        lcd.print("Stop Pedestrian");
        digitalWrite(cross, HIGH);
        delay(2000);
        digitalWrite(red2, LOW);
        digitalWrite(green2, HIGH);
        digitalWrite(cross, HIGH);
        delay(2000);
        break;
      }
    }
    case 4: { // Green state second traffic light
      if (Flag2 == 1) {
        delay(2000);
        lcd.clear();
        lcd.print("Traffic Light");
        lcd.setCursor(0, 1);
        lcd.print("Wait Pedestrian");
        digitalWrite(green2, LOW);
        digitalWrite(yellow2, HIGH);
        delay(2000);
        digitalWrite(yellow2, LOW);
        digitalWrite(red2, HIGH);
        digitalWrite(red, LOW);
        digitalWrite(green, HIGH);
        digitalWrite(cross2, HIGH);
        delay(2000);
        break;
      } else if (Flag == 1) {
        digitalWrite(cross, HIGH);
        delay(2000);
        break;
      }
    }
    case 5: { // Yellow State for the second traffic light
      if (Flag2 == 1) {
        digitalWrite(cross2, HIGH);
        delay(2000);
        lcd.clear();
        lcd.print("Traffic Light");
        lcd.setCursor(0, 1);
        lcd.print("abc");
        digitalWrite(yellow2, LOW);
        digitalWrite(red2, HIGH);
        digitalWrite(red, LOW);
        digitalWrite(green, HIGH);
        delay(2000);
        break;
      } else if (Flag == 1) {
        delay(1000);
        digitalWrite(cross, HIGH);
        delay(1000);
        digitalWrite(yellow2, LOW);
        digitalWrite(red2, HIGH);
        digitalWrite(red, LOW);
        digitalWrite(green, HIGH);
        delay(2000);
        digitalWrite(green, LOW);
        digitalWrite(yellow, HIGH);
        delay(2000);
        digitalWrite(yellow, LOW);
        digitalWrite(red, HIGH);
        digitalWrite(red2, LOW);
        digitalWrite(green2, HIGH);
        delay(1000);
        break;
      }
    }
    case 6: { // Red state second traffic light
      if (Flag2 == 1) {
        digitalWrite(cross2, HIGH);
        delay(1000);
        lcd.clear();
        lcd.print("Traffic Light");
        lcd.setCursor(0, 1);
        lcd.print("Do not cross yet");
        digitalWrite(red, LOW);
        digitalWrite(green, HIGH);
        delay(1000);
        break;
      } else if (Flag == 1) {
        digitalWrite(cross, HIGH);
        delay(1000);
        digitalWrite(red, LOW);
        digitalWrite(green, HIGH);
        delay(2000);
        digitalWrite(green, LOW);
        digitalWrite(yellow, HIGH);
        delay(2000);
        digitalWrite(yellow, LOW);
        digitalWrite(red, HIGH);
        digitalWrite(red2, LOW);
        digitalWrite(green2, HIGH);
        delay(1000);
        break;
      }
    }
    default: {};
  }

  if (Flag == 1) {
    for (i = 0; i <= 5; i++) {
      lcd.clear();
      lcd.print("Traffic Light");
      lcd.setCursor(0, 1);
      lcd.print("Now you can cross");
      digitalWrite(cross, LOW);
      delay(1000);
      digitalWrite(cross, HIGH);
      delay(1000);
    }
  } else if (Flag2 == 1) {
    for (i = 0; i <= 5; i++) {
      lcd.clear();
      lcd.print("Traffic Light");
      lcd.setCursor(0, 1);
      lcd.print("Now you can cross");
      digitalWrite(cross2, LOW);
      delay(1000);
      digitalWrite(cross2, HIGH);
      delay(1000);
    }
  }

  if (Flag == 1) {
    delay(1000);
    digitalWrite(cross, LOW);
    digitalWrite(green2, LOW);
    digitalWrite(yellow2, HIGH);
    delay(2000);
    digitalWrite(yellow2, LOW);
    digitalWrite(red2, HIGH);
    delay(2000);
  }
  Flag = 0;
  Flag2 = 0;
  lcd.clear();
  lcd.print("Traffic Light");
}
