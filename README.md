**Warning:** If the keybase infrastructure detects that you're sending a high volume of messages within a single time frame, it will mark you as a spammer and prevent you from being able to initiate new conversations or converse with new people (i.e. those you haven't already chatted with in the past). To bypass their spam detection, [keybase_util.py](keybase_util.py) allows you to send messages with an intervening sleep time (the code sleeps for a parametrized random quantity of time before sending subsequent messages). I would recommend you send all your messages from a dummy account, where the dummy account has been added to a team of interest.

# TLDR

The heart of this project is [keybase_util.py](./keybase_util.py). This file provides methods which can be used to send messages to multiple people, multiple channels or to determine all the members in a team.



- [process_imp_sg/meeting_reminder.py](process_imp_sg/meeting_reminder.py) shows how to send a message stored in a file to a channel.
- [add_your_subgroup_report_backs/send_message.py](add_your_subgroup_report_backs/send_message.py) shows how to send a message stored in a file to all members of a team.

- [get_members.py](get_members.py) shows how to store the members of any team you're part of into a file. You can then read from that file to send messages to all members using some methods in [keybase_util.py](keybase_util.py)

Please note that I have not included the data files that contain the usernames of various people. To protect their identities.



# Pre-requisites

Have downloaded the Keybase Command Line Interface; have downloaded the tool to the file path `/usr/local/bin/keybase` (or else, modify [keybase_util.py](./keybase_util.py) to use whatever path you fancy).