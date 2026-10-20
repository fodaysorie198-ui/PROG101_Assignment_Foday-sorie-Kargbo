Python 3.12.10 (tags/v3.12.10:0cc8128, Apr  8 2025, 12:21:36) [MSC v.1943 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
>>> FUNCTION processStudent(totalDays)
... INPUT name
... REPEAT
... INPUT daysPresent
... IF daysPresent < 0 OR daysPresent > totalDays THEN
... OUTPUT "Invalid days present. Try again."
... END IF
... UNTIL daysPresent >= 0 AND daysPresent <= totalDays
... REPEAT
... INPUT consecutiveAbsent
... IF consecutiveAbsent < 0 OR consecutiveAbsent > totalDays THEN
... OUTPUT "Invalid number. Try again."
... END IF
... UNTIL consecutiveAbsent >= 0 AND consecutiveAbsent <= totalDays
... SET percent = calculateAttendancePercent(daysPresent, totalDays)
... SET status = checkAttendanceStatus(percent)
... SET referral = needsReferral(status, consecutiveAbsent)
... OUTPUT name, percent, status
... IF referral = TRUE THEN
... OUTPUT "Refer to counsellor"
... ELSE
... OUTPUT "No referral needed"
... END IF
... RETURN status
... END FUNCTION
... 3.3 Functions: calculateAttendancePercent, checkAttendanceStatus, needsReferral
... FUNCTION calculateAttendancePercent(daysPresent, totalDays)
... RETURN (daysPresent / totalDays) * 100
... END FUNCTION
