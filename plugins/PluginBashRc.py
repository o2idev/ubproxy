class PluginBashRc(PluginFile):
	def name(self): return "bashrc"
	def path(self): return "/etc/bash.bashrc"
	def substLineRules(self): return [[r'\n?(\s*export\s+(https?|ftp)_proxy\s*=\s*".*")', r'']]  # type(bool)

	def addLineForProtId(self, lines, protId):
		lines.append( self.envShLineGenFunc(  False,  protId,  True ) + "\n")
		lines.append( self.envShLineGenFunc(  True,  protId,  True ) + "\n")
