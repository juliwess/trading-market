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

Run the following command from the main directory

`cmake -S . -B build && cmake --build build && cmake --install build`

Now go to the folder extra and launch the server by using:

`python3 server.py`

You will then be able to start as many clients as you wish by using:

´python3 client.py´ 

in a different terminal window

The GUI version is still in progress and not to be used