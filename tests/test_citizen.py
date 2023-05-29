
import logging
import pytest
from typing import List, Tuple

import engine as Mafia
from engine import roles

def test_citizen_create() -> roles.Citizen:
    logging.info("Running test: new Citizen")
    citizen = roles.Citizen({'alias': 'test_citizen_1', 'number': '1'})
    
    return citizen

@pytest.fixture(scope="session")
def test_citizen_boostrap() -> Tuple[roles.Citizen, List[roles.Actor]]:
    citizen_1 = roles.Citizen({'alias': 'test_citizen_1', 'number': 1, 'id': '1'})
    citizen_2 = roles.Citizen({'alias': 'test_citizen_2', 'number': 2, 'id': '2'})
    mafioso_1 = roles.Mafioso({'alias': 'test_mafioso_1', 'number': 3, 'id': '3'})
    
    return citizen_1, [citizen_2, mafioso_1]

def test_citizen_find_targets(test_citizen_boostrap: Tuple[roles.Citizen, List[roles.Actor]]):
    citizen, others = test_citizen_boostrap
    
    citizen.find_possible_targets(others)
    logging.debug(citizen.possible_targets)
    assert len(citizen.possible_targets) == 1
    assert len(citizen.possible_targets[0]) == 1
    assert citizen.possible_targets[0][0] == citizen

def test_citizen_find_allies(test_citizen_boostrap: Tuple[roles.Citizen, List[roles.Actor]]):
    citizen, others = test_citizen_boostrap
    
    citizen.find_allies(others)
    assert len(citizen.allies) == 0

def test_citizen_action():
    citizen = roles.Citizen({'alias': 'test_citizen', 'number': 1, 'id': '1'})
    mafioso = roles.Mafioso({'alias': 'test_mafioso', 'number': 2, 'id': '2'})
    
    vests_before = citizen.remaining_vests
    citizen.do_action()
    
    assert citizen.night_immune
    assert citizen.remaining_vests == vests_before - 1
    
    

