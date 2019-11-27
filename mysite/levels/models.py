from django.db import models

# Create your models here.

# FLAGS = ["1111","2222","3333"] 
# https://passwordsgenerator.net/md5-hash-generator/
# easy question
# lets do it once more
# did you enjoy it
# coding club rvce is great
# that was bit tricky
# its a hard one
# one flag more
# you are doing great
# You can win
# you are awesome
 
# 049DCA6B1BA0235FAC48A2B596E1804C
# 915BF19648AC5F6068CFB34163B6B4E9
# 35A9C07BBEC03A35C7185E49A8263DDE
# 40BEE3FB652B1C6BA49E2E6728741229
# 4066065DE9130579502E092072BD5037
# 3AAFB310127FF688D5A2ECE7178ECDBC
# AD54E713C37919A76AE0E68C33C675BD
# 03602896DAAA66DEA614BC7CF6683DA3
# 4E39654C93E39DCEAD499692F99F7A1C
# 75EAD9B4B013E38060CF6668B8FF8F6B
# 7215EE9C7D9DC229D2921A40E899EC5F



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
    # userId = models.CharField(max_length=50)
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
