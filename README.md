# ebb
```
Autonomous enviornmental boat class for skimming marine debris and floaters. 
```
> Take a look at our [video submission](https://www.youtube.com/watch?v=1hm2KFQpkuc&feature=youtu.be "EBB Jetson Devel Challenge") to the nVidia Jetson TX2 Developer Challenge, and look for incoming updates including autonomous object detection and pathfinding code!

---
#### Prototype
A diagram and BOM of the boat are available [in pdf format](https://goo.gl/9HjLTM). 

Current implementation with manual control using a wii remote work both on raspberry pi and nvidia tx2.  For tx2 support install motor hat libraries from [github.com/renowator/Adafruit-Motor-HAT-Python-Library](https://github.com/renowator/Adafruit-Motor-HAT-Python-Library) and [github.com/renowator/Adafruit_Python_GPIO](https://github.com/renowator/Adafruit_Python_GPIO).

> You can try run the current code with startup.sh. May have to run as su or add user to i2c and relevant groups.
Be aware this script uses tmux and leaves the roscore running at 'tmux attach -r ros'.
---

**Thanks for checking it out at this early stage!**




