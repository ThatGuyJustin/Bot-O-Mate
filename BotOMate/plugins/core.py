from disco.bot import Plugin
from disco.api.http import APIException
from disco.bot.command import CommandEvent

class CorePlugin(Plugin):
    def load(self, ctx):

        self.developers = [104376018222972928, 193849229884522496]

        super(CorePlugin, self).load(ctx)


    @Plugin.listen('MessageCreate')
    def on_command_msg(self, event):
        """
        Written by Nadie#0063 as a basic command handler for Disco instead of using the build in one.
        """
        if event.message.author.bot:
            return
        if not event.guild:
            return

        if self.author.id not in self.developers:
            return

        commands = self.bot.get_commands_for_message(False, {}, '!', event.message)
        if not commands:
            return
        for command, match in commands:
            return command.plugin.execute(CommandEvent(command, event, match))


    @Plugin.listen('Ready')
    def on_ready(self, event):
        self.log.info(f"VALC IS DUMB! I logged in as {self.client.state.me}. Watch out meesux.")
    

    @Plugin.command('ping')
    def ping_cmd(self, event):

        member = event.member

        try:
            member.ban(reason="Valc said so")
        except APIException as e:
            if e.code == 50013:
                event.reply("I can't ban you :(")

