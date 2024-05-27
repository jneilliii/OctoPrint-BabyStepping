/*
 * View model for OctoPrint-BabyStepping
 *
 * Author: jneilliii
 * License: AGPLv3
 */
$(function() {
	function babysteppingViewModel(parameters) {
		var self = this;

		self.settingsViewModel = parameters[0];
		self.controlViewModel = parameters[1];

        self.distance = ko.observable();

        self.onBeforeBinding = function() {
            self.distance(self.settingsViewModel.settings.plugins.babystepping.distance());
        };

        self.onEventSettingsUpdated  = function() {
            self.distance(self.settingsViewModel.settings.plugins.babystepping.distance());
        };

		self.getAdditionalControls = function() {
            return [
                {
                    name: "Baby Stepping", type: "section", layout: "horizontal", children: [
                        {
                            type: "javascript",
                            javascript: "OctoPrint.control.sendGcode('M290 Z' + self.settings.settings.plugins.babystepping.distance());",
                            name: "Up"
                        },
                        {
                            type: "javascript",
                            javascript: "OctoPrint.control.sendGcode('M290 Z-' + self.settings.settings.plugins.babystepping.distance());",
                            name: "Down"
                        }
                    ]
                }
            ];
		};
	}

	OCTOPRINT_VIEWMODELS.push({
		construct: babysteppingViewModel,
		dependencies: [ "settingsViewModel", "controlViewModel" ],
		elements: [ "settings_plugin_babystepping_form" ]
	});
});
