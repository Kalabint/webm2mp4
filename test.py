#!/usr/bin/env python3

# https://github.com/MikeWent/webm2mp4
# https://t.me/webm2mp4bot


from bot.utils import ci_cd

if __name__ == "__bot__":
   # stuff only to run when not called via 'import' here
   bot()


text = "Test OK!"
bot.utils.ci_cd(text);

print ("Test Finnished!");
