from mycroft import MycroftSkill, intent_file_handler


class RelayControl(MycroftSkill):
    def __init__(self):
        MycroftSkill.__init__(self)

    @intent_file_handler('control.relay.intent')
    def handle_control_relay(self, message):
        self.speak_dialog('control.relay')


def create_skill():
    return RelayControl()

