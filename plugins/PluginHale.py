class PluginHale(PluginFile):

	## better use abstract symbolic links for specific versions so you do not have to update 
	## all locations but only the link
	#workspace = '/opt/hale-studio-3.3.2-linux.gtk.x86_64/workspace'
	#workspace = '/home/user/hale-studio~/workspace'
	workspace = subprocess.check_output(['/bin/bash', '-c', 'locate hale-studio | grep workspace$']).strip()

	def name(self):  return 'hale-studio'

	## e.g. <workspace>/.metadata/.plugins/org.eclipse.core.runtime/.settings/eu.esdihumboldt.hale.ui.util.prefs
	def path(self): return '%s/.metadata/.plugins/org.eclipse.core.runtime/.settings/eu.esdihumboldt.hale.ui.util.prefs' % self.workspace

	## http.nonProxyHosts=localhost, 127.0.0.1
	## http.proxyHost=myproxy
	## http.proxyPort=8080
	def substLineRules(self):  # type: (bool)
		return [  ## ('\1' backreference should not be followed by a digit ...)
			[r'(\nhttp.proxyHost)=([^\n]*)', r'\1=' + (proxyCfg.srv  if enableProxyPhaseOn else '=')],
			[r'(\nhttp.proxyPort)=([^\n]*)', r'\1=' + (proxyCfg.port if enableProxyPhaseOn else '=')]
		]
