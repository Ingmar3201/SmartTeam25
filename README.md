# Smart Grid 

Dit programma optimaliseert de infrastructruur in een woonwijk om overtollige groene energie, geproduceerd door zonnepanelen op daken van woonhuizen, tijdelijk op te slaan.

## De Case

Ieder huis in de betreffende woonwijk heeft zonnepanelen op het dak die zorgen voor de benodigde energie. In het geval dat de zonnepanelen méér energie opleveren dan de bewoners nodig hebben, wordt via een stroomkabel de overtollige energie naar een batterij geleid, zodat de energie later als nog gebruikt kan worden. Deze batterijen staan op vaste plekken in de woonwijk opgesteld. 

Het doel van de case:
- Elk huis met een batterij verbinden
- Een zo goedkoop mogelijke configuratie vinden

Kosten:
- Kabel: 9 euro per kabelsegment
- Batterij: 5000 euro per batterij

Specificaties:
- Elk huis heeft een vaste energie output
- Elke batterij heeft een vaste maximale capaciteit 
- Huizen en batterijen mogen niet verplaatst worden
- Kabelsegmenten mogen gedeeld worden

### Structuur

Alle Python scripts staan in de folder code. Deze is verder opgedeeld in
- Algorithms: classes met algoritmes
- Classes: classes met objecten voor wijk, huizen, batterijen en kabels
- Visualisation: script voor weergave van de oplossing
In de map Data zitten alle input waardes en in de map resultaten worden alle resultaten opgeslagen door de code.

## Algoritmen

### Beginoplossing

De beginoplossing - Initial Solution - is een door ons gegenereerde startoplossing waarop vervolgens onze optimalisatiealgoritmen kunnen worden losgelaten. De beginoplossing soorteert de huizen op basis van energie output: van groot naar klein. Van groot naar klein wordt er vervolgens gekeken welke batterij voor dat huis het dichtst bij is. Indien mogelijk binnen de capaciteit van de betreffende batterij, wordt het huis verbonden. Zo niet, wordt er gekeken naar de op een na dichtstbijzijnde batterij (en zo verder). Mocht het aan het eind van dit proces niet 'uitkomen'. Worden, in dit geval van klein naar groot, huizen weer losgekoppeld en opnieuw herverdeeld. Dit gaat door tot alle huizen verbonden zijn.

### Eerste Algoritme: Random Swap

Dit algoritme neemt van de beginoplossing twee willekeurige huizen en kijkt of deze gewisseld kunnen worden binnen de capaciteiten van de bijbehorende batterijen. Als het mogelijk is worden ze gewisseld. Met het wisselen van twee huizen verandert ook de totale prijs van de wijk. Door alleen maar wissels van huizen toe te staan als daardoor de prijs zou dalen, zou al snel een lokaal minimum kunnen worden berijkt. In plaats daarvan is een limiet ingesteld (bijvoorbeeld 1.2 keer de prijs van de beginoplossing). Na elke wissel van twee huizen wordt gecontroleerd of de limietprijs wordt overschreden. Als dat het geval is, gaat het algoritme opnieuw proberen vanaf de beginoplossing. Als de prijs van de wijk láger is dan de prijs van de beginoplossing, wordt de goedkopere configuratie opgeslagen.

### Tweede Algoritme: Density

Dit algoritme gaat op een andere manier de beginoplossing aanpassen. Per batterij wordt voor elk bijbehorend huis een totale afstand tot alle andere bijbehorende huizen berekend. Deze waarde zegt dus iets over de ligging van het betreffende huis, ten opzichte van de andere huizen van die batterij. Vervolgens wordt een grenswaarde bepaald, waarvoor geldt dat een huis met een grótere totale afstand dan deze grenswaarde, wordt losgekoppeld van de batterij. Hierdoor zijn de huizen die 'het verst weg liggen' van de andere huizen, nu losgekoppeld. Van de huizen die nog wel vast zitten aan de batterij wordt een middelpunt bepaald. Op dit punt is de 'huisdichtheid' het hoogst. 
De volgende stap is om te kijken naar de losgekoppelde huizen en deze op nieuw in te delen bij een batterij. Er wordt hiervoor gekeken naar de berekende middelpunten. Het losgekoppelde huis wordt aan de batterij toegevoegd die hoort bij de huizen waarvan het middelpunt het dichtstbij het betreffende losgekoppelde huis ligt. Op deze manier worden de huizen zo onderverdeeld dat per batterij alle huizen bij elkaar in de buurt liggen. Dit is belangrijk voor de volgende stap: kabels delen.

### Vervolg Tweede Algoritme: Share Cables

De huizen liggen nu gegroepeerd en veel kabels liggen parralel aan elkaar. Dat komt doordat een kabel van punt A naar punt B zo wordt gelegd, dat eerst de gehele afstand in de x-richting wordt afgelegd en vervolgens de gehele afstand in de y-richting wordt afgelegd. Als een groep huizen links of rechts (x-richting) van de batterij ligt, zullen veel kabels parralel in de x-richting naar de batterij toe lopen en ter hoogte van de batterij over de y-as naar boven of beneden lopen. Het doel van dit algoritme is zo veel mogelijk kabels in de x-richting te laten overlappen, waardoor kosten worden gereduceerd. 

Het algoritme loopt per huis over de kabel richting de batterij. Dit begint vrijwel altijd in de x-richting omdat de kabel daar eerst is aangelegd. Voor elk stapje op de kabel wordt er in de y-richting, een stapje omhoog en een stapje omlaag, gekeken of er een huis van dezelfde batterij staat. Als dit zo is wordt er een kabel naar dat huis gelegd en de kabel die eerst naar de batterij lag verwijderd. Dit wordt herhaald voor alle huizen. Vervolgens wordt dit meermaals herhaald, maar met een toenemend aantal stapjes op de y-as. Bij een volgende keer wordt er dus twee stapjes boven en twee stapjes onder de kabel gekeken naar een 'buurhuis' om een kabel aan te verbinden. Dan drie, vier, en zo voorts.

Een kabel naar een huis dat dichterbij ligt dan de batterij is altijd goedkoper dan een kabel naar de batterij, dus per definitie wordt de configuratie na een wissel goedkoper. Als er meerdere keren geen goedkopere configuratie gevonden is, stopt het algoritme. 

Ook kan het zijn dat er met vier stapjes in de y-richting een goedkopere oplossing gevonden werd dan met bijvoorbeeld vijf of zes stapjes. In dat geval wordt de goedkopste configuratie van vier stapjes opgeslagen en geprint dat dit zo is. 

## Vereisten 

Deze codebase is volledig geschreven in [Python3.8.3](https://www.python.org/downloads/). In requirements.txt staan alle benodigde packages om de code succesvol te draaien. Deze zijn gemakkelijk te installeren via pip dmv. de volgende instructie:

```
pip install -r requirements.txt
```

## Test 

Om de code te draaien met de standaardconfiguratie (bv. brute-force en voorbeeld.csv) gebruik de instructie:

```
python main.py
```

## Auteurs

* Ingmar de Mare
* Koen Smallegange
* Freek Temming

