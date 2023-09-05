int ledFirst = 4;
int ledSecond = 5;
int ledGreen = 7;
int buttonLeft = 3;
int buttonRight = 6;
int stanLeft = LOW;
int stanRight = LOW;
int stanGreen = HIGH;
long rndm;
int i = 0;

void setup()
{
  Serial.begin(9600);
  pinMode(ledSecond, OUTPUT);
  pinMode(ledFirst, OUTPUT);
  pinMode(ledGreen, OUTPUT);
  pinMode(buttonLeft, INPUT);
  pinMode(buttonRight, INPUT);
  digitalWrite(ledGreen, stanGreen);
}

void loop()
{
  randomSeed(millis());
  stanLeft = digitalRead(buttonLeft);
  stanRight = digitalRead(buttonRight);

  if (i == 0)
  {
    digitalWrite(ledGreen, stanGreen);
    rndm = random(2000, 7000);
    Serial.println("zaswieca sie zielona");
    delay(rndm);
    stanGreen = !stanGreen;
    Serial.println("gasnie zielona");
    digitalWrite(ledGreen, stanGreen);
    i++;
  }

  while (Serial.available()) {
    char command = Serial.read(); 
    if (command == 'L' && stanGreen == LOW) {
      stanLeft = !stanLeft;
    }
    else if (command == 'R' && stanGreen == LOW) {
      stanRight = !stanRight;
    }
  }

  if (stanGreen == LOW);
  {
    if (stanLeft == HIGH)
    {
      Serial.println("wygral gracz 1");
      digitalWrite(ledFirst, HIGH);
      Serial.println("zaswieca sie czerwona 1");
      delay(2500);
      digitalWrite(ledFirst, LOW);
      stanGreen = !stanGreen;
      i = 0;
      Serial.println("gasnie czerwona 1");
    }
    if (stanRight == HIGH)
    {
      Serial.println("wygral gracz 2");
      digitalWrite(ledSecond, HIGH);
      Serial.println("zaswieca sie czerwona 2");
      delay(2500);
      digitalWrite(ledSecond, LOW);
      stanGreen = !stanGreen;
      i = 0;
      Serial.println("gasnie czerwona 2");
    }
  }
}
