""" Brighten a light, then return to previous brightness state """ 
# from:
# https://community.home-assistant.io/t/brighten-a-light-then-return-to-previous-brightness-state/20802

# Get Params
entity_id  = data.get('entity_id')
action 	   = data.get('action')
level 	   = int(data.get('level'))

# Get current brightness value
states     = hass.states.get(entity_id)
brightness = states.attributes.get('brightness') or 0

# Set new brightness value
if action == 'dim_up'   : dim = (brightness + level)
if action == 'dim_down' : dim = (brightness - level)
if dim <= 0 			: dim = 0
if dim >= 254			: dim = 254

# Call service
if dim == 0 :
	logger.info('Tuning off ' + str(entity_id))
	data = { "entity_id" : entity_id }
	hass.services.call('light', 'turn_off', data)
else :
	logger.info('Dimming' + str(entity_id) + 'from : ' + str(brightness) + ' to ' + str(dim))
	data = { "entity_id" : entity_id, "brightness" : dim }
	hass.services.call('light', 'turn_on', data)

