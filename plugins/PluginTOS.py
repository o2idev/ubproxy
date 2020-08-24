class PluginTOS(PluginFile):  ## Talend Open Studio

	#confPath = '/opt/TOS_DI-20180116_1512-V6.5.1/configuration/.settings/org.eclipse.ui.ide.prefs'
	confPath = subprocess.check_output(['/bin/bash', '-c', r'locate */TOS_DI*/configuration/.settings/org.eclipse.core.net.prefs']).strip()

	def name(self):  return 'tos'
	def path(self):  return self.confPath


	## eclipse.preferences.version=1
        ## org.eclipse.core.net.hasMigrated=true
	## nonProxiedHosts=xyz|localhost|127.0.0.1
	## proxiesEnabled=true
        ## proxyData/HTTP/hasAuth=false
        ## proxyData/HTTP/host=proxy-list
        ## proxyData/HTTP/port=8080
        ## proxyData/HTTPS/hasAuth=false
        ## proxyData/HTTPS/host=proxy-list
        ## proxyData/HTTPS/port=8080
        ## systemProxiesEnabled=false 

	def substLineRules(self):  # type(bool) 

		enable = self.appSetupProxyDetailsOn()

		mrPairs = [  ## ('\1' backreference should not be followed by a digit ...)
			[r'(\nproxiesEnabled)=([^\n]*)',  r'\1=%s' % ('true' if enable else 'false')],
			[r'(\nsystemProxiesEnabled)=([^\n]*)', r'\1=%s' % ('true' if self.appUseSystemProxiesOn() else 'false')],
		        [r'\s*proxyData\/HTTPS?\/.*=.*',  r''],  ## may not be present
			[r'\nnonProxiedHosts=[^\n]*', r'']       ## may not be present
			]

		return mrPairs

	def addLineForProtId(self, lines, protId):
		if protId != "ftp":
			lines.append('\nproxyData/%s/hasAuth=false' % (protId.upper()))
			lines.append('\nproxyData/%s/host=%s' % (protId.upper(), proxyCfg.srv))
			lines.append('\nproxyData/%s/port=%s' % (protId.upper(), proxyCfg.port))
		if protId == 'http':
			lines.append('\nnonProxiedHosts=%s' % re.sub( noProxyDefaultDelim, '|', proxyCfg.noProxy ))