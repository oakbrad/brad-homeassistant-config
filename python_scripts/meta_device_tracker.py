#
# meta_device_tracker.py
#
# https://github.com/oakbrad/brad-homeassistant-config/blob/master/python_scripts/meta_device_tracker.py
#
# Combine multiple device trackers into one entity
#
# Logic:  Only GPS is reliable for 'not_home'
#         Block others from marking 'not_home' but keep for 'home'
# 
#
   
# Get Data from Automation Trigger
triggeredEntity = data.get('entity_id')
metatrackerName = "device_tracker." + data.get('meta_entity')

# Get current & new state
newState = hass.states.get(triggeredEntity)
currentState = hass.states.get(metatrackerName)
# Get New data
newSource = newState.attributes.get('source_type')

# If GPS source, set new coordinates
if newSource == 'gps':
  newLatitude = newState.attributes.get('latitude')
  newLongitude = newState.attributes.get('longitude')
  newgpsAccuracy = newState.attributes.get('gps_accuracy')
# If not, keep last known coordinates
else:
  if newSource is not None:
    newLatitude = currentState.attributes.get('latitude')
    newLongitude = currentState.attributes.get('longitude')
    newgpsAccuracy = currentState.attributes.get('gps_accuracy')

# Get Battery
if newState.attributes.get('battery') is not None:
  newBattery = newState.attributes.get('battery')
elif currentState.attributes.get('battery') is not None:
  newBattery = currentState.attributes.get('battery')
else:
  newBattery = None

# Set new state and icon
# Everything updates 'home'
if newState.state == 'home':
  newStatus = 'home'
  newIcon = 'mdi:home-map-marker'
# only GPS platforms update 'not_home'
elif newState.state == 'not_home' and newSource == 'gps':
    newStatus = 'not_home'
    newIcon = 'mdi:home'
# Otherwise keep old status
else: 
    newStatus = currentState.state

# Create device_tracker.meta entity
hass.states.set(metatrackerName, newStatus, {
    'icon': newIcon,
    'name': metatrackerName,
    'source_type': newSource,
    'battery': newBattery,
    'gps_accuracy': newgpsAccuracy,
    'latitude': newLatitude,
    'longitude': newLongitude,
    'last_update_source': newState.name 
})

