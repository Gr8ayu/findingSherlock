from django.db import models

# Create your models here.




class Flags(models.Model):
	flag = models.CharField(max_length=50)
	flagID = models.AutoField(primary_key=True)
	level = models.IntegerField(default=1)
	flagString = models.CharField(max_length=50, default="-")


	def __str__(self):
		return "{} : {} ".format(self.flagID, self.flagString)

class User(models.Model):
	userID = models.AutoField(primary_key=True)
	username = models.CharField(max_length=50)
	userKey = models.CharField(max_length=50)
	score = models.IntegerField(default=0)
	def __str__(self):
		return self.username
	
class Clue(models.Model):
    clueID = models.AutoField(primary_key=True)
    level = models.IntegerField()
    clue = models.TextField()
    visible = models.BooleanField(default=False)

    def __str__(self):
        return str(self.level ) +" : " + self.clue[:30]


class Submissions(models.Model):
    level_list = (
        (1, 'level 1'),
        (2, 'level 2'),
        (3, 'level 3'),
        (4, 'level 4'),
        (5, 'level 5'),
        (6, 'level 6'),
        (7, 'level 7'),
        (8, 'level 8'),
        (9, 'level 9'),
        (10, 'level 10')
    )
    SubmissionId = models.AutoField(primary_key=True)
    ip = models.CharField(max_length=20, default="0.0.0.0")
    level = models.IntegerField(choices=level_list)
    key = models.CharField(max_length=50)
    validity = models.BooleanField(default=False)

    date_time = models.DateTimeField('date published')
    userID = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        verbose_name="submission by user",
    )

    def isValidKey(self):


    	if True:
    		self.validity = True
    	else:
    		self.validity = False

    def __str__(self):
    	return "{}, level:{}, {}".format(self.SubmissionId, self.level,self.userID)

    class Meta:
        ordering = ["-date_time"]
