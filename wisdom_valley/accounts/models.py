from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.validators import RegexValidator
from django.utils.text import slugify
from django.db.models.signals import pre_save
from ckeditor.fields import RichTextField



phone_validator = RegexValidator(r"^(\+?\d{0,4})?\s?-?\s?(\(?\d{3}\)?)\s?-?\s?(\(?\d{3}\)?)\s?-?\s?(\(?\d{4}\)?)?$", "The phone number provided is invalid")


class User(AbstractUser):
    
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=200, validators=[phone_validator],null=True,blank=True)


class Contact(models.Model):
    name=models.CharField( max_length=120)
    email=models.EmailField(max_length=120)
    phone=models.CharField(max_length=120)
    desc=models.TextField()
    date=models.DateField()

    def __str__(self):
        return  self.name 

class Category(models.Model):
    category_name=models.CharField(max_length=200)

    def __str__(self):
        return self.category_name

class Sub_Category(models.Model):
    category_decide=models.ForeignKey(Category,on_delete=models.CASCADE)
    sub_category_name=models.CharField(max_length=200)

    def __str__(self):
        return self.sub_category_name + ' __ ' + self.category_decide.category_name

class Sub_Sub_Category(models.Model):
    sub_category_decide=models.ForeignKey(Sub_Category,on_delete=models.CASCADE)
    sub_sub_category_name=models.CharField(max_length=200)

    def __str__(self):
        return self.sub_sub_category_name + ' __ ' + self.sub_category_decide.sub_category_name + ' __ ' + self.sub_category_decide.category_decide.category_name

class Course(models.Model):
    course_Name=models.CharField(max_length=200)
    teacher_Name=models.CharField(max_length=200)
    course_Image=models.ImageField(upload_to = "course_Images")
    fee=models.IntegerField()
    Discount=models.IntegerField()
    course_information=RichTextField()
    choices_of_course_study_option = [
        ('Online', 'Online'),
        ('Physical', 'Physical'),
    ]
    model_Name=models.CharField(max_length=10,
        choices=choices_of_course_study_option,
        default='Online',)
    
    category_selection=models.ForeignKey(Category,on_delete=models.CASCADE)
    sub_category_selection=models.ForeignKey(Sub_Category,on_delete=models.CASCADE)
    sub_sub_category_selection=models.ForeignKey(Sub_Sub_Category,on_delete=models.CASCADE)
    duration_In_Month=models.CharField(max_length=2)
    Tags=models.CharField(max_length=200)
    Description=RichTextField()
    slug = models.SlugField(default='', max_length=500, null=True, blank=True)

    def __str__(self):
        return self.course_Name
    
    def get_absolute_url(self):
        from django.urls import reverse
        return reverse("course_detail", kwargs={'slug': self.slug})

    class Meta:
        db_table = "app_Course"

def create_slug(instance, new_slug=None):
    slug = slugify(instance.course_Name)
    if new_slug is not None:
        slug = new_slug
    qs = Course.objects.filter(slug=slug).order_by('-id')
    exists = qs.exists()
    if exists:
        new_slug = "%s-%s" % (slug, qs.first().id)
        return create_slug(instance, new_slug=new_slug)
    return slug

def pre_save_post_receiver(sender, instance, *args, **kwargs):
    if not instance.slug:
        instance.slug = create_slug(instance)

pre_save.connect(pre_save_post_receiver, Course)

class Additional_Information(models.Model):
    course=models.ForeignKey(Course,on_delete=models.CASCADE)
    detail=RichTextField()
