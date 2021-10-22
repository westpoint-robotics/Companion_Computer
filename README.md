# Back-seat flying
Generic scripts to control a Pixhawk-based UAS through MAVROS running on an onboard companion computer.
  - PX4 firmware greater than v1.9.0. Flight mode for PX4 is 'Offboard'.
  - ArduPilot firmware greater than v4.0.5. Flight mode for ArduPilot is 'Guided'.

# Install
Clone this repository in 
```bash
/catkin_ws/src
```
Then run
```bash
catkin_make
```
in the ```/catkin_ws ``` directory.

# PX4 vs Ardupilot
Use the ```my_state``` variable in ```start_up.py``` to make the scripts usable for PX4 and Ardupilot. Use
```python
self.my_state = "GUIDED"
```
for Ardupilot, and 
```python
self.my_state = "OFFBOARD" 
```
for PX$
