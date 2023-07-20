import subprocess


data = subprocess.check_output(['netsh', 'wlan', 'show', 'profiles']).decode('utf-8').split('\n')
profiles = [line.split(":")[1].strip() for line in data if "All User Profile" in line]

for profile in profiles:
    try:
        results = subprocess.check_output(['netsh', 'wlan', 'show', 'profile', profile, 'key=clear']).decode('utf-8').split('\n')
        password = [line.split(":")[1].strip() for line in results if "Key Content" in line][0]

        print("{:<30} | {}".format(profile, password))
    except IndexError:
        print("{:<30} | ไม่พบรหัสผ่าน".format(profile))
