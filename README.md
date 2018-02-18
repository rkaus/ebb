# ebb
Autonomous enviornmental boat class for skimming marine debris and floaters.
Current implementation with manual control using a wii remote which work both on raspberry pi and nvidia tx2. For tx2 support install motor hat libraries from github.com/renowator/Adafruit-MotorHAT-Python.
Incoming updates with autonomous object detection and pathfinding.

You can try run the current code with startup.sh. May have to run as su or add user to i2c and relevant groups.
Be aware this script uses tmux and leaves the roscore running at 'tmux attach -r ros'.

Thanks for checking it out at this early stage. Come back for updates!
