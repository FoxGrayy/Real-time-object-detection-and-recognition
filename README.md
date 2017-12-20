Real time object detection and recognition
======
Članovi tima
===
SW 85/2017 Aleksandar Đurić
SW 86/2017 Dara Jovanović
SW 90/2017 Milica Lazić

Definicija problema
===
Detektovanje 15 različitih vrsta objekata sa video snimka.

Motivacija problema
===
Prepoznavanje objekata određenog tipa

Skup podataka
===
Podaci za obuku se koriste iz dataset-a
http://cocodataset.org/#...

Metodologije
===
Python
OpenCV
CNN
Za  izdvajanje objekta od pozadine slike koristimo ThensorFlow object detection.
Prvo prevodimo sliku u crno-belu, gde je objekat crne boje, a pozadina bela (ili obrnuto). Na osnovu centra mase, objekat možemo da izrežemo sa slike. Nakon toga imenujemo objekat.

Metod evaluacije
===
Validacija rešenja će se vršiti na osnovu test skupa sa video klipova.
