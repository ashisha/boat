# boat
Boat lets you instantly share any file over HTTP from command line. You can use boat to share files over local network, or transfer to mobile devices if they are on same WiFi network!

![](https://github.com/ashisha/boat/blob/master/screenshot/boat.png)

# Usage
* To share a file called file.txt, run ```boat file.txt```
* boat will spawn a HTTP server and tell you the corresponding URL
* You can now download file.txt on the local network by going to URL via any client (browser, curl, wget)
* Additionally you can ask boat to generate a QR code: ```boat --qr file.txt```
* boat will then generate a QR code for you which can be scanned easily on mobile devices
* For more help, run ```boat --help```

# Features
* Spawns a HTTP server per file, you don't need to worry about port numbers
* The spawned HTTP servers are auto-managed, they kill themselves after a certain timeout or maximum number of requests
* Support for QR code generation to assist mobile devices


# Installation
* [Pip](https://pypi.python.org/pypi/boat) (Recommended)
  ```
  pip install boat
  ```

* Old School
```
  git clone --recursive git@github.com:ashisha/boat.git
  cd boat
  python setup.py install
```

# Usage
## Basic
```
  boat file.txt     # prints the url you can use to download file.txt
```
## Transfer to mobile devices
```
  boat file.txt --qr    # prints the url and QR code you can use to download file.txt
```
## Advanced
```
  boat --help    # you know it
```


# PS
* Tested on Mac and Linux (ArchLinux) with Python2.7 (pulls welcome)
* Thank you!

