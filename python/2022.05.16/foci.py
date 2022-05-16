#egy bajnokságban egy csapat hazai meccseinek eredményeinek szimulációjáa
import random

team_count = int(input("Bajnokságban szereplő csapatok száma:" ))

for i in range(1, team_count):
    home_goals = random.randint(0, 8)
    guest_goals = random.randint(0, 8)
    print(f"{i}. hazai mérkőzés: {home_goals}, {guest_goals}")