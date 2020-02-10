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

def get_client_ip(request):
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[0]
    else:
        ip = request.META.get('REMOTE_ADDR')
    return ip

def message(request):
    # return render(request, 'levels/message.html')
    return render(request, 'levels/index.html')

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
		response = render(request, 'levels/level3.html',{'form': form, 'error_message':error})
		response.set_cookie('IX', "4E39654C93E39DCEAD499692F99F7A1C") 
		return response





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



def level6(request):
	if request.method == "POST":
		values = submit(request,6)
		form = submissionForm(request.POST)

		if values == True:
			form = submissionForm()
			return HttpResponseRedirect("/levels/7/") 

		else:
			return render(request, 'levels/level6.html',values)
	
	else:
		form = submissionForm()
		error = ""
		return render(request, 'levels/level6.html',{'form': form, 'error_message':error})


def level7(request):
	if request.method == "POST":
		values = submit(request,7)
		form = submissionForm(request.POST)

		if values == True:
			form = submissionForm()
			return HttpResponseRedirect("/levels/8/") 

		else:
			return render(request, 'levels/level7.html',values)
	
	else:
		form = submissionForm()
		error = ""
		return render(request, 'levels/level7.html',{'form': form, 'error_message':error})


def level8(request):
	if request.method == "POST":
		values = submit(request,7)
		form = submissionForm(request.POST)

		if values == True:
			form = submissionForm()
			return HttpResponseRedirect("/levels/9/") 

		else:
			return render(request, 'levels/level8.html',values)
	
	else:
		form = submissionForm()
		error = ""
		return render(request, 'levels/level8.html',{'form': form, 'error_message':error})


def level9(request):
	if request.method == "POST":
		values = submit(request,9)
		form = submissionForm(request.POST)

		if values == True:
			form = submissionForm()
			return HttpResponseRedirect("/levels/10/") 

		else:
			return render(request, 'levels/level9.html',values)
	
	else:
		form = submissionForm()
		error = ""
		return render(request, 'levels/level9.html',{'form': form, 'error_message':error})


def level10(request):
	if request.method == "POST":
		values = submit(request,10)
		form = submissionForm(request.POST)

		if values == True:
			form = submissionForm()
			return HttpResponseRedirect("/levels/11/") 

		else:
			return render(request, 'levels/level10.html',values)
	
	else:
		form = submissionForm()
		error = ""
		return render(request, 'levels/level10.html',{'form': form, 'error_message':error})


def level11(request):
	if request.method == "POST":
		values = submit(request,11)
		form = submissionForm(request.POST)

		if values == True:
			form = submissionForm()
			return HttpResponseRedirect("/levels/1/") 

		else:
			return render(request, 'levels/level11.html',values)
	
	else:
		form = submissionForm()
		error = ""
		return render(request, 'levels/level11.html',{'form': form, 'error_message':error})












def submit(request, level):
	if request.method != "POST":
		return HttpResponseRedirect("/levels/submissions") 

	else:
		form = submissionForm(request.POST)
		# error = str(request.__dict__)
		# return render(request, 'levels/level1.html',{'form': form, 'error_message':error})

		if form.is_valid():
			obj = Submissions()
			client_ip = get_client_ip(request)

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
				
				obj.ip = client_ip
				obj.key = form.cleaned_data['key'].upper()
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
					obj.save()
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



