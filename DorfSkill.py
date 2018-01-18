from os.path import dirname

from adapt.intent import IntentBuilder
from mycroft.skills.core import MycroftSkill, intent_handler
from mycroft.util.log import getLogger

__author__ = 'me'
LOGGER = getLogger(__name__)


class DorfSkill(MycroftSkill):
    def initialize(self):
        self.load_data_files(dirname(__file__))

    @intent_handler(IntentBuilder("SufurIntent").require("hello_sufur"))
    def handle_rufus(self, message):
        self.speak_dialog("What")

    def stop(self):
        pass
