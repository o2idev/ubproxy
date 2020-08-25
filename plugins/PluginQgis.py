class PluginQgis(PluginFile):

	#confPath = '/home/user/.config/QGIS/QGIS2.conf'
	#confPath = subprocess.check_output(['/bin/bash', '-c', r'locate /home/*/.config/QGIS/QGIS2.conf | egrep -v "install"']).strip()
	#confPath = '/home/user/.local/share/QGIS/QGIS3/profiles/default/QGIS/QGIS3.ini'
	confPath = subprocess.check_output(['/bin/bash', '-c', r'locate /home/*/.local/share/QGIS/QGIS3/profiles/default/QGIS/QGIS3.ini | egrep -v "install"']).strip()

	def name(self):  return 'qgis'
	def path(self):  return self.confPath


	## ...
	## [Qgis]
	## ...
	## networkAndProxy\networkTimeout=60000
	## networkAndProxy\userAgent=Mozilla/5.0
	## ...
	## [QgsCollapsibleGroupBox]
	## ...
	## QgsOptionsBase\grpProxy\collapsed=false
	## ...
	## [proxy]
	## proxyEnabled=true
	## proxyHost=
	## proxyPort=
	## proxyUser=
	## proxyPassword=
	## proxyType=DefaultProxy
	## proxyExcludedUrls=
	## ...
	def substLineRules(self):  # type: (bool)

		## does not support sys proxy => enable manually if necessary:
		enable = self.appSetupProxyDetailsOn()

		mrPairs = [  ## ('\1' backreference should not be followed by a digit ...)
			[r'(\proxyEnabled)=([^\n]*)', r'\1=' + ('true' if enable else 'false')],
			[r'(\proxyExcludedUrls)=([^\n]*)', r'\1=' + (proxyCfg.noProxy if enable else '')],
			[r'(\proxyType)=([^\n]*)', r'\1=' + ('HttpProxy' if enable else '')]
		]

		mrPairs += [
			[r'(\nproxyHost)=([^\n]*)', r'\1=' + (proxyCfg.srv if enable else '')],
			[r'(\nproxyPort)=([^\n]*)', r'\1=' + (proxyCfg.port if enable else '')]
		]

		return mrPairs
