# APF-simulator 
## Introduction
The main idea behind artificial potential field methods is finding a function that represents the energy of the system,and generating a force on the robot so that the energy of the system is minimized and reach it’s minimum value, preferably only, at the goal position.

This repository contains python,cpp,matlab simulator for APF
## Link to the documentation
https://drive.google.com/drive/folders/0B0UXcR6jjCx3UnBMYzFaN09SYUE

## Installation and Usage
Simulator requires [Python](https://www.python.org/) or Cpp to run.
>Make sure you have Python 2.7(or later) installed. Open the terminal and enter the 'python' (without quotes) command, if the python shell doesn't run, execute the following commands:
```sh
$ sudo apt-get install python2.7
$ sudo apt-get install python-pip python-dev build-essential 
$ sudo pip install --upgrade pip 
$ sudo pip install --upgrade virtualenv 
```
Below Python packages are to be downloaded and installed to their default locations. 
- xlrd
>If not installed, execute the following command
>```sh
>$ pip install xlrd
>```
- opencv
>If not installed, refer [OpenCV Python  Installation](http://docs.opencv.org/2.4/doc/tutorials/introduction/linux_install/linux_install.html)
- numpy
>If not installed, execute the following command
>```sh
>$ pip install numpy
>```
To run the simulator, clone the repository and run the following commands
- python
```sh
$ cd APF-Simulator/PythonCode
$ python simulator.py
```
- cpp
>If Opencv not installed, refer [OpenCV C++ Installation](http://docs.opencv.org/2.4/doc/tutorials/introduction/linux_install/linux_install.html)
```sh
$ cd APF-Simulator/C++Code
$ make
$ ./bin
```

### Contribution
Want to contribute? Great!

1.Fork it!
2.Create your feature branch: git checkout -b my-new-feature
3.Commit your changes: git commit -m 'Add some feature'
4.Push to the branch: git push origin my-new-feature
5.Submit a pull request :D
