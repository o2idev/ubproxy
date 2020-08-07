## does not work for some parent process though: https://stackoverflow.com/a/38982939
class PluginEnvThis(Plugin):
	def name(self): return "env-this"

	def apply(self):  # type(bool)
		for upperOn in [False, True]:
			for pid, pfx in proxyCfg.protIdPrefixMap.items():
				envVar = '%s_proxy' % pid
				if upperOn:  envVar = envVar.upper()
				if enableProxyPhaseOn:
					os.environ[ envVar ] = proxyCfg.authSrvPortSuffix(True)
				else:
					if envVar in os.environ: del os.environ[ envVar ]


	def setupShow(self):
		for k in os.environ:
			if re.match( '.*proxy.*', k, re.I ):
				s = '%s = %s' % (k, os.environ[ k ])
				self.log(s)
				print s
		