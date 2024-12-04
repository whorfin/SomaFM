![feat_img](screenshots/playing.jpg)
# Python SomaFM Player
This simple player for [SomaFM](https://somafm.com/) keeps the distractions, and system resource utilization, to an absolute minimum. The look of this player was inspired equally by the excellent SomaFM terminal interfaces which were already available, and the 80's hacker aesthetic that one may find nostalgic while listening to a Shoutcast stream at 2AM.

Known to work on Linux (including Raspberry Pi, Chrome OS's Crostini and Chromium OS Universal Chroot Environment[^crouton]) and Mac OS.  As an added bonus, high quality Chromecast audio casting is supported.

[^crouton]: For a simple audio-only installation without the need for any X11 or desktop shenanigans:
    - Download [crouton](https://github.com/dnschneid/crouton)
    - `$ sudo sh crouton -r focal -t audio`
    - `$ sudo enter-chroot`
    - `$ sudo apt install mpv python3-requests python3-colorama`
    - ...and if you want to use Chromecast, also do this:
    - `$ sudo apt install python3-pychromecast`

For an up-to-date list of what's new, check the [Changelog](CHANGELOG.md)


## whorfinized
Huge thanks to @MS3FGX for the inspiration and original version.  This has moved far enough along its own path to no longer be relevant as a fork.
Support for players we don't use has been removed, specializing the code for optimized `mpv` support.
This branch is going further, as an `mpv`-only player, we now use unix-domain IPC sockets to communicate with `mpv`.
This means we are no longer parsing a "scraped" text GUI but instead using a documented and supported API.  Not only is this correct, it establishes the base for dealing with upcoming FLAC and HLS support, Love/WTF activation (done!), and clean future work.

FLAC over HLS is now supported.  Note that SomaFM seems to have changed publication formation, so at the moment this may not activate.

After long experiments with metadata parsing, we now instead poll the API for track changes.
This allows full artist/album/title for all mechanisms [regular, HLS and cast] without costing SomaFM a dupe play.
Note that track titles will in general not be perfectly synchronized with what is playing, for reasons ranging from the stochastic polling to asynchrony between the playout servers and track information API.

Windows support is dropped; Unix Domain Sockets are awesome and we have no interest in arsing about with Windows named pipes.  Likewise, perhaps moreso, with tty and termios.

Previously, the main features added to `mpv` launch were robust reconnection by leveraging playlist looping, and fast start, along with `pipewire` support.
Importantly, channel stream extraction parsing is improved to always use the highest quality codec at the highest bitrate; previous logic was dependent on json ordering and assumed the first entry was the best, which incorrectly resulted in mp3.
Desktop notification was yeeted along with channel icon download, and the channel list is downloaded directly on every launch, and not written to a file.  Caching this caused problems when channels were updated.

## Installation
This version is not the same as the version of similar name on PyPi.  One thus needs to clone and install or run from this repository; no need to install if you don't want to, you can just run the `somafm` executable.

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
somafm --random
```

## Optional Arguments
While not required for basic usage, the following arguments are also available:

#### --list
Download the latest master list of SomaFM channels and display their descriptions.

#### --stats
This option shows the number of listeners for each currently online SomaFM channel, along with a total listener count.

#### --cast
If you have the [pychromecast](https://github.com/balloob/pychromecast) library installed, this option starts playback of the given SomaFM channel on the given Chromecast device. 

AAC quality is pushed, the playing channel is kept updated, and exiting will kick the Chromecast device back to the "ambient" screen if enabled.

Tested on Chromecast 3rd Gen [NC2-6A5].

#### --audio
The default `auto` will give a go at auto-detecting based on your OS defaults, while `help` will probe and list available devices.
If you have very particular needs, you can use this flag to choose your weapon.

## Supported Player
This program requires `mpv` to be installed, which it controls via IPC over UDS:
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
