class PluginEtcEnv(PluginFile):
	def name(self): return "etc-env"
	def path(self): return "/etc/environment"
	def substLineRules(self): return [[r'\n?(\s*(https?|ftp)_proxy\s*=\s*".*")', r'']]  # type(bool)

	def addLineForProtId(self,  lines,  protId):
		lines.append( self.envShLineGenFunc(  False,  protId,  False ) + "\n")
		lines.append( self.envShLineGenFunc(  True,  protId,  False ) + "\n")
