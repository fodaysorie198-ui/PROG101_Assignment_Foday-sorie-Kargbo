Python 3.12.10 (tags/v3.12.10:0cc8128, Apr  8 2025, 12:21:36) [MSC v.1943 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
>>> START Main
... CONSTANT GOOD_LIMIT = 80, RISK_LIMIT = 60
... CONSTANT ABSENCE_LIMIT = 5, MAX_STUDENTS = 60
... SET goodCount = 0, riskCount = 0, criticalCount = 0
... REPEAT
... INPUT totalDays
... IF totalDays <= 0 THEN OUTPUT "Total days must be above 0"
... UNTIL totalDays > 0
... REPEAT
... INPUT numStudents
... IF numStudents < 1 OR numStudents > MAX_STUDENTS THEN
... OUTPUT "Enter a number from 1 to", MAX_STUDENTS
... END IF
... UNTIL numStudents >= 1 AND numStudents <= MAX_STUDENTS
... FOR i = 1 TO numStudents DO
... SET status = processStudent(totalDays)
... IF status = "Good" THEN
... goodCount = goodCount + 1
... ELSE IF status = "At Risk" THEN
... riskCount = riskCount + 1
... ELSE
... criticalCount = criticalCount + 1
... END IF
... END FOR
... CALL displaySummary(goodCount, riskCount, criticalCount)
