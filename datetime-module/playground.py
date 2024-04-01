from datetime import datetime, timezone, timedelta

current_dt = datetime.now()

utc_tz = timezone(offset=timedelta(0))
ist_tz = timezone(offset=timedelta(hours=5, minutes=30))
pst_tz = timezone(offset=timedelta(hours=-8, minutes=0))

print("utc", current_dt.astimezone(utc_tz))
print("ist_tz", current_dt.astimezone(ist_tz))
print("pst_tz", current_dt.astimezone(pst_tz))
