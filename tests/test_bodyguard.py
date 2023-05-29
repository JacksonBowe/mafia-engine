
from engine import roles

def test_bodyguard_create():
    bodyguard = roles.Bodyguard({'alias': 'test_bodyguard_1', 'number': 1, 'id': '1'})
    
def test_bodyguard_find_targets():
    citizen = roles.Citizen({'alias': 'test_citizen', 'number': 1, 'id': '1'})
    mafioso = roles.Mafioso({'alias': 'test_mafioso', 'number': 2, 'id': '2'})
    bodyguard = roles.Bodyguard({'alias': 'test_bodyguard', 'number': 3, 'id': '3'})
    
    bodyguard.find_possible_targets([citizen, mafioso, bodyguard])
    
    assert bodyguard.possible_targets == [[citizen, mafioso]]

def test_bodyguard_action():
    citizen = roles.Citizen({'alias': 'test_citizen', 'number': 1, 'id': '1'})
    mafioso = roles.Mafioso({'alias': 'test_mafioso', 'number': 2, 'id': '2'})
    bodyguard = roles.Bodyguard({'alias': 'test_bodyguard', 'number': 3, 'id': '3'})
    
    bodyguard.set_targets([citizen])
    bodyguard.do_action()
    
    assert bodyguard in citizen.bodyguards
    assert bodyguard.visiting == citizen
    assert bodyguard in citizen.bodyguards
    
    mafioso.set_targets([citizen])
    mafioso.do_action()
    
    assert citizen.alive
    assert not mafioso.alive
    assert not bodyguard.alive
    
def test_bodyguard_shootout():
    citizen = roles.Citizen({'alias': 'test_citizen', 'number': 1, 'id': '1'})
    mafioso = roles.Mafioso({'alias': 'test_mafioso', 'number': 2, 'id': '2'})
    bodyguard = roles.Bodyguard({'alias': 'test_bodyguard', 'number': 3, 'id': '3'})
    
    bodyguard.set_targets([citizen])
    bodyguard.do_action()
    
    mafioso.set_targets([citizen])
    mafioso.do_action()
    
    assert citizen.alive
    assert not mafioso.alive
    assert not bodyguard.alive