import json
import os
import time
import random


def send_message_from_file(users, file_name, sleep=0, random_time=0):
    """
    :param random_time: A randomized time that gets added to the sleep time, where the randomized_time ranges in [0, random_time]
    :param sleep: Between every message, a time to sleep for

    Altogether, the time between every message being sent is
    [sleep, sleep + random_time * R]

    Where R is a random whole number uniformly chosen between 0 and 1.

    :param users: A list of users to send a message to
    :param file_name: A file to read the message from. It must be delimited by quotes (e.g. "Hi, I am bob"). Moreover, any quotes inside the outermost quotes must be escaped.

    :return: None
    """
    file = open(file_name, "r")
    msg = file.read()
    for sus in users:
        time.sleep(sleep + random.random() * random_time)
        os.system('/usr/local/bin/keybase chat send ' + sus + ' ' + msg)


def send_message(users, message):
    """
    :param users: A list of users to send a message to
    :param message: The message to send
    :return: None
    """
    for sus in users:
        os.system('keybase chat send ' + sus + ' ' + message)


def remove_some_peeps(users_to_remove, removal_message, team_name):
    """
    Remove people form a team
    :param team_name: The team to remove a user from
    :param users_to_remove: The list of users to remove
    :param removal_message: A message to send to the user before removing them.
    :return: None
    """
    for sus in users_to_remove:
        os.system('keybase chat send ' + sus + ' ' + removal_message)
        os.system('keybase team remove-member ' + team_name + ' -f -u' + ' ' + sus)


def put_usernames_from_team_in_file(team_name, file_name, file_dir):
    """
    Get the usernames of all people in a team
    :param team_name: The name of the team
    :param file_name: A file that will be overwritten with json data from the team.
    :param file_dir: The directory of the file.
    :return: An array of usernames
    """
    the_str = 'keybase team list-members -j ' + team_name + ' > ' + file_dir + '/' + file_name
    print(the_str)
    os.system('keybase team list-members -j ' + team_name + ' > ' + file_dir + '/' + file_name)
    # read file
    return get_user_names_from_file(file_dir + '/' + file_name)


def get_user_names_from_file(file_name):
    """
    Get the usernames of all people in a team
    :param file_name: A file obtained from get_usernames
    :return: An array of usernames
    """
    with open(file_name, 'r') as myfile:
        data = myfile.read()
    # parse file
    obj = json.loads(data)
    # show values
    array_of_priv = [
        obj['members'][z] for z in ['readers', 'writers', 'admins', 'owners'] if obj['members'][z]]
    print(array_of_priv)
    usernames = [user_dict['username'] for priv_group in array_of_priv for user_dict in priv_group]
    return usernames


def change_to_directory_of_current_file(file_path=__file__):
    """
    Change to the directory of a file_path. Useful to use when you
    need to identify files, relative to a certain path. Identifying
    those files may be useful to either write or read from the file


    In a sense, this is the analog of the cd command
    on the bash shell or any derivative on it.

    :param file_path: The path to wherever you wish to
    :return:
    """
    abspath = os.path.abspath(file_path)
    dname = os.path.dirname(abspath)
    print(dname)
    os.chdir(dname)