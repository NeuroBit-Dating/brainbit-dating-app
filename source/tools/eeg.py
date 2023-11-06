from neurosdk.scanner import Scanner
from neurosdk.sensor import Sensor
from neurosdk.brainbit_sensor import BrainBitSensor
from neurosdk.cmn_types import *
from flask import g
from tools.logging import logger  
import random, json
#doing all this a the "module level" in "Demo" server mode it will work fine :)
from db_con import get_db_instance, get_db

eeg_db = get_db()
eeg_cur = eeg_db.cursor()

# Simulated EEG data generation 
def simulate_brain_bit_signal_data():
    return BrainBitSignalData(
        PackNum=random.randint(0, 100),
        Marker=random.randint(0, 1),
        O1=random.uniform(0, 0.5),
        O2=random.uniform(0, 0.5),
        T3=random.uniform(0, 0.5),
        T4=random.uniform(0, 0.5)
    )

# Modified 'on_brain_bit_signal_data_received' function to generate simulated EEG data
def on_brain_bit_signal_data_received(sensor, data):
    simulated_data = simulate_brain_bit_signal_data()
    # Convert to dictionary 
    data_dict = {
        'PackNum': simulated_data.PackNum,
        'Marker': simulated_data.Marker,
        'O1': simulated_data.O1,
        'O2': simulated_data.O2,
        'T3': simulated_data.T3,
        'T4': simulated_data.T4,
    }
    
    # Convert dictionary to JSON
    data_json = json.dumps(data_dict)
    eeg_cur.execute("INSERT INTO brain (movieID, data) VALUES (?, ?)", (0, data_json))
    eeg_db.commit()
    logger.debug(simulated_data)
     

def on_sensor_state_changed(sensor, state):
   logger.debug('Sensor {0} is {1}'.format(sensor.Name, state))


'''
logger.debug("Create Headband Scanner")
gl_scanner = Scanner([SensorFamily.SensorLEBrainBit])
gl_sensor = None
logger.debug("Sensor Found Callback")
def sensorFound(scanner, sensors):
    global gl_scanner
    global gl_sensor
    for i in range(len(sensors)):
        logger.debug('Sensor %s' % sensors[i])
        logger.debug('Connecting to sensor')
        gl_sensor = gl_scanner.create_sensor(sensors[i])
        gl_sensor.sensorStateChanged = on_sensor_state_changed
        gl_sensor.connect()
        gl_sensor.signalDataReceived = on_brain_bit_signal_data_received
        gl_scanner.stop()
        del gl_scanner

gl_scanner.sensorsChanged = sensorFound

logger.debug("Start scan")
#gl_scanner.start()


def get_head_band_sensor_object():
    return gl_sensor
'''

