# Back-seat flying
Generic scripts to control a Pixhawk-based UAS through MAVROS running on an onboard companion computer.
  - PX4 firmware greater than v1.9.0. Flight mode for PX4 is 'Offboard'.
  - ArduPilot firmware greater than v4.0.5. Flight mode for ArduPilot is 'Guided'.

# Mavros Setup Insutruction - Fall 2021

### Companion Computer OS Configuration
Configure ubuntu 20.04 appropraitely depending on your companion computer. It can be downloaded [here](https://ubuntu-mate.org/download/)
  - Raspberry Pi 4 / Odroid: Download the armhf 32 bit version [here](https://ubuntu-mate.org/download/armhf/) onto an sd-card and configure it following the directions based on what OS your main laptop is running. [Linux](https://itsfoss.com/format-usb-drive-sd-card-ubuntu/) or [Windows](https://ubuntu.com/download/iot/installation-media) (scroll to "On Windows" section).
  - Up Core: Follow the instruction on this [page](https://github.com/up-board/up-community/wiki/Ubuntu_20.04).
  - Intel NUC: NUC's from the RRC should already be running 18.04, this is okay.

### Companion Computer ROS/Mavros Install
Now that an ubuntu operating system is downloaded we can install ROS and mavros. 
  - ROS Noetic: Follow the instructions at the page [here](http://wiki.ros.org/noetic/Installation/Ubuntu)
  - Mavros: Once ROS Noetic is installed use the following command to install Mavros
    ```
    sudo apt-get install ros-kinetic-mavros ros-kinetic-mavros-extras
    ```
    You will also need GeographicLib which can be installed with these commands;
    ```
    wget https://raw.githubusercontent.com/mavlink/mavros/master/mavros/scripts/install_geographiclib_datasets.sh
    sudo bash ./install_geographiclib_datasets.sh
    ```
    You need to be in the same directory as ```install_geographiclib_datasets.sh``` to run the second command.
    You can ensure mavros is installed correctly in your system space with:
    ```
    roscd mavros
    ```
    You should be brought to
    ```
    /opt/ros/noetic/share/mavros
    ```
  - IP Address
    Run:
    ```
    sudo apt-get install net tools
    ```
    Then use the command
    ```
    ifconfig
    ```
    and something similar to below should be retruned in the ```wlan0``` section:
    ```
    wlan0: flags=4163<UP,BROADCAST,RUNNING,MULTICAST>  mtu 1500
        inet 10.212.146.230  netmask 255.255.0.0  broadcast 10.212.255.255
        inet6 fe80::cb1f:1655:4a91:3e58  prefixlen 64  scopeid 0x20<link>
        ether dc:a6:32:a1:30:8a  txqueuelen 1000  (Ethernet)
        RX packets 1003  bytes 864468 (864.4 KB)
        RX errors 0  dropped 0  overruns 0  frame 0
        TX packets 692  bytes 299630 (299.6 KB)
        TX errors 0  dropped 0 overruns 0  carrier 0  collisions 0
    ```
    The ip address follows ```inet``` in this case it would be ```10.212.146.230```
    It is helpful to note this for remoting into your companion computer.

### Mavros Set-up
Now we need to configure mavros so you are ready to fly. 
First navigate to the launch files with 
```
roscd mavros/launch
```
Use the following command to allow file editing:
```
chmod 777 px4.launch apm.launch
```
In your favorite text editor change line 5 to match the following:
```
<arg name="fcu_url" default="/dev/ttyUSB0:921600" />
```

### Pixhawk Configuration
For this section you will need to download the following programs onto your laptop (not necessary for companion computer)
  - [QGroundControl](https://docs.qgroundcontrol.com/master/en/getting_started/download_and_install.html)
  - [MissionPlanner](https://ardupilot.org/planner/docs/mission-planner-installation.html)

### Companion Computer Scripts Install
Clone this repository in 
```bash
/catkin_ws/src
```
Then run
```bash
catkin_make
```
in the ```/catkin_ws ``` directory.

### Using PX4 vs Ardupilot In Companion Scripts
Use the ```self.my_state``` variable in ```start_up.py``` to make the scripts usable for PX4 and Ardupilot. Use
```python
self.my_state = "GUIDED"
```
for Ardupilot, and 
```python
self.my_state = "OFFBOARD" 
```
for PX4.
