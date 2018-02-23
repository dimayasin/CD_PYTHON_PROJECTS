from __future__ import unicode_literals
from django.db import models
from ..login_app import Users 

class UsersManager(models.Manager):
    def validateCourseData(self, postData):
        errors = []
        if len(postData['cname']) < 5:
            errors.append("User first name should be more than 5 characters")
        if len(postData['description']) < 15:
            errors.append( "User last name should be more than 15 characters")

        return errors

class Courses(models.Model):
    name = models.CharField(max_length=255)
    description = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    objects = UsersManager()