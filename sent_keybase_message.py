import os
import json


def send_message(peeps_to_keep, keep_message):
    for sus in peeps_to_keep:
        os.system('keybase chat send ' + sus + ' ' + keep_message)


def remove_some_peeps(peeps_to_remove, removal_message):
    for sus in peeps_to_remove:
        os.system('keybase chat send ' + sus + ' ' + removal_message)
        os.system('keybase team remove-member xrsf -f -u' + ' ' + sus)


def get_usernames(team_name, file_name, curr_work_dir):
    the_str = 'keybase team list-members -j ' + team_name + ' > ' + curr_work_dir + '/' + file_name
    print(the_str)
    os.system('keybase team list-members -j ' + team_name + ' > ' + curr_work_dir + '/' + file_name)
    # read file
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


def execute_national_message():
    curr_work_dir = os.getcwd()
    team_name = 'some_team'
    file_name = 'nationalMembers.txt'
    usernames = get_usernames(team_name, file_name, curr_work_dir)
    for sus in usernames:
        os.system('keybase chat send ' + sus + ' ' + msg.format(sus))


def execute_regional_message():
    msg = "\"Greetings Comrade {}!\n\n This is an automated message. It is time that XR West re-organize -- to " \
          "support each other and support a line 3 resistance proposal that requires regional organization! (see this " \
          "proposal https://docs.google.com/document/d/1xHKRv6osPxzXja-Xsvl6N-d7ONqXXrIgLBbyh5q4quc/edit)." \
          "\n\n Can you identify 1-2 reps from your chapter and ask them to fill out this poll (" \
          "https://www.when2meet.com/?10552789-rTNiv) assuming PDT times. My goal is to identify a time when we could " \
          "meet for 2 hours (I think once every month).\" "
    clarifying_msg = "\"Hi (another automated message) -- some clarification: I don't anticicpate us initially " \
                     "working on line 3, at least not until organizers of the linked proposal give us direction. " \
                     "\n\n" \
                     "Initially, I just anticipate us working on chapter organizational needs. Eventually, " \
                     "we may work on line 3 together as a region! Apologies for any confusion\" "
    curr_work_dir = os.getcwd()
    team_name = 'someTeam'
    file_name = 'regionalMembers.txt'
    usernames = get_usernames(team_name, file_name, curr_work_dir)
    for sus in usernames:
            os.system('keybase chat send ' + sus + ' ' + clarifying_msg.format(sus))


if __name__ == "__main__":
    # xrsf = set(get_usernames('xrsf', 'xrsf.txt', os.getcwd()))
    # print(xrsf)
    nrwg = set(get_usernames('someTeam', 'nationalMembers.txt', os.getcwd()))
    # shrines = set(get_usernames('loving_shrines', 'lovingShrines.txt', os.getcwd()))
    print(nrwg)
    # all_xrus = set(get_usernames('xrus', 'allMembers.txt', os.getcwd()))
    # print(all_xrus)
    msg = "\"Hey!\nPlease consider using and sharing this toolkit to build shrines in response to the January 6th " \
          "coup: " \
          "https://truthlovedemocracy.org\""
