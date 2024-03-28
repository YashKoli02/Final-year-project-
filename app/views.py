from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from app.verify import authentication, form_varification
from django.contrib.auth.decorators import login_required
from django.views.decorators.cache import cache_control
from datetime import datetime
from .form import *
from app.models import Applicant_data
import PyPDF2
import sys
import io
from .prediction import *
from pyresparser import ResumeParser
from pdfminer3.layout import LAParams, LTTextBox
from pdfminer3.pdfpage import PDFPage
from pdfminer3.pdfinterp import PDFResourceManager
from pdfminer3.pdfinterp import PDFPageInterpreter
from pdfminer3.converter import TextConverter

# Create your views here.
def index(request):
    # return HttpResponse("This is Home page")    
    return render(request, "index.html")

def log_in(request):
    if request.method == "POST":
        # return HttpResponse("This is Home page")  
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(username = username, password = password)

        if user is not None:
            if str(user) == "hr@gmail.com":
                login(request, user)
                messages.success(request, "Log In Successful...!")
                return redirect("hr_dashboard")
            else:
                login(request, user)
                messages.success(request, "Log In Successful...!")
                return redirect("dashboard")
        else:
            messages.error(request, "Invalid User...!")
            return redirect("log_in")
    # return HttpResponse("This is Home page")    
    return render(request, "log_in.html")

def register(request):
    if request.method == "POST":
        fname = request.POST['fname']
        lname = request.POST['lname']
        username = request.POST['username']
        password = request.POST['password']
        password1 = request.POST['password1']
        # print(fname, contact_no, ussername)
        verify = authentication(fname, lname, password, password1)
        if verify == "success":
            user = User.objects.create_user(username, password, password1)          #create_user
            user.first_name = fname
            user.last_name = lname
            user.save()
            messages.success(request, "Your Account has been Created.")
            return redirect("/")
            
        else:
            messages.error(request, verify)
            return redirect("register")
    # return HttpResponse("This is Home page")    
    return render(request, "register.html")


@login_required(login_url="log_in")
@cache_control(no_cache = True, must_revalidate = True, no_store = True)
def hr_dashboard(request):
    jobs = Job.objects.all()
    context = {
        'fname': request.user.first_name, 
        'jobs' : jobs,
        }
    return render(request, "hr_dashboard.html", context)

@login_required(login_url="log_in")
@cache_control(no_cache = True, must_revalidate = True, no_store = True)
def create_job(request):
    context = {
        'fname': request.user.first_name, 
        'form' : JobForm(),
        }
    if request.method=="POST":
        new_job = JobForm(request.POST, request.FILES)
        if  new_job.is_valid():
            job_description = new_job.cleaned_data['job_description']
            years_of_experience = new_job.cleaned_data['years_of_experience']
            salary = new_job.cleaned_data['salary']
            location = new_job.cleaned_data['location']
            required_skills = new_job.cleaned_data['required_skills']
            job_position = new_job.cleaned_data['job_position']
            save_job = Job(job_position = job_position, job_description = job_description, years_of_experience = years_of_experience, salary = salary, location = location, required_skills = required_skills)
            save_job.save()
            messages.success(request, "Job Saved Successfully!!!")
            return redirect("hr_dashboard")

    return render(request, "create_job.html", context)

@login_required(login_url="log_in")
@cache_control(no_cache = True, must_revalidate = True, no_store = True)
def log_out(request):
    logout(request)
    messages.success(request, "Log out Successfuly...!")
    return redirect("/")



@login_required(login_url="log_in")
@cache_control(no_cache = True, must_revalidate = True, no_store = True)
def dashboard(request):
    context = {
        'fname': request.user.first_name, 
        'form' : applicant_form(),
        }
    if request.method == "POST":
        form = applicant_form(request.POST, request.FILES)
        if form.is_valid():
            first_name = form.cleaned_data['first_name']
            last_name = form.cleaned_data['last_name']
            cv = form.cleaned_data['cv']

            # Read the content of the uploaded file
            cv_content = cv.read()

            # Create a BytesIO object for the PDF reader
            pdf_stream = io.BytesIO(cv_content)

            # Create a PDF reader object
            pdf_reader = PyPDF2.PdfReader(pdf_stream)

            # Initialize an empty string to store text
            text = ''

            # Iterate through each page and extract text
            for page_num in range(len(pdf_reader.pages)):
                page = pdf_reader.pages[page_num]
                text += page.extract_text()

            predicted_category = resume_prediction(text)
            user_level = level_identifier(len(pdf_reader.pages))
            actual_skills, recommended_skills = skills_having(text,predicted_category)
            resume_score = find_resume_score(text)
            
            if predicted_category == "PMO":
                predicted_category = "Project Management Officer"
            data_save = Applicant_data(applicant_first_name = first_name, applicant_last_name = last_name, applicant_cv = cv, prediction = predicted_category, user_level = user_level, actual_skills = actual_skills, recommended_skills = recommended_skills, resume_score = resume_score, no_of_pages = len(pdf_reader.pages))
            data_save.date = datetime.now()
            data_save.save()
            messages.success(request, "You may be Eligible for : " + predicted_category)
            return redirect("result")
        else:
            messages.error(request, "Invalid Form")
            return redirect("dashboard")
    return render(request, "dashboard.html",context)

@login_required(login_url="log_in")
@cache_control(no_cache = True, must_revalidate = True, no_store = True)
def result(request):
    result_data = Applicant_data.objects.last()
    skills = eval(result_data.actual_skills)
    rec_skills = eval(result_data.recommended_skills)
    context = {
        'fname': request.user.first_name, 
        'result_data' : result_data,
        'skills' : skills,
        'rec_skills' : rec_skills,
        }
    return render(request, "result.html", context)