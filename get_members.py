import os
import sys

from keybase_util import put_usernames_from_team_in_file, send_message_from_file, get_user_names_from_file, \
    change_to_directory_of_current_file
from process_imp_sg.meeting_reminder import send_process_imp_reminder
from add_your_subgroup_report_backs.send_message import send_channel_reminders_for_agenda



if __name__ == "__main__":
    change_to_directory_of_current_file()
    put_usernames_from_team_in_file('xrus_structure', 'nationalMembers.txt', 'data')

