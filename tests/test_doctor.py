import logging
from roles.citizen import Citizen
from roles.doctor import Doctor
from roles.mafioso import Mafioso

def test_citizen_find_allies():
    logging.info("Running test: doctor_find_allies")
    citizen = Citizen({"alias": "test_citizen", "number": "1"})
    doctor = Doctor({"alias": "test_doctor", "number": "2"})
    mafioso = Mafioso({"alias": "test_mafioso", "number": "3"})
    
    doctor.find_allies([citizen, doctor, mafioso])
    
    # Check number of allies
    assert len(doctor.allies) == 0, f"{doctor} should have 0 allies"

    logging.info("Test Passed\n")
    
def test_doctor_find_possible_targets():
    logging.info("Running test: doctor_find_possible_targets")
    citizen = Citizen({"alias": "test_citizen", "number": "1"})
    doctor = Doctor({"alias": "test_doctor", "number": "2"})
    mafioso = Mafioso({"alias": "test_mafioso", "number": "3"})
    
    doctor.find_possible_targets([citizen, doctor, mafioso])
    
    # Should only have 1 list of possible targets
    assert len(doctor.possible_targets) == 1, f"{doctor} should only have 1 list of possible targets"
    
    # Inside the list of possible targets should be 2 actors
    assert len(doctor.possible_targets[0]) == 2, f"{doctor} should only have 2 possible targets in list 1"
  
    # Both 'citizen' and 'mafioso' should be in the list of possible targets
    assert citizen in doctor.possible_targets[0], f"{citizen} should be in possible_targets list of {doctor}"
    assert mafioso in doctor.possible_targets[0], f"{mafioso} should be in possible_targets list of {doctor}"
    
    # The 'doctor' should NOT be in it's own list of possible targets
    assert doctor not in doctor.possible_targets[0], f"{doctor} inside own list of possible targets, means they can heal themselves. Bad"
    logging.info("Test Passed\n")

def test_doctor_heal_victim():
    logging.info("Running test: doctor_heal_victim")
    citizen = Citizen({"alias": "test_citizen", "number": "1"})
    doctor = Doctor({"alias": "test_doctor", "number": "2"})
    mafioso = Mafioso({"alias": "test_mafioso", "number": "3"})

    doctor.action([citizen])
    mafioso.action([citizen])
    # TODO
    
    assert citizen.alive == True, f"{citizen} should have been healed by doctor"

    
    logging.info("Test Passed\n")

    
    