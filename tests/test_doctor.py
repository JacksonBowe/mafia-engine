from engine import roles

def test_bodyguard_create():
    doctor = roles.Doctor({'alias': 'test_doctor', 'number': 1, 'id': '1'})
    
def test_doctor_find_targets():
    citizen = roles.Citizen({'alias': 'test_citizen', 'number': 1, 'id': '1'})
    mafioso = roles.Mafioso({'alias': 'test_mafioso', 'number': 2, 'id': '2'})
    doctor = roles.Doctor({'alias': 'test_doctor', 'number': 3, 'id': '3'})
    
    doctor.find_possible_targets([citizen, mafioso, doctor])
    
    assert doctor.possible_targets == [[citizen, mafioso]]

def test_doctor_action():
    citizen = roles.Citizen({'alias': 'test_citizen', 'number': 1, 'id': '1'})
    doctor = roles.Doctor({'alias': 'test_doctor', 'number': 3, 'id': '3'})
    
    doctor.set_targets([citizen])
    doctor.do_action()
    
    assert doctor in citizen.visitors
    assert doctor.visiting == citizen
    assert doctor in citizen.doctors
    
    assert citizen.alive
    
def test_doctor_revive():
    citizen = roles.Citizen({'alias': 'test_citizen', 'number': 1, 'id': '1'})
    mafioso = roles.Mafioso({'alias': 'test_mafioso', 'number': 2, 'id': '2'})
    doctor = roles.Doctor({'alias': 'test_doctor', 'number': 3, 'id': '3'})
    
    mafioso.set_targets([citizen])
    mafioso.do_action()
    
    doctor.revive_target(citizen)
    
    assert citizen.alive
    
    # TODO: Ensure that this creates the correct events