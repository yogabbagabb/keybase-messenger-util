from crontab import CronTab


def make_process_sg_reminder():
    cron = CronTab(user='anjaliagrawal')
    job = cron.new(command='/Library/Frameworks/Python.framework/Versions/3.7/bin/python3.7 '
                           '/Users/anjaliagrawal/Documents/jiivan/vidrohi/allyship/scripts'
                           '/send_keybase_message.py process_imp')
    job.dow.on('MON')
    job.hour.on('8')
    job.minute.on(0)
    cron.write()


def remove_all_jobs():
    cron = CronTab(user='anjaliagrawal')
    cron.remove_all()
    for job in cron:
        print(job)


def find_jobs():
    cron = CronTab(user='anjaliagrawal')
    for job in cron:
        print(job)


if __name__ == "__main__":
    find_jobs()
