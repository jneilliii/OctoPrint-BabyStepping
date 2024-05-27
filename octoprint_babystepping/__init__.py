# coding=utf-8
from __future__ import absolute_import

import octoprint.plugin

class babysteppingPlugin(octoprint.plugin.SettingsPlugin,
						octoprint.plugin.AssetPlugin,
						octoprint.plugin.TemplatePlugin):

	##~~ SettingsPlugin mixin

	def get_settings_defaults(self):
		return {'distance': 0.1}

	##~~ AssetPlugin mixin

	def get_assets(self):
		return {'js': ["js/babystepping.js"]}

	##-- TemplatePlugin mixin

	def get_template_configs(self):
		return [{'type': "settings", 'custom_bindings': False}, {'type': "controls", 'custom_bindings': False}]

	##~~ Softwareupdate hook

	def get_update_information(self):
		return {'babystepping': {'displayName': "Baby Stepping", 'displayVersion': self._plugin_version,
								 'type': "github_release", 'user': "jneilliii", 'repo': "OctoPrint-BabyStepping",
								 'current': self._plugin_version,
								 'pip': "https://github.com/jneilliii/OctoPrint-BabyStepping/archive/{target_version}.zip"}}

__plugin_name__ = "Baby Stepping"
__plugin_pythoncompat__ = ">=2.7,<4"

def __plugin_load__():
	global __plugin_implementation__
	__plugin_implementation__ = babysteppingPlugin()

	global __plugin_hooks__
	__plugin_hooks__ = {
		"octoprint.plugin.softwareupdate.check_config": __plugin_implementation__.get_update_information
	}

