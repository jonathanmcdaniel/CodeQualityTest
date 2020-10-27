from django.contrib.auth.base_user import BaseUserManager
from django.utils.translation import ugettext_lazy as _


class CustomUserManager(BaseUserManager):
    """
    Custom user model manager where email is the unique identifiers
    for authentication instead of usernames.
    """
    def create_user(self, email, password, **extra_fields):
        """
        Create and save a User with the given email and password.
        """
        if not email:
            raise ValueError(_('The Email must be set'))
        email = self.normalize_email(email)
        user = self.model(email_address=email, **extra_fields)
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, email, password, **extra_fields):
        """
        Create and save a Super User with the given email and password.
        """
        if not email:
            raise ValueError(_('The Email must be set'))
        email = self.normalize_email(email)
        user = self.model(email_address=email, **extra_fields)
        user.set_password(password)
        user.save()
        return user

class ClassManager():
    """
    Custom class model manager where class id is the unique identifiers
    for authentication instead of usernames.
    """
    def get_class_data(self, class_id, **extra_fields):
        """
        return a class.
        """
        if not class_id:
            raise ValueError(_('The class does not exist!'))
        class_data = self.model(class_id=class_id, **extra_fields)
        return class_data

class ClassEnrollmentManager():
    """
    Custom class model manager where class id is the unique identifiers
    for authentication instead of usernames.
    """
    def get_class_enrollment_data(self, class_id, **extra_fields):
        """
        return a class.
        """
        if not class_id:
            raise ValueError(_('The class does not exist!'))
        class_data = self.model(class_id=class_id, **extra_fields)
        return class_data

class ClassScheduleManager():
    """
    Custom class model manager where class id is the unique identifiers
    for authentication instead of usernames.
    """
    def get_class_schedule_data(self, class_id, **extra_fields):
        """
        return a class.
        """
        if not class_id:
            raise ValueError(_('The class does not exist!'))
        class_data = self.model(class_id=class_id, **extra_fields)
        return class_data

class AssignmentManager():
    """
    Custom assignment model manager where assignment id is the unique identifiers
    for authentication instead of usernames.
    """
    def get_assignment_schedule_data(self, assignment_id, **extra_fields):
        """
        return a class.
        """
        if not assignment_id:
            raise ValueError(_('The assignment does not exist!'))
        assignment_data = self.model(assignment_id=assignment_id, **extra_fields)
        return assginment_data