class PluginApt(PluginFile):
	def name(self): return "apt-conf"
	def path(self): return "/etc/apt/apt.conf"

	def substLineRules(self): return [[r'\n?\s*Acquire::.+::proxy[^\n;]*;', r'']]  # type(bool) -> str

	def addLineForProtId(self, lines, protId):
		lines.append('Acquire::%s::proxy "%s://%s/";\n' % (protId, proxyCfg.protIdPrefixMap[protId], proxyCfg.authSrvPortSuffix(True)))
		if protId == 'http':
			for np in proxyCfg.noProxyAsList():
				lines.append('Acquire::http::proxy::%s DIRECT;\n' % np)