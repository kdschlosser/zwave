# zwave
Pure Python ZWave Stack


***NOT FUNCTIONAL***
--------------------

This library is not functional yet. It is being developed and will be 
available in the near future. So make sure to check back in.

If you would like to assist in the development that would be great. 
It is a large undertaking to write a Z-Wave stack so I could use the help.  
Open an issue and let me know what you are going to work on and I will explain 
how things are currently being done, how they will hopefully work and why I am 
doing things the way that I am doing them. 


***GOALS***
---------

* Written in Python code only. 
  I do not want to have any code other than python code being used.
* User friendly. This is a tough nut to crack but I do think it is possible. 
  Easy to use is the name of the game. Python is considered to be a beginners 
  programming language and I am not saying that as something to down play it 
  because it is an extremely powerful programming language once you dig deep 
  into it. I am providing all of the bits and pieces that will make it easy 
  to integrate into a UI.
* Fast. It has to be fast. The software should not be the thing that is what 
  is limiting the speed. That means using threads to control the different 
  portions of the library.
* Not specific to a communication method. What I mean by this is it will be the 
  users responsibility to make the connection to the host device.
  This library will be completely ignorant to how the data is being passed to 
  the controller device. The only thing this going to do is call a user supplied 
  read and write functions. So if a user wants to plug in a USV to a raspberry PI
  and create a telnet connection from a PC to it so they can have the stack 
  running on a powerful computer but have the UZB located centrally in the home, 
  that is something that will be able to be done.


Dynamic construction of of nodes. I do not want to have to define devices in 
some kind of a database in order to use this library. That is how moct stacks 
currently work. The stack has knowledge of what command classes are supported 
for a device before the device is added to the network. This is not how I want 
to go about it. A representation of a node is going to be build dynamically 
and supported command classes will be added to that representation at the 
time they are added to the network. There will be a database of sorts that 
holds static information about a node once it is added to the network. 
This is done to improve the stack startup time. the loading of that information
will work just like when a node is added except the zwave commands to collect 
the information will not need to be sent. By doing this it will allow the node 
to become available for use almost immediatly after the stack starts up. 

By having the command classes added to a node representation dynamically 
I am able to leverage python so a user would be able to subclass a command class 
and extend it so that it contained code that would be responsible for creating 
the UI element for that specific command classes function. the dynamic creation 
of the node representation will use the subclass instead of the build in command 
class so whatever functions the user as added to the command class would be 
available in the node representation if that command class is supported by the 
node. 

Several years ago I had made extensive modifications to the openzwave binding 
to Python. The changes I made increased the performance by 1000% at least. a 50 
device network has a stack startup time of only a few seconds. This was done by 
creating a thread for each node on the nmetwork and having a thread that would 
control the data being received and transmitted. This allowed the stack to do 
whatever internal processing it needed to do without causing communications to 
the nodes on the network to stop. There is no reason why communications with 
the network should have to stop while a UI processes a state change for a node.


4.7.4 Bridge Application Command Handler Command