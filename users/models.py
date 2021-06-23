from django.db import models
from django.utils import timezone
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager
from phonenumber_field.modelfields import PhoneNumberField

from django.db.models.signals import post_save



class CustomAccountManager(BaseUserManager):

    def create_superuser(self, email, phone_number, full_name, password, **other_fields):

        other_fields.setdefault('is_staff', True)
        other_fields.setdefault('is_superuser', True)
        other_fields.setdefault('is_active', True)

        if other_fields.get('is_staff') is not True:
            raise ValueError(
                'Superuser must be assigned to is_staff=True.')
        if other_fields.get('is_superuser') is not True:
            raise ValueError(
                'Superuser must be assigned to is_superuser=True.')

        return self.create_user(email, phone_number, full_name, password, **other_fields)

    def create_user(self, email, phone_number, full_name, password, **other_fields):
        other_fields.setdefault('is_active', True)
        if not email:
            raise ValueError(_("Siz elektron pochta manzilingizni ko'rsatishingiz kerak"))
        
        email = self.normalize_email(email)
        user  = self.model(email=email, phone_number=phone_number, full_name=full_name, **other_fields)
        user.set_password(password)
        user.save()
        return user

class NewUser(AbstractBaseUser, PermissionsMixin):

    email        = models.EmailField(_('Email'), unique=True)
    full_name   = models.CharField(_("Full Name"), max_length=150)
    phone_number = PhoneNumberField(_('Phone Number'), unique=True) # validators should be a list
    start_date   = models.DateTimeField(default=timezone.now)
    about        = models.TextField(_("About"), blank=True, null=True)
    is_staff     = models.BooleanField(default=False)
    is_active    = models.BooleanField(default=True)

    objects = CustomAccountManager()

    USERNAME_FIELD  = 'email'
    REQUIRED_FIELDS = ['phone_number', 'full_name']

    def __str__(self):
        return self.full_name + " | " + str(self.phone_number)



class Student(models.Model):
    class faculty_choice(models.TextChoices):
        dif     = "DIF",    _("Dasturiy injiniring fakulteti")
        kif     = "KIF",    _("Kompyuter injiniringi fakulteti")
        ttf     = "TTF",    _("Telekommunikatsiya texnologiyalari fakulteti")
        axf     = "AXF",    _("Axborot xavfsizligi fakulteti")
        tvtf    = "TvTF",   _("Televizion texnologiyalar fakulteti")
        akt_im  = "AKT_IM", _("AKT sohasida iqtisodiyot va menejment fakulteti")
        akt_kt  = "AKT_KT", _("AKT sohasida Kasb ta`limi fakulteti")
    class level_choice(models.TextChoices):
        first_level  = "I", _("1-kurs")
        second_level = "II", _("2-kurs")
        third_level  = "III", _("3-kurs")
        fourth_level = "IV", _("4-kurs")

    student = models.OneToOneField(NewUser, blank=True, null=True, on_delete=models.SET_NULL, related_name='student')
    image   = models.ImageField(_("Your Image"), upload_to="student-image/", blank=True, null=True)

    faculty = models.CharField(_('Faculty'), max_length=300, blank=True, null=True, choices=faculty_choice.choices)
    group   = models.CharField(_("Group"), max_length=100, blank=True, null=True,)  
    level   = models.CharField(_('Level'), max_length=50, blank=True, null=True, choices=level_choice.choices)

    class Meta:
        verbose_name        = _("Student")
        verbose_name_plural = _("Students")

    def __str__(self):
        if self.group:
            return self.student.full_name + " > " + self.group
        return self.student.full_name
    
    @property
    def imageURL(self):
        try:
            url = self.image.url
        except:
            url = ''
        return url

def post_save_student_receiver(sender, instance, created, **kwargs):
    student = instance
    if created:
        student = Student(student=student)
        student.save()

post_save.connect(post_save_student_receiver, sender=NewUser)