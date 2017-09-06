# Home Assistant Configuration
[Home Assistant](http://homeassistant.io) configuration files.

Some detailed information about setting various parts of this up on [DIY Futurism](http://www.diyfuturism.com).

* [Hardware](#hardware)
* [Presence Detection](#presence)
* [Automations](#automations)
* [House Modes](#house-modes)
* [Other Projects Used](#other-projects-used)

My HA is an Hassbian install on a Raspberry Pi 3 with an [GoControl Z-Wave/Zigbee USB stick](http://amzn.to/2u8XVGm).

Running HA version: 0.50.1

![Floorplan](https://github.com/oakbrad/brad-homeassistant-config/blob/master/screenshots/floorplan.png)

![Screenshot](https://github.com/oakbrad/brad-homeassistant-config/blob/master/screenshots/ha-1-homepage.png)

# Hardware
* Lights
  * LimitlessLED - [Milight RGB Bulbs](http://amzn.to/2slpT2W) using [MiLight WiFi Bridge](http://amzn.to/2roEQ59) x2
  * Ikea Tradfri - several bulbs via gateway
  * ESP8266 bulb with [AiLight firmware](https://github.com/stelgenhof/AiLight) - TESTING
* Wall Switches
  * [GE Z-Wave 12727 Wall Toggle Switch](http://amzn.to/2rnVCBs) x1
  * [GE Z-Wave 12729 Wall Toggle Dimmer Switch](http://amzn.to/2spiWil) x2
  * Enerwave Z-Wave ZWN-RSM2 Dual In-Wall Relay x1
* Smart Devices
  * [WEMO Mr. Coffee](http://amzn.to/2sysDuG)
  * [Withings Body Scale](http://amzn.to/2spNwIQ)
  * Fitbit
* Switches
  * [TP-Link HS100 Smart Switch](http://amzn.to/2sq1bQb)
  * [Sonoff Switches](https://www.itead.cc/sonoff-wifi-wireless-switch.html) running [Sonoff-HomeAssistant](https://github.com/KmanOz/Sonoff-HomeAssistant) firmware
* Media Players
  * [Volumio](https://volumio.org/) Raspberry Pi streaming player for stereo
  * Plex (Roku)
  * MPD - plays radio through speaker on HA Raspberry Pi
  * VLC - for Amazon Polly TTS output
* Sensors
  * [Wemos D1 Mini](http://amzn.to/2sydVU8) (esp8266) nodes with sensors for motion, temps, etc. via MQTT
  * Mi Flora plant sensors x9
  * [Z-Wave Motion Sensor](http://amzn.to/2symNta) (battery powered)
* Other Hardware
  * [Echo Dot](http://amzn.to/2ubdoVC) Voice control
  * [Bluetooth iBeacons](http://amzn.to/2slTOIF)
  * old iPhones with IPCam app
  * Synology DS413j - NAS
  * [Amazon Dash Buttons](http://amzn.to/2uXPJZe)
# Presence
Tracking with:
* Owntracks - 'significant changes' mode, iBeacon
* HomeAssistant iOS app - enable location tracking, enable iBeacon
* ping - Is my phone pingable on my network?
* Bluetooth

I use a python script to filter 'home' and 'not_home' signals by platform.
* All platforms update 'home'
* Only GPS platforms (Owntracks, iOS app) update 'not_home'
  * Delayed by 10 minutes to avoid turning everything off on quick dog walks / bodega runs
* Retain the most recent GPS coordinates and battery state regardless of platform

This script creates a new device_tracker with the most recent information and state, using the most platforms in the most reliable way.

Position in house is located using variable.last_motion

![Screenshot](https://github.com/oakbrad/brad-homeassistant-config/blob/master/screenshots/device-tracker.png)
![Screenshot](https://github.com/oakbrad/brad-homeassistant-config/blob/master/screenshots/last-motion.png)

# Automations
* Alarm
  * Alarm Away - when no one is home
  * Alarm Home - when coming home
  * TTS Announce Disarm, Pending, and Armed Status
  * Audible Alert when Front Door opens and Armed Home
  * Trigger Alarm - Notify with security camera photo if Door Opened, "Presence Detected" announcement
* Alarm Clock
  * Make Morning Coffee when Alarm goes off
  * Alarm Clock - turn on lights and radio to wake me up
  * TTS Annouce Weather & other Info
  * UI - change default view to show commute times, weather info during morning
* Aquarium
  * Turn on 30 mins before sunrise and 1 hour after
  * Turn on 1 hour before sunset, turn off 4 hours after or at 10PM (whichever is first)
* Climate
  * Indoor Temperature & Humidity is a mean of all available sensors (using min_max component)
* IFTT Integration
  * When plants need to be watered, add them to my Todoist todo list
  * If Fitbit logs new sleep but no alarm is set, wake house up
  * Withings weigh in before bed 9pm - 12am, start goodnight sequence
* Lights
  * Flux - adjust color temp based on time (currently Tradfri lights only)
  * Sunset - 40m before sunset, turn on evening lights
  * Day - during day turn on day dim lights and throttle Transmission
  * Evening - turn on dim lights if I come home after 10pm
  * After Midnight - turn on red lights if I come home 12a-430a
  * Turn everything off when no one's home
  * Turn Closet lights on/off by motion detector
  * Turn Bathroom lights on/off by motion detector (off 12a-8:30a)
  * Turn Office Lights on/off by motion detector
  * Turn Crawl space light on/off by door sensor
  * Turn kitchen lamps on/off using wall switch
  * Turn on office lamps using switch
  * Night Light - Kitchen on motion
* Media
  * Dim house lights when Plex starts playing
  * Turn on bathroom lights & lamp when movie pausd
  * Fade house lights up when Plex stops
  * Turns off bandwidth throttling for Transmission/sabnzbd when I'm away from home
* Python Scripts
  * are_any_lights_on.py - input_boolean for lights on/off, counts lights and switches on
    * Does not count nightlights
  * meta_device_tracker.py - Consolidate device tracking into one entity, only use GPS platforms for 'not_home'
  * plant_problems.py - Count number of plants that need attention
* Notifications
  * Alarm - security photo if door opens when armed_away
  * Alarm Clock - send weather summary and image from window camera when alarm goes off
  * Security - send image from front door camera if no one's home and door opens
  * Reminder - If I'm home at 10:30pm and coffee isn't ready but alarm is set, remind me
  * Reminder - Full moon
  * Plants - Once a day reminder to water plants if more than 3 are thirsty
  * System - Notify if disk use gets high
  * System - Notify if new HA version available
  * System - Notify when critical smart home device goes offline for more than 5 minutes
* Timelapse - record JPEGs of sunrise/sunset

# House Modes
* Alarm Override - Turns off all alarm automations, sound effects, and alerts.
* Night Light Override - Prevents red night lights from coming on
* Vacation Mode
* Guest Mode

# Other Projects Used
* esp8266 related
  * [Sonoff-HomeAssistant](https://github.com/KmanOz/Sonoff-HomeAssistant)
  * [ESPEasy](https://github.com/letscontrolit/ESPEasy)
  * [AiLight](https://github.com/stelgenhof/AiLight)
  * [esp8266-milight-hub](https://github.com/sidoh/esp8266_milight_hub)
  * [Bruh Multisensor](https://github.com/bruhautomation/ESP-MQTT-JSON-Multisensor)
* HA addons
  * [Floorplan](https://github.com/pkozul/ha-floorplan)
  * [custom-ui](https://github.com/andrey-git/home-assistant-custom-ui)
  * [dasher](https://github.com/maddox/dasher)
* [forever-service](https://github.com/zapty/forever-service) For Python scripts as services
* My Scripts
  * [raspi-pir-mqtt-homeassistant](https://github.com/oakbrad/raspi-pir-mqtt-homeassistant) Publish connected PIR sensor to MQTT on a Raspberry Pi
* Media Software
  * [Transmission](http://transmissionbt.com) torrent manager
  * [sabnzbd](http://sabnzbd.org) NZB queue manager
  * [Plex](http://plex.tv) Media management & server
