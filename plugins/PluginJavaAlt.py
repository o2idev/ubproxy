class PluginJavaAlt(PluginFile):
	
	def name(self): return "java-alt"
	def supportsSystemProxiesUsage(self): # type: () => bool
		return True  ## recommended
		#return False  ## alternative if <True> not working for your software

	## JAVA_HOME/lib/net.properties where JAVA_HOME is determined from /etc/alternatives/java
	def path(self): return subprocess.check_output(['/bin/bash', '-c', r"update-alternatives --query java | grep 'Value: ' | sed 's/Value: \(.*\)\/bin\/java/\1\/lib\/net.properties/'"]).strip()


	def substLineRules(self):  # type(bool)
		rules = [[r'(\n?\s*java.net.useSystemProxies\s*=\s*)(true|false)(.*)',  
			r'\1true\3' if self.appUseSystemProxiesOn() else r'\1false\3']]
		if self.appCleanProxyDetailsOn():
			rules.append([r'\n?(\s*(https?|ftp)\.(proxy(Host|Port)|nonProxyHosts)\s*=.+)',  r''])  ## => remove old http.proxyHost etc. entries
		return rules


	def addLineForProtId(self, lines, protId):

		## e.g. appending
		##   https.proxyHost=myhost
		##   https.proxyPort=8080
		##   java.net.useSystemProxies=true
		if self.appSetupProxyDetailsOn():
		    lines.append('%s.proxyHost=%s\n' % (protId, proxyCfg.srv))
		    lines.append('%s.proxyPort=%s\n' % (protId, proxyCfg.port))
		    lines.append('%s.nonProxyHosts=%s\n' % (protId,  proxyCfg.noProxyAsDelimStr('|') ))
		    #if protId == 'http':
		    	#lines.append('java.net.useSystemProxies=true\n')  ## done in substLineRules() above
