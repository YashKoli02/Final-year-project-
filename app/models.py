from django.db import models

# Create your models here.
class Applicant_data(models.Model):
    applicant_first_name = models.CharField(max_length=50)
    applicant_last_name = models.CharField(max_length=50)
    applicant_cv = models.FileField()
    prediction = models.CharField(max_length = 50)
    resume_score = models.CharField(max_length = 50)
    no_of_pages = models.CharField(max_length = 50)
    user_level = models.CharField(max_length = 50)
    actual_skills = models.CharField(max_length = 900)
    recommended_skills = models.CharField(max_length = 900)
    date = models.DateField()

    def __str__(self):
        return self.applicant_first_name + " " + self.applicant_last_name
    

class Job(models.Model):
    job_position = models.CharField(max_length=100)
    job_description = models.TextField()
    years_of_experience = models.IntegerField()
    salary = models.DecimalField(max_digits=10, decimal_places=2)
    location = models.CharField(max_length=100)
    required_skills = models.CharField(max_length=255)

    def __str__(self):
        return self.job_position