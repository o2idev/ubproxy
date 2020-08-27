class PluginBashRc(PluginFile):
	def name(self): return "bashrc"
	def path(self): return "/etc/bash.bashrc"
	def substLineRules(self): return [[r'\n?\s*export\s+(https?|ftp|no)_proxy\s*=\s*[^\n]*', r'']]  # type(bool)

	def addLineForProtId(self, lines, protId):
		lines.append( self.envShLineGenFunc(  False,  protId,  True ) + "\n")
		lines.append( self.envShLineGenFunc(  True,  protId,  True ) + "\n")
		if protId == 'http':
			for vname in ('no_proxy', 'NO_PROXY'):
				lines.append( 'export %s="%s"\n' % (vname, proxyCfg.noProxy))
