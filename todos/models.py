from django.db import models
from django.utils import timezone

# Create your models here.

class Person(models.Model):
  person_name = models.CharField(max_length=20)
  create_date = models.DateTimeField('Create Date')

  def __str__(self):
    return self.person_name

class Task(models.Model):
  person = models.ForeignKey(Person, on_delete=models.CASCADE)
  task_desc = models.CharField(max_length=200)
  task_start = models.DateTimeField('Start Date')
  task_end = models.DateTimeField('End Date', default=timezone.now)

  def __str__(self):
    return self.task_desc

class Job(models.Model):
  task = models.ForeignKey(Task, on_delete=models.CASCADE)
  job_desc = models.CharField(max_length=200)

  def __str__(self):
   return self.job_desc
