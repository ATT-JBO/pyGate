# this plugin module provides access to the pins of a beaglebone
# the config file 'beaglePins.config' defines which pins should be used and how.

import config
import device
import Adafruit_BBIO.GPIO as GPIO

_device = None                                          # we are a single device, not a full gateway, so use this wrapper to manage
_pinLayouts = None

def connectToGateway(moduleName):
    '''optional
        called when the system connects to the cloud.'''
    global _cloud, _pinLayouts
    _device = device(moduleName, 'beagle')
    configs = config.load('beaglePins', True)
    _pinLayouts = configs['pinLayouts']
    setupGPIO()

def syncDevices(existing):
    '''optional
       allows a module to synchronize it's device list. 
       existing: the list of devices that are already known in the cloud for this module.'''
    if not existing:
        _device.createDevice('beagle pins', 'all the pins on the beagle bone')
        _cloud.addAsset('1', 'garage', 'garagae lights', True, 'boolean')
         
def run():
    ''' required
        main function of the plugin module'''


def onActuate(actuator, value):
    """called when an actuator command was received (either internally from the plugin system or from the cloud)"""
    if actuator == '1':
        if value == "true":
            GPIO.output("P9_22", GPIO.HIGH)
            _device.send("true", actuatorPin)                #provide feedback to the cloud that the operation was succesful
        elif value == "false":
            GPIO.output("P9_22", GPIO.LOW)
            _device.send("false", actuatorPin)               #provide feedback to the cloud that the operation was succesful
        else:
            print("unknown value: " + value)


def setupGPIO():
    GPIO.setup("P9_22", GPIO.OUT)