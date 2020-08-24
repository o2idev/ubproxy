class PluginEtcEnv(PluginFile):
	def name(self): return "etc-env"
	def path(self): return "/etc/environment"

	def substLineRules(self): return [[r'\n?\s*(https?|ftp|no)_proxy\s*=[^\n]*', r'']]  # type(bool)

	def addLineForProtId(self,  lines,  protId):
		lines.append( self.envShLineGenFunc(  False,  protId,  False ) + "\n")
		lines.append( self.envShLineGenFunc(  True,  protId,  False ) + "\n")
		if protId == 'http':
			for vname in ('no_proxy', 'NO_PROXY'):
				lines.append( '%s="%s"\n' % (vname, proxyCfg.noProxy))