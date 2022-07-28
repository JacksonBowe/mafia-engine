


import logging
from roles.citizen import Citizen
from roles.mafioso import Mafioso


def test_citizen_find_allies():
    logging.info("Running test: citizen_find_allies")
    citizen = Citizen({"alias": "test_citizen", "number": "1"})
    citizen_2 = Citizen({"alias": "test_citizen_2", "number": "2"})
    mafioso = Mafioso({"alias": "test_mafioso", "number": "3"})
    
    citizen.find_allies([citizen, citizen_2, mafioso])
    
    # Check number of allies
    assert len(citizen.allies) == 0, f"{citizen} should have 0 allies"

    logging.info("Test Passed\n")
    
def test_citizen_find_possible_targets():
    logging.info("Running test: citizen_find_possible_targets")
    citizen = Citizen({"alias": "test_citizen", "number": "1"})
    citizen_2 = Citizen({"alias": "test_citizen_2", "number": "2"})
    mafioso = Mafioso({"alias": "test_mafioso", "number": "3"})
    
    citizen.find_possible_targets([citizen, citizen_2, mafioso])
    
    # Should only have 1 list of possible targets
    assert len(citizen.possible_targets) == 1, f"{citizen} should only have 1 list of possible targets"
    
    # Inside the list of possible targets should be 1 actor
    assert len(citizen.possible_targets[0]) == 1, f"{citizen} should only have 1 possible target in list 1"
    
    # The actor in the list should be 'citizen'
    assert citizen in citizen.possible_targets[0], f"{citizen} not in own possible targets list"
    logging.info("Test Passed\n")
    
def test_citizen_night_action():
    logging.info("Running test: citizen_night_action")

    citizen = Citizen({"alias": "test_citizen", "number": "1"})
    mafioso = Mafioso({"alias": "test_mafioso", "number": "3"})
    
    citizen.action([citizen]) # Use vest on self
    
    assert citizen.night_immune == True, f"{citizen} should be night immune"
    assert citizen.remaining_vests == citizen.max_vests - 1, f"{citizen} should have {citizen.max_vests - 1} vest/s remaining, but instead has {citizen.remaining_vests}"
    
    logging.info("Test Passed\n")
