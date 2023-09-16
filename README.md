# trading-market
A simulated trading-market where you can buy and sell goods

# purpose
This project is intended to practice the use of Representational State Transfer(REST)-Applications
communicating via HypterTextTransferProtocol (HTTP)

Therefore the following requirements should be met:
* Client-Server-Architecture
* Statelessness
* Caching
* Hypermedia as the engine of application state (HATEOAS)
* Multi-Layer-System

# setup the project 

You will have to install cmake and python 3.11 or a newer version to build and execute the project

Run the following command from the main directory:

`cmake -S . -B build && cmake --build build && cmake --install build`

If this doesen't work yet try to install the following:
* cmake >= 3.16
* python3 >= 3.8
- python3-dev und python3-pybind11
- python3-pip3 >= 10
- Python3-Module (via pip3): pybind11, pyside6 sowie fastapi[all]
* QT Libraries >= 6.2
- qt6-base-dev und qt6-base-dev-tools sowie libglx-dev und libgl1-mesa-dev


Now go to the folder extra and launch the server by using:

`python3 server.py`

You will then be able to start as many clients as you wish by using:

`python3 client.py``

in a different terminal window

The GUI version is still in progress. If you'd like to use the market
with a Graphical User Interface run:


