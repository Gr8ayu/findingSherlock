from django.shortcuts import render
from .forms import submissionForm
from .models import Submissions, User, Flags
from django.http import HttpResponse, HttpResponseRedirect
from django.utils import timezone

def validate(password,level):
	flags = Flags.objects.all()

	for i in flags:
		if password == i.flag and level == i.level:
			return True
	return False

"""
def level1(request):
	if request.method == "POST":
		
		form = submissionForm(request.POST)

		if form.is_valid():
			obj = Submissions()

			try:
				userdata = User.objects.get(userKey= form.cleaned_data['username'])
				
				obj.key = form.cleaned_data['key']
				obj.level = form.cleaned_data['level']
				obj.userID = userdata
				obj.date_time = timezone.now()
				obj.validity = validate(obj.key)
				
				if obj.validity:
					userdata.score += 1
					userdata.save()
					obj.save()
					return render(request, 'levels/level2.html')

				else:
					userdata.save()
					obj.save()
					error = "Wrong Key"
					return render(request, 'levels/level1.html',{'form': form, 'error_message':error})
				
				# TODO USE redirect here
				
			except User.DoesNotExist:
				
				# raise e
				error = "User not found"
				return render(request, 'levels/level1.html',{'form': form, 'error_message':error})
				# form = submissionForm()
		else:
			error = "Invalid Input"

			return render(request, 'levels/level1.html',{'form': form, 'error_message':error})
				

	
	form = submissionForm()
	error = ""
	return render(request, 'levels/level1.html',{'form': form, 'error_message':error})
"""
def level1(request):
	if request.method == "POST":
		values = submit(request,1)
		form = submissionForm(request.POST)

		if values == True:
			form = submissionForm()
			return HttpResponseRedirect("/levels/2/") 

		else:
			return render(request, 'levels/level1.html',values)
	
	else:
		form = submissionForm()
		error = ""
		return render(request, 'levels/level1.html',{'form': form, 'error_message':error})

def level2(request):
	if request.method == "POST":
		values = submit(request,2)
		form = submissionForm(request.POST)

		if values == True:
			form = submissionForm()
			return HttpResponseRedirect("/levels/3/") 

		else:
			return render(request, 'levels/level2.html',values)
	
	else:
		form = submissionForm()
		error = ""
		return render(request, 'levels/level2.html',{'form': form, 'error_message':error})


def level3(request):
	if request.method == "POST":
		values = submit(request,3)
		form = submissionForm(request.POST)

		if values == True:
			form = submissionForm()
			return HttpResponseRedirect("/levels/4/") 

		else:
			return render(request, 'levels/level3.html',values)
	
	else:
		form = submissionForm()
		error = ""
		return render(request, 'levels/level3.html',{'form': form, 'error_message':error})





def level4(request):
	if request.method == "POST":
		values = submit(request,4)
		form = submissionForm(request.POST)

		if values == True:
			form = submissionForm()
			return HttpResponseRedirect("/levels/5/") 

		else:
			return render(request, 'levels/level4.html',values)
	
	else:
		form = submissionForm()
		error = ""
		return render(request, 'levels/level4.html',{'form': form, 'error_message':error})


def level5(request):
	if request.method == "POST":
		values = submit(request,5)
		form = submissionForm(request.POST)

		if values == True:
			form = submissionForm()
			return HttpResponseRedirect("/levels/6/") 

		else:
			return render(request, 'levels/level5.html',values)
	
	else:
		form = submissionForm()
		error = ""
		return render(request, 'levels/level5.html',{'form': form, 'error_message':error})













def submit(request, level):
	if request.method != "POST":
		return HttpResponseRedirect("/levels/submissions") 

	else:
		form = submissionForm(request.POST)
		# error = str(request.__dict__)
		# return render(request, 'levels/level1.html',{'form': form, 'error_message':error})

		if form.is_valid():
			obj = Submissions()

			try:
				userdata = User.objects.get(userKey= form.cleaned_data['username'])

				obj.level = form.cleaned_data['level']

				if level != obj.level:
					error = "Invalid level selection "
					return {'form': form, 'error_message':error}

				
				# submitted_responses = Submissions.objects.filter(userID=userdata).filter(level=obj.level).filter(key=obj.key)
				submitted_responses = Submissions.objects.filter(userID=userdata.userID).filter(level=obj.level)
				for submission in submitted_responses:
	
					if submission.validity :
						error = "Valid key Already registered for this level " + "DEBUG :" + str(submission.SubmissionId)
						# error += "DEBUG : " + str(len(submitted_responses)) + " " + str(obj.level) +"|"   
						return {'form': form, 'error_message':error}
						# return HttpResponseRedirect(request, 'levels/level1.html',{'form': form, 'error_message':error})
				
				obj.key = form.cleaned_data['key']
				obj.userID = userdata
				obj.date_time = timezone.now()
				obj.validity = validate(obj.key, obj.level)
				error = "DEBUG : level = " + str(obj.level)
				# return {'form': form, 'error_message':error}
				# return render(request, 'levels/level1.html',{'form': form, 'error_message':error})
				if obj.validity:
					userdata.score += 1
					userdata.save()
					obj.save()
					return True
					# return HttpResponseRedirect('/levels/submissions/')

				else :
					error = "entered key is Wrong"
					return {'form': form, 'error_message':error}
					# return render(request, 'levels/level1.html',{'form': form, 'error_message':error})
				

				# TODO USE redirect here
				
			except User.DoesNotExist:
				error = "User not found"
				return {'form': form, 'error_message':error}
				# return render(request, 'levels/level1.html',{'form': form, 'error_message':error})
				
		else:
			error = "Invalid data"
			return {'form': form, 'error_message':error}
			# return render(request, 'levels/level1.html',{'form': form, 'error_message':error})

	# else:
		# form = submissionForm()

	# return render(request, 'levels/level1.html',{'form': form})

def leaderboard(request):
	users = User.objects.all().order_by('-score')
	return render(request,'levels/leaderboard.html',{'users':users})

def submissions(request):
	submissionList = Submissions.objects.all()
	return render(request,'levels/submissions.html',{'submissionList':submissionList})



