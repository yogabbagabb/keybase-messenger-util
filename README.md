# Keybase CLI Wrapper


## Description

Keybase is a messaging application. It exposes a CLI that allows one to programatically send messages to users, among other things. Keybase Groups can contain thousands of users. It is useful to have the ability to send a message not to the group en masse but to each user within the group. This repository exposes a module through [keybase_util.py](keybase_util.py), for doing so.

**Warning:** If the keybase infrastructure detects that you're sending a high volume of messages within a single time frame, it will mark you as a spammer and prevent you from being able to initiate new conversations or converse with new people (i.e. those you haven't already chatted with in the past). To bypass their spam detection, [keybase_util.py](keybase_util.py) allows you to send messages with an intervening sleep time (the code sleeps for a parametrized random quantity of time before sending subsequent messages). I would recommend you send all your messages from a dummy account, where the dummy account has been added to a team of interest.

## Usage

### Pre-requisites

Have downloaded the Keybase Command Line Interface; have downloaded the tool to the file path `/usr/local/bin/keybase` (or else, modify [keybase_util.py](./keybase_util.py) to use whatever path you fancy).

The API lives in [keybase_util.py](./keybase_util.py). This file provides methods which can be used to send messages to multiple people, multiple channels or to determine all the members in a team.


Some examples are contained in the repo:

- [process_imp_sg/meeting_reminder.py](process_imp_sg/meeting_reminder.py) shows how to send a message stored in a file to a channel.
- [add_your_subgroup_report_backs/send_message.py](add_your_subgroup_report_backs/send_message.py) shows how to send a message stored in a file to all members of a team.
- [get_members.py](get_members.py) shows how to store the members of any team you're part of into a file. You can then read from that file to send messages to all members using some methods in [keybase_util.py](keybase_util.py)

Please note that, for data privacy reasons, I have not included the data files that contain the usernames of various people. These data files were obtained using [get_members.py](get_members.py) -- I then used these files in [keybase_util.py](./keybase_util.py) to send out messages.


## License

The MIT License (MIT)

Copyright © 2022

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the “Software”), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED “AS IS”, WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.


## Contributing

- Tests need to be written for [keybase_util.py](./keybase_util.py)