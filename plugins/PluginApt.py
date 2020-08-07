class PluginApt(PluginFile):
	def name(self): return "apt-conf"
	def path(self): return "/etc/apt/apt.conf"
	def substLineRules(self): return [[r'\n?(\s*Acquire::.+::proxy\s+"[^"]*"\s*;)', r'']]  # type(bool) -> str

	def addLineForProtId(self, lines, protId):
		lines.append('Acquire::%s::proxy "%s://%s/";\n' % (protId, proxyCfg.protIdPrefixMap[protId], proxyCfg.authSrvPortSuffix(True)))