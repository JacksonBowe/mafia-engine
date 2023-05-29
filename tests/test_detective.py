from engine import roles
from engine import events
from engine.events import ACTION_EVENTS

def test_detective_create():
    detective = roles.Detective({'alias': 'test_detective', 'number': 1, 'id': '1'})
    
def test_detective_find_targets():
    citizen = roles.Citizen({'alias': 'test_citizen', 'number': 1, 'id': '1'})
    mafioso = roles.Mafioso({'alias': 'test_mafioso', 'number': 2, 'id': '2'})
    detective = roles.Detective({'alias': 'test_detective', 'number': 3, 'id': '3'})
    
    detective.find_possible_targets([citizen, mafioso, detective])
    
    assert detective.possible_targets == [[citizen, mafioso]]

def test_detective_action():
    citizen = roles.Citizen({'alias': 'test_citizen', 'number': 1, 'id': '1'})
    mafioso = roles.Mafioso({'alias': 'test_mafioso', 'number': 2, 'id': '2'})
    detective = roles.Detective({'alias': 'test_detective', 'number': 3, 'id': '3'})
    
    detective.set_targets([mafioso])
    detective.do_action()
    
    assert detective.visiting == mafioso
    assert detective in mafioso.visitors
    
    mafioso.set_targets([citizen])
    mafioso.do_action()
    
def test_detective_investigate():
    citizen = roles.Citizen({'alias': 'test_citizen', 'number': 1, 'id': '1'})
    mafioso = roles.Mafioso({'alias': 'test_mafioso', 'number': 2, 'id': '2'})
    detective = roles.Detective({'alias': 'test_detective', 'number': 3, 'id': '3'})
    
    detective.set_targets([mafioso])
    detective.do_action()
    
    assert detective.visiting == mafioso
    assert detective in mafioso.visitors
    
    mafioso.set_targets([citizen])
    mafioso.do_action()
    
    ACTION_EVENTS.reset(new_id="post-resolve")
    detective.investigate()
    
    assert ACTION_EVENTS.get_by_id(events.Common.VISITED_BY) is not None