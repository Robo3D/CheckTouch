# coding=utf-8
from __future__ import absolute_import
import octoprint.plugin
import subprocess

class CheckTouch(octoprint.plugin.SettingsPlugin, octoprint.plugin.AssetPlugin, octoprint.plugin.TemplatePlugin, octoprint.plugin.StartupPlugin):

    def on_startup(self, host, port):
        run = ['sudo', 'evtest', '/dev/input/event0']
        subprocess.call(run, shell=True)

    def get_update_information(self):
        return dict(
                hotspot_off=dict(
                displayName="CheckTouch Plugin",
                displayVersion=self._plugin_version,
                type="github_release",
                user="Robo3D",
                repo="CheckTouch",
                current=self._plugin_version,
                pip="https://github.com/Robo3D/CheckTouch/archive/{target_version}.zip"
            )
        )


__plugin_name__ = "CheckTouch Plugin"

def __plugin_load__():
    global __plugin_implementation__
    __plugin_implementation__ = CheckTouch()

    global __plugin_hooks__
    __plugin_hooks__ = {
        "octoprint.plugin.softwareupdate.check_config": __plugin_implementation__.get_update_information
    }
