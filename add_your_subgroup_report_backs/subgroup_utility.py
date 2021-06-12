import os


def send_report_back_reminder(file_name, format_str):
    msg = get_file_contents(file_name, format_str)
    os.system('/usr/local/bin/keybase chat send --channel process_imp_sg  xrus_structure ' + msg)
    os.system('/usr/local/bin/keybase chat send --channel liaison_sg  xrus_structure ' + msg)
    os.system('/usr/local/bin/keybase chat send --channel XRUS_transition  xrus_structure ' + msg)
    os.system('/usr/local/bin/keybase chat send --channel basic_structure_wg  xrus_structure ' + msg)
    os.system('/usr/local/bin/keybase chat send --channel chapterEngage_sg  xrus_structure ' + msg)
    os.system('/usr/local/bin/keybase chat send --channel equity_sg  xrus_structure ' + msg)
    os.system('/usr/local/bin/keybase chat send --channel regenerative_sg  xrus_structure ' + msg)
    os.system('/usr/local/bin/keybase chat send --channel conflict_resilience  xrus_structure ' + msg)


def send_agenda_reminder(file_name, format_str):
    msg = get_file_contents(file_name, format_str)
    os.system('/usr/local/bin/keybase chat send --channel ActionItems xrus_structure ' + msg)
    os.system('/usr/local/bin/keybase chat send --channel general  xrus_structure ' + msg)
    os.system('/usr/local/bin/keybase chat send --channel facilitators  xrus_structure ' + msg)


def get_file_contents(file_name, format_str=''):
    """
    :param format_str: A string to format the message by
    :param users: A list of users to send a message to
    :param file_name: A file to read the message from. It must be delimited by quotes (e.g. "Hi, I am bob")
    :return: None
    """
    file = open(file_name, "r")
    msg = file.read().format(format_str)
    return msg
