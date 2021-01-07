# Baseline
1. for every house calculate the distance to every battery
2. choose the shortest distance and create a cable between house and battery
3. calculate the total output of every battery
4. for every battery with overflow (total output > capacity):
    1. pick random house
    2. connect it to the shortest distance battery without overflow
    3. repeat till this battery no longer overflows
5. go to next battery until no batties have overflow
