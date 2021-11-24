# Create GUI apps in Python

Followed tutorial https://www.youtube.com/watch?v=YXPyB4XeYLA  
More videos in this playlist https://www.youtube.com/playlist?list=PLCC34OHNcOtoC6GglhF3ncJ5rLwQrLGnV  

Thanks to https://datatofish.com/matplotlib-charts-tkinter-gui/ for showing how to plot charts in tkinter window itself, and not in a new window

_Need to install Pillow for images handling_  

    pip install pillow

_Module requests is for json\_request example_

    pip install requests

_Modules numpy and matplotlib are for matplotlib example_

    pip install numpy  
    pip install matplotlib  

_Need tkcalendar to work with Calendar_

    pip install tkcalendar  

_To run Text to Speech_

    pip install pyttsx3
    sudo apt install libespeak1 espeak ffmpeg

_To play sound_

I tested pydub, but it doesn't have a stop() feature.  
I tested simpleaudio, but it doesn't have a pause() feature.
I checked musicplayer, but it is not maintained anymore.
I checked sounddevice, but it is too complex.
The easiest way is pygame, even though just playing sounds is not the objective.
Module mutagen is used to get the length of the sound

    pip install pygame
    pip install mutagen

_To use Excel_

    pip install openpyxl


_Code 058 needs pandas, numpy, xlrd_  
**xlrd is needed to open old Excel format .xls.** Don't need to install it if you are not going to work with .xls

    pip install pandas
    pip install numpy
    pip install xlrd

_To use PDF_

The tutorial teaches PyPDF2, but this is not maintained. Use pymupdf

    pip install pymupdf

_To do HTML parser using beautiful soup_

    pip install beautifulsoup4

___ 
# Assets

1. Star icon
    * <div>Icons made by <a href="https://www.flaticon.com/authors/pixel-perfect" title="Pixel perfect">Pixel perfect</a> from <a href="https://www.flaticon.com/" title="Flaticon">www.flaticon.com</a></div>
    * https://www.flaticon.com/free-icon/star_1828884?related_id=1828884
    * I have resized the icon to 48x48
  

2. Song Orchestral
    * <div>Song made by <a href="www.youtube.com/c/Tadon" title="www.youtube.com/c/Tadon">www.youtube.com/c/Tadon</a> from <a href="https://opengameart.org/content/forward-operating-base/" title="opengameart.org">opengameart.org</a></div>
    * https://opengameart.org/content/forward-operating-base
    * https://opengameart.org/content/first-snowfall

3. Music player icons
    * <div>Icons made by <a href="https://www.flaticon.com/authors/pixel-perfect" title="Pixel perfect">Pixel perfect</a> from <a href="https://www.flaticon.com/" title="Flaticon">www.flaticon.com</a></div>
    * https://www.flaticon.com/packs/music-225

4. CAM logo
    * https://atletico.com.br/paginas/simbolos-e-marcas
    * I resized it to 398x600

5. Bell icon
    * <div>Icons made by <a href="https://www.flaticon.com/authors/pixel-perfect" title="Pixel perfect">Pixel perfect</a> from <a href="https://www.flaticon.com/" title="Flaticon">www.flaticon.com</a></div>
    * https://www.flaticon.com/free-icon/bell_1827422?term=bell&page=1&position=11&page=1&position=11&related_id=1827422&origin=search
    * I have resized the icon to 150x150

6. Bitcoin icon
    * <div>Icons made by <a href="https://icon54.com/" title="Pixel perfect">Pixel perfect</a> from <a href="https://www.flaticon.com/" title="Flaticon">www.flaticon.com</a></div>
    * https://www.flaticon.com/free-icon/bitcoin_893071?term=bitcoin&page=1&position=3&page=1&position=3&related_id=893071
    * I have resized the icon to 128x128