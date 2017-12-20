# RealTimeSignLanguageRecognition

#Članovi tima
SW 85/2017 Aleksandar Đurić
SW 86/2017 Dara Jovanović
SW 90/2017 Milica Lazić

#Definicija problema
Detektovanje znakovnog jezika sa snimka.

#Motivacija problema
Olakšavanje svakodnevne komunikacije sa gluvo-nemim osobama.

#Skup podataka
Podaci za obuku će biti ručno napravljeni. Sami ćemo napraviti set fotografija za svako slovo iz alfabeta, kao i set fotografija koje ne predstavljaju nikakav konkretan znak.

#Metodologije
Python
OpenCV
CNN
Za izdvajanje šake od pozadine slike koristimo ThensorFlow object detection. Prvo prevodimo sliku u crno-belu, gde je šaka crne boje, a pozadina bela (ili obrnuto). Na osnovu centra mase, šaku možemo da izrežemo sa slike. Nakon toga vršimo predikciju slova alfabeta.

#Metod evaluacije
Validacija rešenja će se vršiti na osnovu test skupa slika, gde svaka slika predstavlja slovo alfabeta.
