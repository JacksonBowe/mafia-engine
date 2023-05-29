from engine import roles
from engine import events
from engine.events import ACTION_EVENTS

def test_godfather_create():
    godfather = roles.Godfather({'alias': 'test_godfather', 'number': 1, 'id': '1'})
    
def test_godfather_find_allies():
    citizen = roles.Citizen({'alias': 'test_citizen', 'number': 1, 'id': '1'})
    mafioso = roles.Mafioso({'alias': 'test_mafioso', 'number': 2, 'id': '2'})
    godfather = roles.Godfather({'alias': 'test_godfather', 'number': 3, 'id': '3'})
    
    godfather.find_allies([citizen, mafioso, godfather])
    
    assert godfather.allies == [mafioso, godfather]
    
def test_godfather_find_targets():
    citizen = roles.Citizen({'alias': 'test_citizen', 'number': 1, 'id': '1'})
    mafioso = roles.Mafioso({'alias': 'test_mafioso', 'number': 2, 'id': '2'})
    godfather = roles.Godfather({'alias': 'test_godfather', 'number': 3, 'id': '3'})
    
    godfather.find_possible_targets([citizen, mafioso, godfather])
    
    assert godfather.possible_targets == [[citizen]]

def test_godfather_action_proxy():
    citizen = roles.Citizen({'alias': 'test_citizen', 'number': 1, 'id': '1'})
    mafioso = roles.Mafioso({'alias': 'test_mafioso', 'number': 2, 'id': '2'})
    godfather = roles.Godfather({'alias': 'test_godfather', 'number': 3, 'id': '3'})
    
    godfather.find_allies([citizen, mafioso, godfather])
    
    godfather.set_targets([citizen])
    godfather.do_action()
    
    assert godfather.visiting == None
    assert godfather not in mafioso.visitors
    assert godfather not in citizen.visitors
    
    mafioso.do_action()
    
    assert mafioso.visiting == citizen
    
    assert not citizen.alive
    
def test_godfather_action_success():
    citizen = roles.Citizen({'alias': 'test_citizen', 'number': 1, 'id': '1'})
    godfather = roles.Godfather({'alias': 'test_godfather', 'number': 3, 'id': '3'})
    
    godfather.set_targets([citizen])
    godfather.do_action()
    
    assert godfather.visiting == citizen
    assert godfather in citizen.visitors
    
    assert not citizen.alive
    
def test_godfather_action_fail():
    citizen = roles.Citizen({'alias': 'test_citizen', 'number': 1, 'id': '1'})
    godfather = roles.Godfather({'alias': 'test_godfather', 'number': 3, 'id': '3'})
    
    citizen.night_immune = True
    
    godfather.set_targets([citizen])
    godfather.do_action()
    
    assert godfather.visiting == citizen
    assert godfather in citizen.visitors
    
    assert citizen.alive