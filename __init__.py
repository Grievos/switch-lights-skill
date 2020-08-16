from mycroft import MycroftSkill, intent_file_handler


class SwitchLights(MycroftSkill):
    def __init__(self):
        MycroftSkill.__init__(self)

    @intent_file_handler('lights.switch.intent')
    def handle_lights_switch(self, message):
        self.speak_dialog('lights.switch')


def create_skill():
    return SwitchLights()

