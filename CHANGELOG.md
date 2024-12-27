# Version History

## December, 2024
- Release as v3.3.1
- Fix spinner
- Fix event race
- Compatibility tweak for older Requests/pre-v2 urllib3
- Disable cache for faster startup and in hopes of further squashing long uptime mpv issues
- Keep socket recv buffer maintained

## November, 2024
- Release as v3.1.0
- Switch to polling for track details; avoids issues with missed metadata observertions [recent mpv flatpak bug], simplifies code, handles HLS, and avoids duplicate playback stream in chromecast and HLS scenarios to save SomaFM un-needed stream play fees
- Indicate polling w/ spinner
- Update pychromecast and test once more
- Release as v2.7.18
- Various robustness improvements
- Unforked

## October, 2024
- Release as v2.7.15
- Humanize runtime better
- API query retry with exponential backoff

## September, 2024
- Release as v2.7.12
- Show progress of socket connection and bitrate computation
- Detect `mpv` launch failure during socket connection; `mpv` in older distros such as focal lacked IPC control
- Full agent declaration

## August, 2024
- Release as v2.7.4
- Rewrite to use IPC rather than scraping stdout UX from `mpv`
- Query tracks from API - provides album info, and works with HLS
- Support LOVE and WTF?!
- Drop stationID highlighting - station IDS are not identified by the API
    - ... and it has become very inconsistent from station to station and not all IDs are long enough for the metadata to update
- Grab audio information from player processing, not just icy-data - this supports HLS
- Added support for lossless HLS playback with track information
- Unescape metadata which remains with weird embedded escapes, especially unicode zero-width-space
- Switch to "auto" audio device default; works for everybody
    - and since `pipewire` replaces `alsa/pipewire` on more recent `mpv` versions
- Buffer usage tweaking for minimum memory
- Last old-style Release as v1.88-whorfin

## July, 2024
- Release as v1.86-whorfin
- Remove support for all but `mpv`
- support robust reconnects via playlist looping
- set stream buffer to 4 seconds for fast start and quick recoveery
- target pipewire for audio, but allow bypassing the force-option
- fix channel parsing to find and use highest bitrate AAC codec
- channel information downloaded whenever it is needed, not written to disk
- no more Highlander Rules (there can be more than one)
- killall considered harmful
- change the default channel to be correct - Drone Zone
- sort the channel list
- mpv can provide all the information we require - use it
- use raw strings for SomaFM 1337 logos to avoid recent python bitching
- improve fuzzy channel matching robustness
- indicate current streaming server, and update when it changes
- handle audio output more flexibly, a gift for non-pipewire peeps
- detect when there is an audio output driver error, notify user, and break out of playlist loop
- make chromecast work - discovery and shutdown are proper, and AAC playback is supported
- simplify main loop, reduce CPU load even more

## January 5th, 2024
- Fix station ID matching
- Add Nerd Show to list of station IDs

## November 16th, 2023
- Add experimental track saving (press C during playback)

## November 10th, 2023
- Add random channel option (Thanks blutack)

### January 8th, 2022
- Release as v1.71

### December 11th, 2021
- Dynamically space channel name column when using -l

### November 26th, 2021
- Strip HTTPS from all playlist links
- Remove player/OS specific HTTPS fixes (now redundant)

### December 10th, 2020
- Fix unclean exit when channel not found

### December 5th, 2020
- Add ability to select Chromecast device from command line
- Use tempfile to find safe temporary directory on each OS
- Use HTTP link for MPlayer on Windows/Mac OS
- Use cls on Windows
- Update README
- Release as v1.7

### September 1st, 2020
- Make sure PID is deleted in fringe cases

### July 27th, 2020 (HOPE 2020 Release)
- Update README
- Update PyPi README
- Bump version to 1.61

### July 4th, 2020
- Add option to log played tracks to file
- Add PID file creation/detection

### July 1st, 2020
- Fix for MPlayer HTTPS links not working on Mac OS

### June 30th, 2020
- Starting script with -v will display backend player output for debug

### May 17th, 2020
- Update README
- Update PyPi README
- Release as v1.6

### May 7th, 2020
- Modular approach to supporting alternate players
- Experimental support for custom notification commands

### May 3rd, 2020
- Don't show desktop notifications for station IDs

### May 1st, 2020
- Fix notifications
- Initial support for mpv
- Add optional player name display
- Chromecast track sync now optional

### April 30th, 2020
- Initial support for mpg123
- Restructuring for PyPi upload

### December 3rd, 2019
- Fix for track titles with apostrophes

### August 8th, 2019 (DEF CON 27 Release)
- Update README
- Bump version to 1.5
- Fix for duplicate stream info display

### August 7th, 2019
- Modularize stream playback
- Highlight known Station IDs (optional)
- Get time elapsed for Chromecast stream
- Show track info for Chromecast steam in terminal

### August 6th, 2019
- Initial Chromecast support

### August 5th, 2019
- Fuzzy channel matching

### July 27th, 2019
- Add about screen with donation link

### June 26th, 2019
- Add cache purge option
- Improve channel matching

### June 23rd, 2019
- Release as v1.1

### June 20th, 2019
- Add CHANGELOG.md
- Add name/email to source file
- Display time elapsed when playback ended
- Add experimental desktop notifications with libnotify

### June 4th, 2019
- First Release, v1.0
