Service controlling the backlights on my Raspberry Pi based calendar board.

Place the python script in: `/opt/BacklightService/` and place the service file in `/etc/systemd/system`, then make sure the system is time synced and that the timezone is set correctly, and run `systemctl start BacklightService` and `systemctl enable BacklightService`.
