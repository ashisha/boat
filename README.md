# craft
Craft lets you instantly share any file over HTTP from command line. You can use craft to share files over local network, or transfer to mobile devices if they are on same WiFi network!

![](https://github.com/ashisha/craft/blob/master/screenshot/craft.png)

# Usage
* To share a file called file.txt, run ```craft file.txt```
* craft will spawn a HTTP server and tell you the corresponding URL
* You can now download file.txt on the local network by going to URL via any client (browser, curl, wget)
* Additionally you can ask craft to generate a QR code: ```craft --qr file.txt```
* craft will then generate a QR code for you which can be scanned easily on mobile devices
* For more help, run ```craft --help```

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
  sudo chmod +x /usr/local/bin/craft
```

# PS
* Tested on Mac and Linux (ArchLinux) with Python2.7 (pulls welcome)
* Thank you!
