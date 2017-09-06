# Temperature sensors
#
# Consolidate all of these, if available...
#
#      - sensor.entry_temperature - closet
#      - sensor.kitchen_pothos_temperature - kitchen
#      - sensor.kitchen_temperature
#      - sensor.giant_pothos_temperature - office
#      - sensor.hanging_red_pothos_temperature - dining
#      - sensor.window_air_temp - window
#      - sensor.giant_philodrendon_temperature - living
#      - sensor.hanging_spider_plant_temperature - living
#      - sensor.palm_temperature - living
#      - sensor.projector_pothos_temperature - living
#      - sensor.rubber_plant_temperature - living
#      - sensor.small_philodendron_temperature - office
#      - sensor.window_spider_plant_temperature - living

tempEntities = ["sensor.entry_temperature","sensor.kitchen_pothos_temperature", "sensor.kitchen_temperature", "sensor.giant_pothos_temperature","sensor.hanging_red_pothos_temperature","sensor.window_air_temp","sensor.giant_philodendron_temperature","sensor.hanging_spider_plant_temperature","sensor.palm_temperature","sensor.projector_pothos_temperature","sensor.rubber_plant_temperature","sensor.small_philodendron_temperature","sensor.window_spider_plant_temperature"]
sensorsTotal = len(tempEntities)
tempsCounted = 0
tempsTotal = 0

# look up each entity_id
for entity_id in tempEntities:
  # copy it's state
  state = hass.states.get(entity_id)

  # If not None, add up and increase counter
  if state.state is not None:
     if state.state is not 'unknown':
       tempsCounted = tempsCounted + 1
       tempsTotal = tempsTotal + int(float(state.state))

# Get average
averageTemp = "{0:.2f}".format(tempsTotal / tempsCounted)

hass.states.set('sensor.average_indoor_temp', averageTemp, {
    'unit_of_measurement': '°F',
    'friendly_name': 'Indoor Temp',
    'icon': 'mdi:thermometer',
    'temps_counted': tempsCounted,
    'temps_total': sensorsTotal
})  
 
