class PluginGsettings(Plugin):

	osUser = 'user'
	resetMode = 'none'
	

	def name(self):  return "gsettings"

	def load(self):
		self.execLastOn = True


	def apply(self):  # type(bool)
		pc = proxyCfg  ## shortcut

		#prepare()

		uid = getpwnam( self.osUser )[2]
		os.setgid( uid )
		os.setuid( uid )
		#def setuidfunc():
		#    os.setgid(uid)
		#    os.setuid(uid)
		#os.system("gsettings set org.gnome.system.proxy.http enabled false")
		#subprocess.check_output('/bin/bash -c "gsettings set org.gnome.system.proxy mode \'auto\'"', preexec_fn=setuidfunc)

		enable = enableProxyPhaseOn
		os.system("gsettings set org.gnome.system.proxy mode '%s'" % ('manual' if enable else self.resetMode))

		if not enable and not self.appCleanProxyDetailsOn():  ## if no cleanups wanted: skip doing it below
			return


		os.system("gsettings set org.gnome.system.proxy.http enabled %s" % ('true' if enable else 'false'))
		#subprocess.check_output('/bin/bash -c "gsettings set org.gnome.system.proxy mode \'auto\'"', preexec_fn=setuidfunc)
		os.system("gsettings set org.gnome.system.proxy.http host '%s'" % (pc.srv if enable else ''))
		os.system("gsettings set org.gnome.system.proxy.http port '%s'" % (pc.port if enable else '0'))
		os.system("gsettings set org.gnome.system.proxy.ftp host '%s'" % (pc.srv if enable else ''))
		os.system("gsettings set org.gnome.system.proxy.ftp port '%s'" % (pc.port if enable else '0'))
		## this seems not possible to apply ("https" protocol for HTTPS):
		#if pc.protIdPrefixMap['https'] == "https":

		os.system("gsettings set org.gnome.system.proxy.https host '%s'" % (pc.srv if enable else ''))
		os.system("gsettings set org.gnome.system.proxy.https port '%s'" % (pc.port if enable else '0'))
		if pc.usrname != "":
		    os.system("gsettings set org.gnome.system.proxy.http authentication-user '%s'" % (pc.usrname if enable else ''))
		    os.system("gsettings set org.gnome.system.proxy.http authentication-password '%s'" % (pc.usrpass if enable else ''))
		else:
		    os.system("gsettings set org.gnome.system.proxy.http use-authentication false")


	def setupShow(self):
                
		l = subprocess.check_output(['gsettings','list-recursively','org.gnome.system.proxy']).strip()
		self.log(l)
		print l


	## TODO: may be this unfinished stuff can help to solve problems with gsettings setup
	## https://askubuntu.com/a/484752
	def prepare():
	    #pid = subprocess.check_output(["pgrep", "gnome-session"]).decode("utf-8").strip(A)
	    pid = subprocess.check_output(["pgrep", "xfce4-session"]).decode("utf-8").strip()
	    #cmd = "grep -z DBUS_SESSION_BUS_ADDRESS /proc/"+pid+"/environ|cut -d= -f2-"
	    cmd = "grep -z DBUS_SESSION_BUS_ADDRESS /proc/"+pid+"/environ  |  cut -d= -f2-  |  sed -r 's/(.+)/DBUS_SESSION_BUS_ADDRESS=\\\\1/'"
	    #print ("PATH: < %s >" % (os.environ["PATH"]))
	    #print ("DBUS_SESSION_BUS_ADDRESS: < %s >" % (os.environ["DBUS_SESSION_BUS_ADDRESS"]))
	    os.environ["DBUS_SESSION_BUS_ADDRESS"] = subprocess.check_output(['/bin/bash', '-c', cmd]).decode("utf-8").strip().replace("\0", "")
	    #os.environ["DBUS_SESSION_BUS_ADDRESS"] = 'unix:abstract=/tmp/dbus-3LpGWPt0WX,guid=c17a8bf032ed6179687fa8265f215de7' 
