import json
import logging
from events import EVENTS, GameEventGroup
from roles import Citizen
from roles import Mafioso



def test_mafioso_find_allies():
    logging.info("Running test: mafioso_find_allies")
    mafioso = Mafioso({'alias': 'test_mafioso', 'number': '1'})
    citizen = Citizen({'alias': 'test_citizen', 'number': '2'})
    mafioso_2 = Mafioso({'alias': 'test_mafioso_2', 'number': '3'})
    
    mafioso.find_allies([mafioso, citizen, mafioso_2])
    
    # Check number of allies
    assert len(mafioso.allies) == 2, f"{mafioso} should have 2 allies, [{mafioso}, {mafioso_2}]"
    
    # Check that self and mafioso_2 are in the allies list
    assert mafioso in mafioso.allies, f"{mafioso} should be his own ally, but not in the allies list"
    assert mafioso_2 in mafioso.allies, f"{mafioso_2} should be an ally of {mafioso}, but not in the allies list"

    logging.info("Test Passed\n")
    
def test_mafioso_find_possible_targets():
    logging.info("Running test: mafioso_find_possible_targets")
    mafioso = Mafioso({'alias': 'test_mafioso', 'number': '1'})
    citizen = Citizen({'alias': 'test_citizen', 'number': '2'})
    mafioso_2 = Mafioso({'alias': 'test_mafioso_2', 'number': '3'})
    citizen_2 = Citizen({'alias': 'test_citizen_2', 'number': '4'})
    
    mafioso.find_possible_targets([mafioso, citizen, mafioso_2, citizen_2])
    
    
    # Should only have 1 list of possible targets
    assert len(mafioso.possible_targets) == 1, f"{mafioso} should only have 1 list of possible targets"
    
    # Inside the list of possible targets should be 2 actors
    assert len(mafioso.possible_targets[0]) == 2, f"{mafioso} should only have 2 possible targets in list 1"
    
    # The actors in the list should be 'citizen' and 'citizen_2'
    assert citizen in mafioso.possible_targets[0], f"{citizen} not in {mafioso} possible targets list"
    assert citizen_2 in mafioso.possible_targets[0], f"{citizen_2} not in {mafioso} possible targets list"
    
    logging.info("Test Passed\n")

def test_mafioso_action_basic():
    logging.info("Running test: mafioso_action_basic")
    # EVENTS = GameEventGroup()
    
    mafioso = Mafioso({'alias': 'test_mafioso', 'number': '1', "id": "1111"})
    citizen = Citizen({'alias': 'test_citizen', 'number': '2', "id": "2222"})
    
    mafioso.action(targets=[citizen])
    
    # Check that the target has died
    assert citizen.alive == False, f"{mafioso} attempted to kill {citizen}, but target not dead"
    
    # Check that Mafioso is at targets house
    assert mafioso in citizen.house, f"Mafioso action should place them at the targets house, but this hasn't happened"
    
    logging.info("Test Passed\n") 
    
def test_mafioso_action_night_immune():
    logging.info("Running test: mafioso_action_night_immune")
    
    mafioso = Mafioso({'alias': 'test_mafioso', 'number': '1', "id": "1111"})
    citizen = Citizen({'alias': 'test_citizen', 'number': '2', "id": "2222"})
    
    # Citizen use vest
    citizen.action(targets=[citizen])
    
    # Mafioso attempt kill on citizen
    mafioso.action(targets=[citizen])
    
    assert citizen.alive == True
    logging.info("Test Passed\n")
