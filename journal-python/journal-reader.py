#!/usr/bin/python3
# See https://www.freedesktop.org/software/systemd/python-systemd/journal.html

from systemd import journal
j = journal.Reader()
j.this_boot()
j.log_level(journal.LOG_DEBUG)
j.add_match(_SYSTEMD_UNIT="journal-app-service.service")
for entry in j:
    print(entry)
    print(entry['MESSAGE'])
