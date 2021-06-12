import keybase_util
from add_your_subgroup_report_backs.subgroup_utility import send_report_back_reminder, get_file_contents, \
    send_agenda_reminder


def send_channel_reminders_for_agenda():
    keybase_util.change_to_directory_of_current_file(__file__)
    agenda_link = get_file_contents('agenda_link.txt')
    send_report_back_reminder('message.txt', agenda_link)


def send_agenda_reminder_fac():
    keybase_util.change_to_directory_of_current_file(__file__)
    send_agenda_reminder('messageTwo.txt', "")


def send_reminder_to_subgroup_and_standard_channels():
    keybase_util.change_to_directory_of_current_file(__file__)
    send_report_back_reminder('messageTwo.txt', "")
    send_agenda_reminder('messageTwo.txt', "")


if __name__ == "__main__":
    num = 2
    if num == 1:
        send_channel_reminders_for_agenda()
    elif num == 2:
        send_agenda_reminder_fac()
    elif num == 3:
        send_reminder_to_subgroup_and_standard_channels()
