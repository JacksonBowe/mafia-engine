import random
import time

import engine as Mafia

PLAYERS = [
    {
        "id": "1",
        "name": "Player 1",
        "alias": "Brandon",
    },
    {
        "id": "2",
        "name": "Player 2",
        "alias": "Gordon",
    },
    {
        "id": "3",
        "name": "Player 3",
        "alias": "Dog",
    },
    {
        "id": "4",
        "name": "Player 4",
        "alias": "Jackson",
    },
    {
        "id": "5",
        "name": "Player 5",
        "alias": "Scrooge",
    },
    {
        "id": "6",
        "name": "Player 6",
        "alias": "Rory",
    },
    {
        "id": "7",
        "name": "Player 7",
        "alias": "Muck",
    },
    {
        "id": "8",
        "name": "Player 8",
        "alias": "Dinkle",
    },
    {
        "id": "9",
        "name": "Player 9",
        "alias": "Bertha",
    },
    {
        "id": "10",
        "name": "Player 10",
        "alias": "Kody",
    },
    {
        "id": "11",
        "name": "Player 11",
        "alias": "Car",
    },
    {
        "id": "12",
        "name": "Player 12",
        "alias": "Mick",
    },
    {
        "id": "13",
        "name": "Player 13",
        "alias": "Bronson",
    },
    {
        "id": "14",
        "name": "Player 14",
        "alias": "Wesley",
    },
    {
        "id": "15",
        "name": "Player 15",
        "alias": "Brett",
    },
]

CONFIG = {
    "tags": [
        "Citizen",  # "town_government",
        "Doctor",  # "town_protective",
        "Doctor",  # "town_protective",
        "BodyGuard",  # "town_power",
        "Detective",  # "town_investigative",
        "Bodyguard",  # "town_killing",
        "Detective",  # "town_investigative",
        "town_random",
        "Godfather",  # "Godfather",
        "Mafioso",  # "mafia_deception",
        "Mafioso",  # "mafia_support",
        "neutral_evil",
        "neutral_benign",
        "neutral_random",
        "any_random",
    ],
    "settings": {},
    "roles": {
        "Citizen": {"max": 0, "weight": 1, "settings": {"maxVests": 2}},
        # "Mayor": {
        #     "max": 0,
        #     "weight": 1,
        #     "settings": {
        #     }
        # },
        "Doctor": {"max": 3, "weight": 1, "settings": {}},
        # "Detective": {
        #     "max": 1,
        #     "weight": 1,
        #     "settings": {}
        # },
        "Godfather": {"max": 1, "weight": 1, "settings": {}},
        "Bodyguard": {"max": 3, "weight": 1, "settings": {}},
        "Mafioso": {"max": 2, "weight": 1, "settings": {}},
    },
}

EVENT_SLEEP_MAP = {
    "mafia_kill_success": 3,
    "mafia_kill_fail": 3,
    "bodyguard_shootout": 3,
}


def process_events(events, root=True):
    for item in events:
        time.sleep(0.5)
        if "group_id" in item:
            process_events(item["events"], root=False)
        elif "event_id" in item:
            print("{}: {}".format(item["targets"], item["message"]))
            if item["event_id"] in EVENT_SLEEP_MAP:
                time.sleep(EVENT_SLEEP_MAP[item["event_id"]])

        # if root:
        #     time.sleep(item["duration"])
        #     print()
    # for event in events:
    #     if "events" in event:
    #         process_events(event["events"])
    #     else:
    #         print("{}: {}".format(event["targets"], event["message"]))
    # print(events)
    # print()
    # if "duration" in events:
    #     print("here")
    #     time.sleep(event["duration"])


def print_deaths(state):
    pass


def main():
    game = Mafia.new_game(PLAYERS, CONFIG)
    deaths = []
    while not game.check_for_win():
        print("Day:", game.day)

        # Dump the existing state
        players = game.dump_actors()
        state = game.dump_state()

        deaths = [player for player in state["graveyard"] if player["dod"] == game.day]
        for death in deaths:
            print(f"{death['alias']} died. Cause of death: {death['cod']}")
            # time.sleep(3)

        for player in players:
            if "possibleTargets" not in player:
                continue

            for pt_list in player["possibleTargets"]:
                if player["role"] == "Citizen":
                    if not random.choice([True, False]):
                        continue

                player["targets"].append(random.choice(pt_list))

        # Perform the actions
        game = Mafia.load_game(players, CONFIG, state)
        game.resolve()

        events = game.events.dump()

        print("Night", game.day - 1)
        process_events(events)

        print()


if __name__ == "__main__":
    main()
