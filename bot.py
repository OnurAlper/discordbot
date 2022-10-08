from os import getenv

import dotenv

import f_commands

dotenv.load_dotenv(".env")


if __name__ == "__main__":
    f_commands.time_module.start()
    f_commands.check_standup.start()
    f_commands.bcr_check_standup.start()
    f_commands.bcr_time_module.start()
    f_commands.client.run(getenv("DISCORD_TOKEN", "stand_up"))
    f_commands.client.run(getenv("DISCORD_TOKEN", "bcr_standup"))
    #f_commands.bot.run(getenv("DISCORD_TOKEN", "hiddenslate_chn"))
    # f_commands.time_module_zamancizelge.start()
