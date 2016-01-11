# Untitled Sentiment Analysis Project
This is a sentiment analysis project in python using twitter and it's API

Implementation of tweepy
========================

<h2>Libraries used so far:</h2>
 
 For Python 3.4 and above
 
<h2>Installing Tweepy:</h2>
<h3>For Windows:</h3>

Using the GitHub repository
   
Install by running these commands in command prompt:
    
    git clone https://github.com/tweepy/tweepy.git
    cd tweepy   
    python setup.py install

Using pip

    pip install tweepy
    
<h3>For Linux:</h3>
Download the tweepy GitHub repository from [here](https://github.com/tweepy/tweepy/archive/master.zip)
Extract and run the console from the directory and install using the command

    python setup.py 
    
Using pip

    pip install tweepy


<h3>Usage:</h3>

Standard example to pull twitter feeds based on

   [Streaming tweets example](https://github.com/tweepy/tweepy/blob/master/examples/streaming.py)

Test code : Extracting only the english language tweets using
    [twitter_streaming.py](https://github.com/DeamonSpawn/UntitledSAProj/blob/master/src/twitter_streaming.py)
   
Output of the tweet stream is in the JSON format from which the "text:" specifies the tweet which is extracted from the JSON text.

_Output:_

Output is stored to a [output text file](https://github.com/DeamonSpawn/UntitledSAProj/blob/master/test/tweetsansJSON.txt) using the command line
 
    python twitter_streaming.py >> output.txt 

The extraction process can be allowed to run until rate limitation by twitter occurs or alternatively the process can be interrupted using

    Ctrl+c

Implementation of a Wordbank based sentiment score using Patricia Tries and Plotting the sentiment analysis using Matplotlib
============================================================================================================================
<h2>Libraries used so far:</h2>
 
 For Python 3.4 and above
<h2>Installing NLTK:</h2>
<h3>For Windows:</h3>

NLTK - The fastest way to install is using pip
NLTK dependancies:

Numpy - Requires a GNU compiler like [MinGW](http://www.mingw.org/wiki/Getting_Started) or 
[Visual Studio 2013 or higher](https://www.visualstudio.com/en-us/downloads/download-visual-studio-vs.aspx) installed

<h3>Using Visual Studio:</h3>
The Numpy installation looks for the Visual Studio file _vcvarsall.bat_ by default,
and installing Visual Studio is sufficient to meet this requirement and install Numpy
    
<h3>Using MinGW:</h3>

- [Install MinGW](http://www.mingw.org/wiki/Getting_Started) with C++ Compiler option checked
- Add C:\MinGW\bin to your PATH

<h3>Installing MinGW and MSYS</h3>

Download and run mingw-get-inst (the download link above).

Select "Use pre-packaged repository catalogues".

Review and accept the License agreement.

Please note that MinGW should be installed to a directory path that doesn't contain any spaces.

This method has been tested with a directory path of C:\MinGW.

Select C++ Compiler and MSYS Basic System as optional components.

Wait until every package has been downloaded and installation is finished.

<h3>Setting up MSYS</h3>

Go to your MSYS folder (found at <MinGW installation folder>\msys\1.0, C:\MinGW\msys\1.0 in this example), 
open etc\fstab with a text editor (for example Notepad) and add the following line at the end of the file:

    C:\MinGW\   /usr/local

On Windows Vista and newer, you'll need additional steps to make MSYS fully work if User Account Control is enabled (it is by default).

Go to your MSYS folder (C:\MinGW\msys\1.0 here), open msys.bat with a text editor (right-click -> Open With -> Notepad or equivalents) 
and add the following line after   
@echo off:

    cd "C:\MinGW\msys\1.0"


And if your MSYS installation drive is not the disk Windows is installed on, add one more line:

    C:(MSYS drive)

After saving the file, right click on _msys.bat_ and choose "Run as Administrator".
You will need to do this every time you run MSYS. 
After that, programs requiring admin rights (such as install and patch) will work.
Testing MinGW/MSYS installation

Open the MinGW shell (MSYS) by running msys.bat.
Run the following commands:

    make -v
    gcc -v
    
They should output something. Check if something goes wrong.
Compilation and installation of the required packages
 
To compile and install these packages and avoid the error 'wget: command not found', first you need to install the following commands: 
(To compile on Windows 7, the service "application experience" must be activated and running)

IN MSYS:

    mingw-get install msys-wget
    mingw-get install msys-unzip
    mingw-get install msys-patch

If you get following error: configure: error: cannot run C compiled programs. 
, one of the reasons could be your anti-virus, that silently deletes a.exe binary files. 
Try to temporarily disable anti-virus software and compile again

- In PYTHONPATH\Lib\distutils, create a file distutils.cfg and add these lines:
    
        [build]
        compiler=mingw32
    
Then install using either

    pip install numpy
    pip install nltk
    
or alternatively using the Git Repositories
    
    git clone https://github.com/numpy/numpy.git
    cd tweepy
    python setup.py install
    git clone https://github.com/nltk/nltk.git
    cd tweepy
    python setup.py install
    
    
<h3>For Linux:</h3>
If you have python 3.4.3 or higher you have pip installed
The same instructions for windows with pip can be performed in linux

After NLTK is installed open the Python interpreter and type
    
    >>import nltk
    >>nltk.download
    
In the NLTK Downloader dialog box select _All packages_ and click the _Download_ button


<h2>Installing Matplotlib:</h2>
<h3>For Windows:</h3>

Matplotlib Dependencies:

- numpy 1.6 (or later)
Already installed for NLTK

- libpng 1.2 (or later)

 To be installed via MinGW 
If MSYS is not setup the instructions are [here](https://github.com/DeamonSpawn/UntitledSAProj#setting-up-msys).

 If not installed Open the _MinGW setup_ and select and install the _MSYS basic system package_

 libpng requires zlib to install zlib do the following,

 In MSYS:

        wget http://zlib.net/zlib-1.2.8.tar.gz
        tar xvfz zlib-1.2.8.tar.gz
        cd zlib-1.2.8
        make -f win32/Makefile.gcc BINARY_PATH=/usr/local/bin INCLUDE_PATH=/usr/local/include LIBRARY_PATH=/usr/local/lib install
        cd ..
    
 then proceed with
    
        wget http://sourceforge.net/projects/libpng/files/libpng15/older-releases/1.5.16/libpng-1.5.16.tar.xz/download
        tar xvfJ libpng-1.5.16.tar.xz
        cd libpng-1.5.16
        mv INSTALL INSTALL.txt
        ./configure
        make install
        cd ..

- freetype 2.3 or later
 
 To be installed via MinGW 

 In MSYS:

        wget http://sourceforge.net/projects/libpng/files/libpng15/older-releases/1.5.16/libpng-1.5.16.tar.xz/download
        tar xvfJ libpng-1.5.16.tar.xz
        cd libpng-1.5.16
        mv INSTALL INSTALL.txt
        ./configure
        make install
        cd ..

- dateutil 1.1 or later

 If using pip, easy_install or installing from source, the installer will attempt to download and install python_dateutil from PyPI. 
Note that python_dateutil also depends on six. 
pip and other package managers should handle installing that secondary dependency automatically.

- pyparsing

 If using pip, easy_install or installing from source, the installer will attempt to download and install pyparsing from PyPI.

- six 1.4 or later

 Also a dependency of dateutil.

- pytz


<h3>Usage:</h3>

Test Code: To evaluate our twitter tweets positive and negative sentiments we implement
[tweets_score.py](https://github.com/DeamonSpawn/UntitledSAProj/blob/master/src/tweets_score.py). 
It utilises a Patricia Trie constructed using a python dictionary data structure 
with wordbanks [negative-words.txt](https://github.com/DeamonSpawn/UntitledSAProj/blob/master/lib/negative-words.txt) 
and [positive-words.txt](https://github.com/DeamonSpawn/UntitledSAProj/blob/master/lib/positive-words.txt) as data. 
Using these tries we optimise the wordbank search for positive and negative word matches.
Test Tweet data used in this example is [here](https://github.com/DeamonSpawn/UntitledSAProj/blob/master/test/tweetsansJSON.txt).

_Output_
 
positive = 78
negative = 20
unknown = 120

Shown by a plot using pythons Matplotlib

![plot_tweetsansJSON](https://github.com/DeamonSpawn/UntitledSAProj/raw/master/res/plot_tweetsansJSON.png)
 