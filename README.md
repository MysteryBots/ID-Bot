# The ID Bot

> A star ⭐ from you means a lot to us!

<p align="center"><a href="https://www.github.com/MysteryBots/ID-Bot"><img src="https://telegra.ph/file/784c14c76533f944ae9b0.jpg" width="5000"></a></p>

Telegram bot to give id of any user, group,bot, channels and even stickers.

[![Open Source Love svg1](https://badges.frapsoft.com/os/v1/open-source.svg?v=103)](https://github.com/ellerbrock/open-source-badges/)

<details open="open">
  <summary> Table of Contents</summary>
  <ol>
    <li>
      <a href="#usage">Usage</a>
      <ul>
        <li><a href="#deploy-to-heroku">Deploy To Heroku</a></li>
        <li><a href="#local-deploying">Local Deploying</a></li>
      </ul>
    </li>
    <li>
      <a href="#environment-variables">Environment Variables</a>
      <ul>
        <li><a href="#mandatory-vars">Mandatory Vars</a></li>
        <li><a href="#optional-vars">Optional Vars</a></li>
      </ul>
    </li>
    <li><a href="#functions">Functions</a></li>
    <li><a href="#to-do">To-Do</a></li>
    <li><a href="#stats">Stats</a></li>
    <li><a href="#license">License</a></li>
    <li><a href="#contributing">Contributing</a></li>
    <li><a href="#credits">Credits</a></li>
    <li><a href="#support">Support</a></li>
  </ol>
</details>

## Usage

### Deploy to Heroku

[![Deploy](https://www.herokucdn.com/deploy/button.svg)](https://heroku.com/deploy?template=https://github.com/MysteryBots/ID-Bot)

1. Tap on above button and fill `API_ID`, `API_HASH`, `BOT_TOKEN`. Alternatively fill `OWNER_ID` and `OWNER_NAME`.
   Note : Fill both or leave both unless bot won't work.
   2)Turn on "Inline Mode" of your bot!
   3)Then tap "Deploy App" below it. Wait till deploying is complete (will take atmost 2 minutes).
2. After deploying is complete, tap on "Manage App"
3. Check the logs to see if your bot is ready!

### Local Deploying

1. Clone the repo
   ```markdown
   git clone https://github.com/MysteryBots/ID-Bot
   ```
2. Edit `Config.py` and Fill the needed variables by following [this](https://github.com/MysteryBots/ID-Bot/blob/master/Config.py#L11)

3. Turn on "Inline Mode" using settings in BotFather.

4. Enter the directory
   ```markdown
   cd ID-Bot
   ```
5. Run the file
   ```markdown
   python3 idbot.py
   ```

## Environment Variables

#### Mandatory Vars

- `API_ID` - Get this from [my.telegram.org](https://my.telegram.org/auth) or [@TgOrgBot](https://t.me/TgOrgBot)
- `API_HASH` - Get this from [my.telegram.org](https://my.telegram.org/auth) or [@TgOrgBot](https://t.me/TgOrgBot)
- `BOT_TOKEN` - Get this from [@BotFather](https://t.me/BotFather)

#### Optional Vars

> (fill both or neither)

- `OWNER_ID` - Get it from [@MissMiley_bot](https://t.me/MissMiley_bot) by sending /id to it.
- `OWNER_NAME` - Your Name (to be shown as owner in bot)

## Functions

> More features soon, this is an minimal example :)

1. Telegram bot to give id of any user, group,bot, channels.
2. Support for using in groups and channels
   3)Support for Inline Mode
3. Also support to het id by Forwarding any message to the bot from users, bots, channels and even anonymous admins.
4. Get id from usernames too.
5. Specify owner's account to get help or something.

## To-Do

1. Database for stats
2. Add more group features.
3. Add more inline features

## Stats

[![GitHub forks](https://img.shields.io/github/forks/MysteryBots/ID-Bot.svg?style=social&label=Fork&maxAge=2592000)](https://github.com/MysteryBots/ID-Bot/network/) [![GitHub stars](https://img.shields.io/github/stars/MysteryBots/ID-Bot.svg?style=social&label=Star&maxAge=2592000)](https://github.com/MysteryBots/ID-Bot/stargazers/) [![GitHub watchers](https://img.shields.io/github/watchers/MysteryBots/ID-Bot.js.svg?style=social&label=Watch&maxAge=2592000)](https://github.com/MysteryBots/ID-Bot/watchers/)
[![Maintenance](https://img.shields.io/badge/Maintained%3F-yes-green.svg)](https://github.com/MysteryBots/ID-Bot/graphs/commit-activity)

## License

[![License: AGPL v3](https://img.shields.io/badge/License-AGPL%20v3-blue.svg)](https://www.gnu.org/licenses/agpl-3.0)

## Contributing

[![GitHub contributors](https://img.shields.io/github/contributors/MysteryBots/ID-Bot.svg)](https://github.com/MysteryBots/ID-Bot/graphs/contributors/)

> Contributions are heartily accepted.

[![PRs Welcome](https://img.shields.io/badge/PRs-welcome-brightgreen.svg?style=flat-square)](http://makeapullrequest.com)

## Credits

- [Dan Tès](https://github.com/delivrance) for his [Pyrogram](https://docs.pyrogram.org) Library
- [@The_Firefrost](https://t.me/The_firefrost) for the idea.
- Inspired from My-ID-Bot and IDBot (not open source though)

## Support

Channel :- [@MysteryBots](https://t.me/MysteryBots)

Group Chat :- [@MysteryBotsChat](https://t.me/MysteryBotsChat)

## :)

[![forthebadge made-with-python](http://ForTheBadge.com/images/badges/made-with-python.svg)](https://www.python.org/)

[![ForTheBadge built-with-love](http://ForTheBadge.com/images/badges/built-with-love.svg)](https://github.com/MysteryBots)

[![ForTheBadge makes-people-smile](http://ForTheBadge.com/images/badges/makes-people-smile.svg)](https://github.com/MysteryBots)
