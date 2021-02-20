from pi_mqtt_gpio.modules import GenericSensor
import logging

REQUIREMENTS = ("spidev","mfrc522")

CONFIG_SCHEMA = {
    "rc522": {"type": "integer", "required": True, "empty": False},
}

_LOG = logging.getLogger("mqtt_gpio")


class Sensor(GenericSensor):
    """
    Implementation of RC255 NFC/RFID sensor.
    """

    def __init__(self, config):
        from mrfc522 import SimpleMFRC522
        self.reader = SimpleMFRC522()
    
    def setup_sensor(self, config):
        return True  # nothing to do here
    
    def get_value(self, config):
        id, text = self.reader.read()
        _LOG.warning("MFRC522: Reading from Tag: "+id+" " +text)
        return id
    
    def cleanup(self):
        # nothing to do here