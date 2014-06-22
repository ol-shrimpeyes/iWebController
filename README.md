iWebController
==========

A python/flask frontend for SSHMediaControls on *jailbroken* iOS devices!

This software is in its very early days. This is very prelimenary. Everything here was done in about 15 minutes.

Setup
-----
requires

* [Python 2.7](https://code.google.com/p/yangapp/downloads/detail?name=python_2.7.3-3_iphoneos-arm.deb)
* [pip](https://bootstrap.pypa.io/get-pip.py) *(install as root)*
* [fake-libgcc](https://code.google.com/p/ipod-tools/downloads/detail?name=fake-libgcc_1.0_iphoneos-arm.deb)
* GNU C compiler (in cydia)

required modules:
* flask
* sh

`pip install flask sh` *(run as root)*

in server.py change the bottom line from
`app.run(degug=True)` to `app.run(host={{your local ip}})`
