import os


def send_process_imp_reminder(file_name):
    """
    :param users: A list of users to send a message to
    :param file_name: A file to read the message from. It must be delimited by quotes (e.g. "Hi, I am bob")
    :return: None
    """
    file = open(file_name, "r")
    msg = file.read()
    os.system('/usr/local/bin/keybase chat send --channel process_imp_sg  xrus_structure ' + msg)
