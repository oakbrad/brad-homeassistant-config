problemPlants = 0
allproblemPlants = []
waterPlants = []
numberWater = 0
fertilizePlants = []
numberFertilize = 0
deadBatteries = []
numberdeadBatteries = 0
whichIcon = "mdi:help-circle-outline"

for entity_id in hass.states.entity_ids('plant'):
    state = hass.states.get(entity_id)
    if state.state == 'problem':
        problemPlants = problemPlants + 1
        allproblemPlants.append(state.name)
        problem = state.attributes.get('problem') or 'none'
        if "conductivity low" in problem:
          fertilizePlants.append(state.name)
          numberFertilize = numberFertilize + 1
        if "moisture low" in problem:
          waterPlants.append(state.name)
          numberWater = numberWater + 1
        if "battery low" in problem:
          deadBatteries.append(state.name)
          numberdeadBatteries = numberdeadBatteries + 1

# Set icon
if problemPlants > 0:
  whichIcon = "mdi:alert-circle-outline"
else:
  whichIcon = "mdi:check-circle-outline"

# Set states
hass.states.set('sensor.plant_problems', problemPlants, {
    'unit_of_measurement': 'plants',
    'friendly_name': 'Problem Plants',
    'icon': whichIcon,
    'problem_plants': allproblemPlants,
    'water': waterPlants,
    'water_number': numberWater,
    'fertilize': fertilizePlants,
    'fertilize_number': numberFertilize,
    'battery_change': deadBatteries,
    'battery_number': numberdeadBatteries
})

hass.states.set('sensor.water_plants_number', numberWater, {
    'unit_of_measurement': 'plants',
    'friendly_name': 'Water Plants Number',
    'icon': 'mdi:water'
})

waterplantsList = ', '.join(waterPlants)
if waterplantsList == "":
  waterplantsList = "None"
hass.states.set('sensor.water_plants_friendly', waterplantsList, {
    'friendly_name': 'Water Plants',
    'icon': 'mdi:water'
})

hass.states.set('sensor.fertilize_plants_number', numberFertilize, {
    'unit_of_measurement': 'plants',
    'friendly_name': 'Fertilize Plants Number',
    'icon': 'mdi:emoticon-poop'
})

fertilizeplantsList = ', '.join(fertilizePlants)
if waterplantsList == "":
  waterplantsList = "None"
hass.states.set('sensor.fertilize_plants_friendly', fertilizeplantsList, {
    'unit_of_measurement': 'plants',
    'friendly_name': 'Fertilize Plants',
    'icon': 'mdi:emoticon-poop'
})
