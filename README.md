# Translation app for ubuntu
ubuntu translation app

### Summary
  This is a translation app for ubuntu system, or other ubuntu like system.<br>I use python to get selection word and make a translation request to some translation api like google translate and so on.And I use electron to make the main ui for ubuntu.My ubuntu version is 22.10

### Technology Stack
1. python == 3.8
2. electron_ui is refer to https://github.com/Wisgon/electron-react-boilerplate-multiple-windows
3. antdesign
4. websocket

### Requirement
1. `sudo apt install libfuse2`  This is for running .AppImage file which electron build it in Linux System.
2. `pip install -r requirements.txt`
3. Because pynput use xlib, so wayland is not able to use,you should disable wayland:`sudo gedit /etc/gdm3/custom.conf `,if you can't find gdm3, find something like "gdm".Then, change the line like "# WaylandEnable=false",delete "#" to uncomment it.And then restart your computer.After restarted, if you have something wrong with your system, please recover the "custom.conf".Because ubuntu22.04 use wayland in some window,so if wayland is active status, there is some window that this app can't communicate.
