from django.db import models
from django.utils.translation import ugettext as _
from phonenumber_field.modelfields import PhoneNumberField

from django.contrib.auth import get_user_model

User = get_user_model()

# Create your models here.


class Resume(models.Model):
    user     = models.OneToOneField(User, on_delete=models.CASCADE, related_name='user_resume')
    image    = models.ImageField(_("Your Image"), upload_to='student-image/', blank=True, null=True)
    bg_image = models.ImageField(_("Background Image"), upload_to='bg-image/', blank=True, null=True)
    career   = models.CharField(_("Career"), max_length=500, )
    about_me = models.TextField(_("About Me"), )

    class Meta:
        verbose_name = _("Resume")
        verbose_name_plural = _("Resumes")

    def __str__(self):
        return self.user.full_name + " | " + str(self.user.phone_number)


class Education(models.Model):
    user     = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user_education')
    start_at = models.DateField(_("Start Date"),)
    end_at   = models.DateField(_("End Date"), blank=True, null=True)
    otm_or_place_of_education = models.CharField(_("Institution/Place of Education"), max_length=300,)
    faculty_or_subject        = models.CharField(_("Faculty/Subject"), max_length=300)     
    learned_skill             = models.TextField(_("Learned Skills"),)

    class Meta:
        verbose_name = _("Education")
        verbose_name_plural = _("Educations")

    def __str__(self):
        return self.user.full_name + " | " + str(self.user.phone_number)


class Experience(models.Model):
    user          = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user_experience')
    company       = models.CharField(_("Company Name"), max_length=200)
    occpation     = models.TextField(_('Occupation'), max_length=300)
    qualification = models.TextField(_('Qualification'),)

    start_at = models.DateField(_('Start Date'),)
    end_at   = models.DateField(_('End Date'), blank=True, null=True)

    link     = models.URLField(_('Company Web Site Link'), blank=True, null=True)
    address  = models.CharField(_("Address"), max_length=300, blank=True, null=True)
    phone_number = PhoneNumberField(_("Company Phone-Number"), blank=True, null=True)

    class Meta:
        verbose_name = _("Experience")
        verbose_name_plural = _("Experiences")

    def __str__(self):
        return self.user.full_name + " | " + str(self.user.phone_number)


class Portfolio(models.Model):
    user        = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user_portfolio')
    image       = models.ImageField(_("Cover Image"), upload_to='portfolio-cover-image/', blank=True, null=True)
    name        = models.CharField(_("Name"), max_length=300, blank=True, null=True)
    short_desc  = models.TextField(_('Short Description'), blank=True, null=True)
    description = models.TextField(_('Description'), blank=True, null=True)
    link        = models.URLField(_("Project Link"), blank=True, null=True)

    file        = models.FileField(_("Project File"), upload_to='project-file/', blank=True, null=True)
    document    = models.FileField(_("Project Document"), upload_to='project-document/', blank=True, null=True)

    class Meta:
        verbose_name = _("Portfolio")
        verbose_name_plural = _("Portfolios")

    def __str__(self):
        return self.user.full_name + " | " + str(self.user.phone_number)

    @property
    def imageURL(self):
        try:
            url = self.image.url
        except:
            url=''
        return url


class Image(models.Model):
    portfolio = models.ForeignKey(Portfolio, on_delete=models.CASCADE, related_name='portfolio_image')
    image     = models.ImageField(_("Image"), upload_to="portfolio-image/", blank=True, null=True)
    caption   = models.CharField(_('Caption'), max_length=300, blank=True, null=True)

    class Meta:
        verbose_name = _("Image")
        verbose_name_plural = _("Image")

    def __str__(self):
        return self.portfolio.name
    
    @property
    def imageURL(self):
        try:
            url = self.image
        except:
            url=''
        return url

