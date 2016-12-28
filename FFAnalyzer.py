import itertools

inputFile = open("input.txt", "r");

for line in inputFile:
    totalPoints = float(0.0);
    cols = line.split(" ");
    name = cols[0] + " " + cols[1];
    position = cols[2];
    games = int(cols[3]);
    receptions = float(cols[4]);
    targets = float(cols[5]);
    tds = int(cols[6]);

    for game in itertools.islice(cols, 9, len(cols)-1):
        totalPoints += float(game);

    pointsPerGame = totalPoints/games;

    print("Name: " + name);
    print("Total Points: " + str(totalPoints));
    print("Points per Game: " + str(pointsPerGame));
    print("");


