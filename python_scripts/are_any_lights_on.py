#
# Are all lights off?
# If lights are on, how many?
# Should work regardless of light/switch domain
# 
# Return input_boolean.are_any_lights_on
# Attributes: number of lights & switches on and the total
#

lightStatus = 'off'
switchEntities = ["switch.aquarium","switch.edison_pendants","switch.office","switch.sink","switch.string_lights","switch.work_lamp","switch.bathroom_light"]
lightsOn = 0
switchesOn = 0
totalOn = 0
whichIcon = "mdi:lightbulb-outline"

# Don't count nightlights if they're currently on
# This allows other motion activated night lights to trigger with are_any_lights_on as condition
kitchenNightlight = ["light.stove","light.fridge"]
kitchenNightlightOn = hass.states.get('input_boolean.nightlight_kitchen')
bedroomNightlight = ["light.entry"]
bedroomNightlightOn = hass.states.get('input_boolean.nightlight_bedroom')
livingroomNightlight = ["light.floor_lamp"]
livingroomNightlightOn = hass.states.get('input_boolea.nightlight_livingroom')

# Get the light entities
lights = hass.states.entity_ids('light')

# Kitchen filtering if night light is on
if kitchenNightlightOn == 'on': lights = [x for x in lights.name if x not in kitchenNightlight]
if bedroomNightlightOn == 'on': lights = [y for y in lights.name if y not in bedroomNightlight]
if livingroomNightlightOn == 'on': lights = [z for z in lights.name if z not in livingroomNightlight]

for entity_id in lights:
  state = hass.states.get(entity_id)
  # filter out bulbs not on
  if (state.state == 'on'):
    if ('tradfri' not in state.name):
      lightStatus = 'on'
      lightsOn = lightsOn + 1

for entity_id in switchEntities:
  state = hass.states.get(entity_id)
  if state.state == 'on':
    lightStatus = 'on'
    switchesOn = switchesOn + 1

if lightStatus == 'on':
  whichIcon = "mdi:lightbulb-on-outline"

totalOn = switchesOn + lightsOn

# Return sensor state
hass.states.set('input_boolean.are_any_lights_on', lightStatus, { 
    'friendly_name': 'Are Any Lights On?',
    'icon': whichIcon,
    'lights_on': lightsOn,
    'switches_on': switchesOn,
    'total_on': totalOn,
    'extra_data_template':'{total_on} lights on'
})
