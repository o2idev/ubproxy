## ubproxy

Ongoing development of the unmaintained https://code.google.com/p/ubproxy/

An inevitable tool to configure proxy-settings in universities and office environment.
Eliminates repetitive editing of system files prone to manual errors.

(Gnome)GUI for updating various default Ubuntu proxy aware "places":

* `/etc/environment`
* `/etc/bash.bashrc`
* `/etc/apt/apt.conf`
* `gsettings list-recursively org.gnome.system.proxy`

with this it covers all the system places mentioned e.g. here:

* [AskUbuntu: How do I set system-wide proxy servers in Xubuntu, Lubuntu or Ubuntu Studio?](https://askubuntu.com/a/151047)

# GUI options

![Screenshot](https://github.com/o2idev/ubproxy/blob/master/2020-07-28%2Cscreenshot)

* `host`: for all HTTP, HTTPS, FTP connections
* `port`: for all the above
* `httpsProtocol`: default: `http` ; used for env var setup above ; maybe sometimes it must be `https`

# download and install

* download as zip from [here](https://github.com/o2idev/ubproxy/archive/master.zip) to `/tmp`
* optional: move to `/opt` for availability after restarts (may be prefix `sudo ` if needed): `mv  /tmp/ubproxy*  /opt`

# test current proxy setup

to check in all the above "system places" you can execute `sh /opt/ubproxy-status.sh` (or wherever you installed it)

# desktop shortcut

create it similar to this (if moved to `/opt`): `ln -s  /opt/ubproxy  /home/user/Desktop/proxy-setup.sh`
