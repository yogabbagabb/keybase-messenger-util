import json
import os


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