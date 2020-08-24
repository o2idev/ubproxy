class PluginTomcat8(PluginFile):

	def name(self): return "tomcat8"
	def path(self): return '/etc/default/tomcat8'


	## must be one-liner statements
	def substLineRules(self):  # type(bool)
		return [[r'\n\s*[^#].+-D(https?|ftp).proxyHost=.*',  r'']]


	## JAVA_OPTS="${JAVA_OPTS} -Dhttp.proxyHost=myproxy -Dhttp.proxyPort=8080 -Dhttp.nonProxyHosts=\"localhost|127.0.0.1\""
	## JAVA_OPTS="${JAVA_OPTS} -Dhttps.proxyHost=myproxy -Dhttps.proxyPort=8080 -Dhttps.nonProxyHosts=\"localhost|127.0.0.1\""
	def addLineForProtId(self, lines, protId):

		lines.append('\nJAVA_OPTS="${JAVA_OPTS} -D%s.proxyHost=%s -D%s.proxyPort=%s -D%s.nonProxyHosts=\\"%s\\""' % (protId,  proxyCfg.srv,  protId,  proxyCfg.port,  protId,  re.sub( noProxyDefaultDelim, '|', proxyCfg.noProxy )))
