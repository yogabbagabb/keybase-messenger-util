import sys

from keybase_util import put_usernames_from_team_in_file, send_message_from_file, get_user_names_from_file, \
    change_to_directory_of_current_file
from process_imp_sg.meeting_reminder import send_process_imp_reminder
from add_your_subgroup_report_backs.send_message import send_channel_reminders_for_agenda


if __name__ == "__main__":
    change_to_directory_of_current_file()

    if len(sys.argv) == 1:
        nrwg = set(get_user_names_from_file('./data/nationalMembers.txt'))
        send_message_from_file(nrwg, './data/meetingReminder.txt', 10, 10)
    elif len(sys.argv) == 2 and sys.argv[1] == 'process_imp':
        send_process_imp_reminder('./process_imp_sg/process_imp_reminder.txt')
    elif len(sys.argv) == 2 and sys.argv[1] == 'channel_reminder':
        send_channel_reminders_for_agenda()
