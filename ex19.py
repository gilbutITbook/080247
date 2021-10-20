def passwd_to_dict(filename):
    users = {}
    with open(filename) as passwd:
        for one_line in passwd:
            if one_line.startswith(('#', '\n')):
                continue
            user_info = one_line.split(':')
            users[user_info[0]] = int(user_info[2])
    return users

print(passwd_to_dict('etc/linux-etc-passwd.txt'))