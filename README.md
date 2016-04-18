# juliet
A mirror that displays information by using a two-way mirror and an LCD screen, powered by Raspberry Pi.

juliet is designed to run on a Raspberry Pi connected to an LCD screen behind a two-way mirror, giving the illusion of text on a mirror surface.
To acheive this, the python program uses `pygame` and takes control of the Linux framebuffer, which allows low level control over the whole screen.
More infoormation about the project in general can be found on the project's Hackaday page: <https://hackaday.io/project/9595-juliet-magic-mirror>.
The purpose behind making the app a python script and not a webserver hosted screen like other mirrors is so that the code can be run without having to install a webserver, which incurs some overhead.
This also gives the project complete control over what gets drawn every frame and access to custom layout possibilities if needed.

In addition to being closer to the metal, python allows the usage of many excellent electronics libraries for the Raspberry Pi's GPIO pins.
This allows easier integration of external sensors and instruments with the mirror, like proximity sensors to detect human prescence and turn on.

### Installation
This python program requires a number of external resources, like default fonts, icons, and API keys.
In order to use this program, a number of programs and files need to be installed/moved to the main directory of this program (ie. juliet/Comme-Thin.ttf).
These files are:

`pygame` - The basis for using the low-level Linux framebuffer. Your distro should have a way of installing this already figured out, if it isn't already. Usually this involves searching your distro's package manager for the pygame package and installing it. Otherwise, pygame's website can be found here: http://www.pygame.org

`Comme-Thin.ttf` - A clean, modern font that matches the feel of a simple interface.
Found here: <http://www.fontsquirrel.com/fonts/comme>. Copy the `Comme-Thin.ttf` file to the main directory.

`Forecast.io Wrapper` - A simple to use library for interfacing with forecast.io's API calls.  
To install, run `pip install python-forecastio`, as per <https://github.com/ZeevG/python-forecast.io>

`weathericons.ttf` - A scalable ttf Unicode font that features a large number of weather icons.
Found here: <https://erikflowers.github.io/weather-icons/> (Thanks Erik!). Also copy this to the main directory.

`modules/weather_module/api.key` - A single line textfile containing your `forecast.io` API key.
This key can be acquired by making an account over at <https://developer.forecast.io/>

### Project Terms
---
**Module** - a python file which features a class that implements the base juliet_module.py.
Modules are the basis of all visible objects in juliet.
Each module has three basic functions and some parameters:

`__init__(self, _id, ...)`

Pretty straightforward, the standard constructor of the module.
This must contain at least the `_id` field as the first parameter.
In addition, any number of additional paramters needed by the main program at module initiation should be added here.

As an example, the default text module takes an initial string as a parameter of it's `__init__` function.

`draw(self, surface)`

This function gets called each frame that the module is in a dirty area of the screen, that is, an area which needs to be updated.
This function takes a surface that is given to it by the main program loop, which is usually a rectangle the size of `mod_rect`.
The module uses this space to draw its contents.
The surface is sort of like a window in your desktop environment/window manager, it is the only space on the screen that the module can affect.

In addition, `draw()` returns the rectangle that now needs to be updated due to drawing to the screen, usually the result of a `surface.blit()` pygame call.

As an example, the default text module finds the size of its text and puts it into the `mod_rect` field.
Then, during the draw call, the module renders its text to the surface, which eventually gets put onto the screen.

`update(self)`

This function gets called each frame. This allows the module to update its state, which gives rise to automatic weather, changing text, etc.
This function should not rely on information from the main program.
It should be able to get all the information it needs from API calls or the system itself.

Modules also have some basic parameters which affect their behavior in the system, namely:

`mod_name`: A name for the module readable by a computer (ie., no spaces or crazy characters ideally)

`mod_id`: The unique ID of this module among other modules currently used

`mod_rect`: The size and position of the module's rectangular footprint in the module.
This gets used during the `draw()` call in order to give the module an appropriately sized surface for drawing.

---

**Importer** - The python script which finds all installed modules at startup and during runtime if called upon.

## Code Structure
The main code loop can be found in `juliet_graphics.py`.
The main loop calls the `update()` function of each module that is currently active,
figures out which modules are now a part of changed portions of the screen,
then calls the `draw()` function of each module that touches a dirty section of the screen.

*To be completed at a later point in time (02-09-2016).  
In the meantime, check out the project page on Hackaday here: <https://hackaday.io/project/9595-juliet-magic-mirror>*
