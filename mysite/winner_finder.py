#python3 manage.py shell

from levels.models import Submissions
from levels.models import User

max_score = 2
S = Submissions.objects.all()
U = User.objects.filter(score = max_score)

for eachuser in U:
	last_submission = S.filter(userID=eachuser).filter(validity=True).order_by('-date_time')[0]
	print(str(last_submission.userID.userKey) +"||"+str(last_submission.date_time))
