from mycroft import MycroftSkill, intent_file_handler


class Sabarinathan(MycroftSkill):
    def __init__(self):
        MycroftSkill.__init__(self)

    @intent_file_handler('sabarinathan.intent')
    def handle_sabarinathan(self, message):
        self.speak_dialog('sabarinathan')


def create_skill():
    return Sabarinathan()

