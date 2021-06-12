import keybase_util

if __name__ == "__main__":
    usernames = keybase_util.get_user_names_from_file("nrwgMembers.txt")
    keybase_util.send_message_from_file(usernames, "message.txt", 5, 10)