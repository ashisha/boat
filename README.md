# craft
Craft lets you instantly share files over HTTP from command line. You can use craft to share files over local network, or transfer to mobile devices if they are on same WiFi network!


# Features
* Spawns a HTTP server per file, you don't need to worry about port numbers
* The spawned HTTP servers are auto-managed, they kill themselves after a certain timeout or maximum number of requests
* Support for QR code generation to assist mobile devices


# Requirements
* Python 2.x
* Python Imaging and QR libraries (optional):
```
  pip install Pillow
  pip install pyqrcode
```

# Installation
Installing craft is easy, fire up your terminal, and execute the following commands in order:
```
  sudo wget https://raw.github.com/ashisha/craft/master/craft -O /usr/local/bin/craft
  sudo chmod +x /usr/local/bin/shuttle
```

# PS
* Tested only on Mac with Python2.7 (pulls welcome)
* Thank you!
