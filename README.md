![feat_img](screenshots/playing.jpg)
# Python SomaFM Player
This simple player for [SomaFM](https://somafm.com/) keeps the distractions, and system resource utilization, to an absolute minimum. The look of this player was inspired equally by the excellent SomaFM terminal interfaces which were already available, and the 80's hacker aesthetic that one may find nostalgic for when listening to a Shoutcast stream at 2AM.

Known to work on Linux (including Raspberry Pi, Chrome OS's Crostini and Chromium OS Universal Chroot Environment[^crouton]), Mac OS, and even Windows[^windows].  As an added bonus, high quality Chromecast audio casting is supported.

[^crouton]: For a simple audio-only installation without the need for any X11 or desktop shenanigans:
    - Download [crouton](https://github.com/dnschneid/crouton)
    - `$ sudo sh crouton -r focal -t audio`
    - `$ sudo enter-chroot`
    - `$ sudo apt install mpv python3-requests python3-colorama`
    - ...and if you want to use Chromecast, also do this:
    - `$ sudo apt install python3-pychromecast`

[^windows]: You need to make sure `mpv.com` is resolvable through the system `PATH`.
In the same cmd terminal where you run `somafm`, try to run `mpv`. You
should get the help banner.  Here's how this manages to work:  because
windows, `mpv.exe` is a GUI-only program with no stdio.  `mpv.com` uses
[shenanigans](https://github.com/mpv-player/mpv/wiki/FAQ#on-windows-why-does-mpvexe-not-attach-to-the-console-and-what-does-mpvcom-do) to wrap `mpv.exe` and provide standard input and output.  Because windows will prefer `.com` to `.exe` by default, a `Popen()` of `mpv` launches `mpv.com` and `somafm` is able to communicate with it over stdio.

For an up-to-date list of what's new, check the [Changelog](CHANGELOG.md)


## whorfinized
This is my fork.  Huge thanks to the original author.  I've removed support for players I don't use, simplifying the code for optimized `mpv` support.
The main features I've added to `mpv` launch are robust reconnection by leveraging playlist looping, and fast start, along with `pipewire` support.
Importantly, I've also fixed channel stream extraction parsing to always use the highest quality codec at the highest bitrate; previous logic was dependent on json ordering and assumed the first entry was the best, which incorrectly resulted in mp3.
Desktop notification was yeeted along with channel icon download, and the channel list is downloaded directly on every launch, and not written to a file.  Caching this caused problems when channels were updated.

If you aren't me and want to try this, try the `--audio auto` flag if you aren't rocking `pipewire`.

## Installation
This forked version is not backported, and thus not on PyPi as is the original.  One thus needs to pull and install or run from this repository; no need to install if you don't want to, you can just run the `somafm` executable.

## Dependencies
At minimum, this program requires Python 3 versions of the following libraries:

* [colorama](https://pypi.org/project/colorama/)
* [requests](https://3.python-requests.org/)

## Channel Selection
Simply running `somafm` with no options will start streaming "Drone Zone." In the somewhat unlikely event you wanted to listen to something else, simply give it the channel name like so:

```console
somafm "Underground 80s"
```

Channel entry is not case sensitive and uses a certain amount of "fuzzy" matching. So rather than typing out the entire name, the following will also work:

```console
somafm 80
```

Finally, if you're not sure what you want to listen to, you can pass the -r option to let the script randomly select from one of the currently active channels:

```console
somafm -r
```

## Optional Arguments
While not required for basic usage, the following arguments are also available:

#### --list
Download the latest master list of SomaFM channels and display their descriptions.

#### --stats
This option shows the number of listeners for each currently online SomaFM channel, along with a total listener count.

#### --cast
If you have the [pychromecast](https://github.com/balloob/pychromecast) library installed, this option starts playback of the given SomaFM channel on the given Chromecast device. If no device name is given, the default specified by the `chromecast_name` variable will be used.

AAC quality is pushed, the playing channel is kept updated, and exiting will kick the Chromecast device back to the "ambient" screen if enabled.

Tested on Chromecast 3rd Gen [NC2-6A5].

#### --audio
I love `pipewire`, and by default enable it without requiring config shenanigans.
If you have yet to embrace the future, you can use this flag to chose your weapon.
`auto` will give a go at auto-detecting based on your OS defaults, while `help` will probe and list available devices.

## Supported Player
This program is simply a front-end, playback requires `mpv` to be installed:
* [mpv](https://mpv.io/)

## About SomaFM
![somabanner](http://somafm.com/linktous/728x90sfm.jpg)

SomaFM is a listener-supported Internet-only radio station. That means no advertising or annoying commercial interruptions. SomaFM's mission is to search for and expose great new music which people may otherwise never encounter.

If you like what you hear on SomaFM and want to help, please consider visiting their site and [making a donation](https://somafm.com/support/).

## License
This program is free software; you can redistribute it and/or modify it under the terms of the GNU General Public License version 3 as published by the Free Software Foundation.

![](https://www.gnu.org/graphics/gplv3-127x51.png)

This program is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.

For details, see the file "COPYING" in the source directory.
