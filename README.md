This is an old project revived from the old burgerbot/ambibot.
The aim of this project is to build a simple 2WD Drive Robot using ROS2 packages.

#### You'll Need:  
- Raspberry Pi(brain)  
- ESP32 (talk to the motors)  
- L298N Motor Driver  
- RP Lidar A1M8  
- Caster Wheel  
- Chassis of your choice

  
# Prerequisites
- Ubuntu 22.04 Server (on RPI)
- Ubuntu 22.04 Desktop (on Host PC)
- ROS2 Humble Distro
- Arduino IDE 1.8.19

## TO-DO: Update README.md

## Steps to follow:  
&ensp;&ensp; a. Clone this repository  
&ensp;&ensp; b. Clone Lidar repository inside ~/dev_ws/src/  
&ensp;&ensp; &ensp;&ensp; &ensp;&ensp; &ensp;&ensp; (Follow this repo to install [sllidar_ros2](https://github.com/Slamtec/sllidar_ros2.git))  
&ensp;&ensp; c. Upload esp32-motor-control-sketch.ino to ESP32  
&ensp;&ensp; d. Test the motors using any Serial Monitor  
&ensp;&ensp; e. Test Lidar scan in RViz
```
mkdir burgerbot-revived
cd ~/burgerbot-revived
git clone [https://github.com/sufruuu/burgerbot-revived.git](https://github.com/sufruuu/burgerbot-revived.
cd ~/dev_ws                   # ~/robot_ws in RPI
colcon build --symlink-install
source ~/.bashrc
```
### Command to launch the nodes:
```
ros2 launch 
