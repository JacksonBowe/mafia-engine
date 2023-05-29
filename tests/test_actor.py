
import logging
import pytest
from typing import List, Tuple

import engine as Mafia
from engine import roles

@pytest.fixture(scope="session")
def test_actors_boostrap() -> Tuple[roles.Citizen, List[roles.Actor]]:
    citizen_1 = roles.Citizen({'alias': 'test_citizen_1', 'number': 1, 'id': '1'})
    citizen_2 = roles.Citizen({'alias': 'test_citizen_2', 'number': 2, 'id': '2'})
    mafioso_1 = roles.Mafioso({'alias': 'test_mafioso_1', 'number': 3, 'id': '3'})
    
    return citizen_1, [citizen_2, mafioso_1]

def test_actor_night_immune():
    citizen = roles.Citizen({'alias': 'test_citizen', 'number': 1, 'id': '1'})
    mafioso = roles.Mafioso({'alias': 'test_mafioso', 'number': 2, 'id': '2'})
    
    citizen.night_immune = True
    
    mafioso.set_targets([citizen])
    mafioso.do_action()
    
    assert citizen.alive
    
def test_actor_bodyguard():
    citizen = roles.Citizen({'alias': 'test_citizen', 'number': 1, 'id': '1'})
    mafioso = roles.Mafioso({'alias': 'test_mafioso', 'number': 2, 'id': '2'})
    bodyguard = roles.Bodyguard({'alias': 'test_bopdyguard', 'number': 3, 'id': '3'})
    
    bodyguard
    
    mafioso.set_targets([citizen])
    mafioso.do_action()
    
    assert not citizen.alive
    
def test_actor_die():
    citizen = roles.Citizen({'alias': 'test_citizen', 'number': 1, 'id': '1'})
    mafioso = roles.Mafioso({'alias': 'test_mafioso', 'number': 2, 'id': '2'})
    
    mafioso.set_targets([citizen])
    mafioso.do_action()
    
    assert not citizen.alive
    

