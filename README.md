iWebController
==========

A python/flask frontend for SSHMediaControls on *jailbroken* iOS devices!

This software is in its very early days. This is very prelimenary. Everything here was done in about 15 minutes.

Setup
-----
### requires:

* [Python 2.7](https://code.google.com/p/yangapp/downloads/detail?name=python_2.7.3-3_iphoneos-arm.deb)
* [pip](https://pip.pypa.io/en/latest/installing.html) *(install as root)*
* [fake-libgcc](https://code.google.com/p/ipod-tools/downloads/detail?name=fake-libgcc_1.0_iphoneos-arm.deb)

#### in cydia:

* git *big suprise there*
* GNU C compiler
* OpenSSH
* SSHMediaControls

#### required modules:
* flask
* sh

`pip install flask sh` *(run as root)*

### configuring:

`cp ./default/conf.py ./conf.py`

Change the `HOST` variable in conf.py to your internal ip. Only set `DEBUG` to `True` if you know what this is.

#### running:

	git clone git://github.com/ol-shrimpeyes/iwebcontroller
	cd ./iwebcontroller
	python server.py