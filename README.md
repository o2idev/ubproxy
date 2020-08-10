# ubproxy

## topics

* [intro](#intro)
* [GUI options](#gui-options)
* [other features](#other-features)
* [download and install](#download-and-install)
* [desktop shortcut](#desktop-shortcut)
* [known issues](known-issues)
* [test current proxy setup](#test-current-proxy-setup)
  * [test setup](#test-setup)
  * [test directly: Terminal](#test-directly-terminal)
  * [test directly: Browser Firefox](#test-directly-browser-firefox)
  * [test directly: Java](#test-directly-java)
  * [test directly: Tomcat or other Java application servers](test-directly-tomcat-or-other-java-application-servers)
* [release history](#release-history)
  
## intro

If you are running some standard Ubuntu (e.g. with the Unity UI) then first have a look if configuring it via the [standard UI](https://www.serverlab.ca/tutorials/linux/administration-linux/how-to-configure-proxy-on-ubuntu-18-04/) already solves your problems.

(This version is an already heavily improved from the 2015 https://code.google.com/p/ubproxy/ version)

An inevitable tool to configure proxy-settings in universities and office environments.
Eliminates repetitive editing of system files prone to manual errors.

(Gnome)GUI for updating various default Ubuntu proxy aware "places" all included as plugins:

* standard application / places (Plugin):
	* `/etc/environment` standard ([PluginEtcEnv](plugins/PluginEtcEnv.py))
		* `http_proxy=http://myproxy:8080`, `HTTPS_PROXY=...`, ... (upper and lowercase)
	* Bash standard: `/etc/bash.bashrc` ([PluginBashRc](plugins/PluginBashRc.py))
		* similar to above but with `export ` prefix
	* Shell Env (currently running): e.g. invoked via `/bin/bash` or `CTRL+T` (Terminal) ([PluginEnvThis](plugins/PluginEnvThis.py))
	        * similar to bash above
	* Apt: `/etc/apt/apt.conf` ([PluginApt](plugins/PluginApt.py))
		* `Acquire::http::proxy "http://myproxy:8080"` ...
	* Gnome settings: `gsettings list-recursively org.gnome.system.proxy` ([PluginGsettings](plugins/PluginGsettings.py))
	* Java Runtime Environment (default): `/etc/alternatives/java` ([PluginJavaAlt](plugins/PluginJavaAlt.py))
		* it's `JAVA_HOME/lib/net.properties`, e.g. `java.net.useSystemProxies=...`, `http.proxyHost=...`, `https.proxyHost=...` properties
* individual tools (not making use of the above settings, at least in certain environments or versions)
	* Tomcat 8: `/etc/default/tomcat8` with `-Dhttp.proxyHost=myproxy -Dhttp.proxyPort=8080 ...` ([PluginTomcat8](plugins/PluginTomcat8.py))
	* Hale Studio: `<hale-studio>/workspace/.metadata/.../....prefs` ([PluginHale](plugins/PluginHale.py))
	* QGIS: `/home/user/.config/QGIS/QGIS2.conf` / `proxyHost=myproxy` ... ([PluginQgis](plugins/PluginQgis.py))
	* maybe your application by easily adding some new plugin

with this it covers all (4 first of the above) system places mentioned e.g. here:

* [AskUbuntu: How do I set system-wide proxy servers in Xubuntu, Lubuntu or Ubuntu Studio?](https://askubuntu.com/a/151047)

## GUI options

![Screenshot](2020-07-28%2Cscreenshot)

* `host`: for all HTTP, HTTPS, FTP connections
* `port`: for all the above
* `httpsProtocol`: default: `http` ; used for env var setup above ; maybe sometimes it must be `https`
* `REMOVE` button: to reset proxy (remove entries ; `gsettings` `mode` to `'none'` ; `java.net.useSystemProxies` to `false`)

## other features

* backups dir: `~/.ubproxy.backups`
* logfile: `/var/logs/ubproxy.log`
* outputting relevant setup (lines) of each plugin after setup or removal of the proxy settings to stdout and the log file
* many easily adjustable parameters on top of [ubproxy](blob/master/ubproxy) main file or some plugin files

## download and install

* download
	* latest final release version [v3.0.0 as zip or tar.gz](https://github.com/o2idev/ubproxy/releases/tag/ubproxy-v3.0.0)
	   * or [from here via git](https://github.com/o2idev/ubproxy): `git clone https://github.com/o2idev/ubproxy`
	* or latest development version as zip from [here](https://github.com/o2idev/ubproxy/archive/master.zip) to `/tmp`
* optional: move to `/opt` for availability after restarts (may be prefix `sudo ` if needed): `mv  /tmp/ubproxy*  /opt`

## desktop shortcut

create it similar to this (if moved to `/opt`): `ln -s  /opt/ubproxy  /home/user/Desktop/proxy-setup.sh`

## known issues

* some `dconf` related errors can be ignored (it seems related to calling `gsettings` with the `user` account instead of some sudo user):
lines look like this: `(process:3261): dconf-CRITICAL **: unable to create directory '/root/.cache/dconf': Keine Berechtigung.  dconf will not work properly.`

* by default all plugins are enabled although the may not be present or unique: this may lead to recoverable error messages
	* one can disable such plugins by simply renaming them using a `_` prefix, e.g. `plugins/_PluginJavaAlt`
* see also [issues](issues)

## test current proxy setup

### test setup

**hint:** if you change the proxy settings via **`ubproxy` (which is based on python)**, it will display the same data via stdout and in the logs **for all plugins**.
In a future version this could be available without touching the proxy settings and thus replacing/extending the functionality of the **`ubproxy-status.sh` (which is based on shell)** below.

to check in **all the 6 "standard" above "system places"** you can execute `sh /opt/ubproxy-status.sh` (or wherever you installed it)
the output could be similar to this:

```
$ /opt/ubproxy-status.sh 
++ echo -e '\n'


++ update-alternatives --query java
++ grep 'Value: '
++ sed 's/Value: \(.*\)\/bin\/java/\1\/lib\/net.properties/'
++ xargs cat
++ egrep -i prox
# For now, only the various proxy settings can be configured here.
# Whether or not the DefaultProxySelector will default to System Proxy
# specific proxy settings
# Note that the system properties that do explicitely set proxies
# (like http.proxyHost) do take precedence over the system settings
# even if java.net.useSystemProxies is set to true.
# Proxy configuration for the various protocol handlers.
# DO NOT uncomment these lines if you have set java.net.useSystemProxies
java.net.useSystemProxies=true
# HTTP Proxy settings. proxyHost is the name of the proxy server
# (e.g. proxy.mydomain.com), proxyPort is the port number to use (default
# value is 80) and nonProxyHosts is a '|' separated list of hostnames which
# should be accessed directly, ignoring the proxy server (default value is
# http.proxyHost=
http.nonProxyHosts=localhost|127.*|[::1]
# HTTPS Proxy Settings. proxyHost is the name of the proxy server
# (e.g. proxy.mydomain.com), proxyPort is the port number to use (default
# value is 443). The HTTPS protocol handlers uses the http nonProxyHosts list.
# https.proxyHost=
# FTP Proxy settings. proxyHost is the name of the proxy server
# (e.g. proxy.mydomain.com), proxyPort is the port number to use (default
# value is 80) and nonProxyHosts is a '|' separated list of hostnames which
# should be accessed directly, ignoring the proxy server (default value is
# ftp.proxyHost=
ftp.nonProxyHosts=localhost|127.*|[::1]
# Gopher Proxy settings. proxyHost is the name of the proxy server
# (e.g. proxy.mydomain.com), proxyPort is the port number to use (default
# gopher.proxyHost=
# gopher.proxyPort=80
# Socks proxy settings. socksProxyHost is the name of the proxy server
# (e.g. socks.domain.com), socksProxyPort is the port number to use
# socksProxyHost=
# socksProxyPort=1080
# when proxying HTTP or HTTPS.  For example, "Basic" results in effectively the
# schemes that will be disabled when tunneling HTTPS over a proxy, HTTP CONNECT.
# The 'jdk.http.auth.proxying.disabledSchemes' property lists the authentication
# schemes that will be disabled when proxying HTTP.
#jdk.http.auth.proxying.disabledSchemes=
++ echo -e '\n'


++ cat /etc/bash.bashrc
++ egrep -i prox
export http_proxy="http://myproxyhost:8080"
export ftp_proxy="ftp://myproxyhost:8080"
export https_proxy="http://myproxyhost:8080"
export HTTP_PROXY="http://myproxyhost:8080"
export FTP_PROXY="ftp://myproxyhost:8080"
export HTTPS_PROXY="http://myproxyhost:8080"
++ echo -e '\n'


++ cat /etc/environment
++ egrep -i prox
http_proxy="http://myproxyhost:8080"
ftp_proxy="ftp://myproxyhost:8080"
https_proxy="http://myproxyhost:8080"
HTTP_PROXY="http://myproxyhost:8080"
FTP_PROXY="ftp://myproxyhost:8080"
HTTPS_PROXY="http://myproxyhost:8080"
++ echo -e '\n'


++ egrep -i prox
++ cat /etc/apt/apt.conf
Acquire::http::proxy "http://myproxyhost:8080/";
Acquire::ftp::proxy "ftp://myproxyhost:8080/";
Acquire::https::proxy "http://myproxyhost:8080/";
++ echo -e '\n'


++ set
++ egrep -i prox
BASH_SOURCE=([0]="/opt/ubproxy-status.sh")
FTP_PROXY=ftp://myproxyhost:8080
HTTPS_PROXY=http://myproxyhost:8080
HTTP_PROXY=http://myproxyhost:8080
PWD=/opt/UrlProxyTester
ftp_proxy=ftp://myproxyhost:8080
http_proxy=http://myproxyhost:8080
https_proxy=http://myproxyhost:8080
++ echo -e '\n'


++ gsettings list-recursively org.gnome.system.proxy
org.gnome.system.proxy use-same-proxy true
org.gnome.system.proxy mode 'manual'
org.gnome.system.proxy autoconfig-url ''
org.gnome.system.proxy ignore-hosts ['localhost', '127.0.0.0/8', '::1']
org.gnome.system.proxy.ftp host 'myproxyhost'
org.gnome.system.proxy.ftp port 8080
org.gnome.system.proxy.socks host ''
org.gnome.system.proxy.socks port 0
org.gnome.system.proxy.http host 'myproxyhost'
org.gnome.system.proxy.http port 8080
org.gnome.system.proxy.http use-authentication false
org.gnome.system.proxy.http authentication-password ''
org.gnome.system.proxy.http authentication-user ''
org.gnome.system.proxy.http enabled true
org.gnome.system.proxy.https host 'myproxyhost'
org.gnome.system.proxy.https port 8080
++ echo -e '\n'
```

## test directly: Terminal

the output of `wget http://duckduckgo.com -O /tmp/wget-proxy-test.html` (likely in a new Terminal with `CTRL + ALT + T`) should be similar to this:

```
--2020-07-31 11:13:06--  http://duckduckgo.com/
Auflösen des Hostnamen »myproxyhost (myproxyhost)«... 172.11.11.11
Verbindungsaufbau zu myproxyhost (myproxyhost)|172.11.11.11|:8080... verbunden.
Proxy-Anforderung gesendet, warte auf Antwort... 301 Moved Permanently
Platz: https://duckduckgo.com/ [folge]
--2020-07-31 11:13:06--  https://duckduckgo.com/
Verbindungsaufbau zu myproxyhost (myproxyhost)|172.11.11.11|:8080... verbunden.
Proxy-Anforderung gesendet, warte auf Antwort... 200 OK
Länge: 5403 (5,3K) [text/html]
In »»/tmp/wget-proxy-test.html«« speichern.

/tmp/wget-proxy-test.html         100%[==========================================================>]   5,28K  --.-KB/s    in 0s      

2020-07-31 11:13:07 (929 MB/s) - »/tmp/wget-proxy-test.html« gespeichert [5403/5403]
```

### test directly: Browser Firefox

Opening `http://www.duckduckgo.com` should work. make sure it's not coming from the local browser cache => press [`CTRL + F5` or similiar](https://support.mozilla.org/de/questions/1073264) to ensure it

### test directly: Java

use `java ProxyTester <URL>`, e.g. `java ProxyTester http://www.duckduckgo.com` which should output something like this if the setup works:
```
supply HTTP or HTTPS url as param
header fields:{null=[HTTP/1.1 301 Moved Permanently], X-Cache=[MISS from lnx-proxy01], Server=[nginx], 
Connection=[keep-alive], Date=[Thu, 30 Jul 2020 06:46:22 GMT], Via=[1.1 proxy01 (squid/8.8.8)], 
Strict-Transport-Security=[max-age=31536000], Cache-Control=[max-age=31536000], 
X-Cache-Lookup=[MISS from proxy01:8080], Expires=[Fri, 30 Jul 2021 06:46:22 GMT], Content-Length=[162], 
Age=[94138], Location=[https://duckduckgo.com/], Content-Type=[text/html]}
``` 

### test directly: Tomcat or other Java application servers

put [proxy-test.war](blob/master/proxy-test.war) containing a very simple [servlet](blob/master/java-appsrv-proxy-test-war/src/UrlTestServlet.java) in your `<tomcat>/webapps` folder and test the proxy functionality e.g. like this `http://localhost:8080/proxy-test/test?url=https://duckduckgo.com`

## release history

### v3.0.0

* plugin concept added and existing functionality moved to plugins
* further plugins added: Tomcat8, Hale Studio, Qgis
* backup dir now `~/.ubproxy.backups` (before `.Ubuntu-Proxy`)
* logfile now `/var/logs/ubproxy.log` (before `/var/logs/proxychangerlogs`)
* many easily adjustable parameters on top of [ubproxy](blob/master/ubproxy) main file or some plugin files
* outputting relevant setup (lines) of each plugin after setup or removal of the proxy settings to stdout and the log file
* backup functionality fixed
* various refactorings and enhancements
* code prepared for non-GUI usage and cmd line param functionality (code separation)

### v2.0.0

* `gsettings` support added
* `httpsProtocol` GUI parameter
* default JAVA/JRE support added
* various fixes/refactorings

### v1.0.0

considering the google code from 2015 as v1.0.0
