Python 3.12.10 (tags/v3.12.10:0cc8128, Apr  8 2025, 12:21:36) [MSC v.1943 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
>>> FUNCTION calculateAttendancePercent(daysPresent, totalDays)
... RETURN (daysPresent / totalDays) * 100
... END FUNCTION
...  
... FUNCTION checkAttendanceStatus(percent)
... IF percent >= GOOD_LIMIT THEN
... RETURN "Good"
... ELSE IF percent >= RISK_LIMIT THEN
... RETURN "At Risk"
... ELSE
... RETURN "Critical"
... END IF
... END FUNCTION
...  
... FUNCTION needsReferral(status, consecutiveAbsent)
... RETURN (status = "Critical") OR (consecutiveAbsent >= ABSENCE_LIMIT)
