Project: SmartGrid
Groep: SmartTeam25

Voor de baseline is een verdeling van willekeurige oplossingen weergeven. Het algoritme kiest een willekeurig huis en verbindt deze aan een willekeurige batterij. Als door het toekennen van dit huis de overgebleven capaciteit van de batterij wordt overschreden, wordt er willekeurig een andere batterij gekozen. Dit proces wordt herhaald tot alle huizen zijn toegekend. Dit is een enkele iteratie en levert een willekeurige oplossing met een bijbehorende prijs voor de wijk op. Om een verdeling van willekeurige oplossingen te krijgen wordt dit proces gedurende een bepaalde tijd herhaald.  

In figuur 1 is een verdeling van oplossingen te zien voor wijk 1. Deze heeft een runtime van 120 minuten en bevat ca 340.000 iteraties. Dit geeft een goede weergave van de ruimte van oplossingen (‘state space’).  

In figuur 3 is een verdeling te zien van oplossingen voor wijk 3, welke verkregen zijn met een runtime van 20 minuten. Dit zijn ca 83.000 iteraties. Door een gering verschil tussen capaciteit en output en het feit dat de output van alle huizen minder gespreid is, is het met een willekeurige verdeling lastig om een oplossing te vinden. Hierdoor is het met dezelfde runtime als in Wijk 2 (figuur 2) lastiger is om een oplossing te vinden. 

