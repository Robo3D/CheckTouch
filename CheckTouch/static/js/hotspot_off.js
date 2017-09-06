/*
 * View model for hotspot_off
 *
 * Author: victor
 * License: AGPLv3
 */
$(function() {
    function Hotspot_offViewModel(parameters) {
        var self = this;

        // assign the injected parameters, e.g.:
        // self.loginStateViewModel = parameters[0];
        // self.settingsViewModel = parameters[1];

        // TODO: Implement your plugin's view model here.
    }

    // view model class, parameters for constructor, container to bind to
    OCTOPRINT_VIEWMODELS.push([
        Hotspot_offViewModel,

        // e.g. loginStateViewModel, settingsViewModel, ...
        [ /* "loginStateViewModel", "settingsViewModel" */ ],

        // e.g. #settings_plugin_hotspot_off, #tab_plugin_hotspot_off, ...
        [ /* ... */ ]
    ]);
});
