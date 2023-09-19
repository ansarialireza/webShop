from unittest import result
from django.db import models
from django.urls import reverse
# Create your models here.
for_what_choices = (
        ('c2' , "2col"),
        ('c3' , "3col"),
        ('f1' , "fisrt1"),
        ('f2' , "fisrt2"),
        ('b1' , "big1"),
        ('e1' , "end1"),
)
#----------------------------------------------------------------------------------------------
class Survey(models.Model):
    name = models.CharField(max_length=200)
    email = models.EmailField()
    phoneNumber = models.CharField(max_length=200)
    title = models.CharField(max_length=200)
    text = models.TextField()

    def __str__(self):
        return f"{self.email} - {self.name}"
#----------------------------------------------------------------------------------------------
class FAQGroup(models.Model):
    bigTitle = models.CharField(max_length=100)

    def __str__(self):
        return self.bigTitle
#----------------------------------------------------------------------------------------------
class FAQ(models.Model):
    group = models.ForeignKey(FAQGroup,on_delete=models.CASCADE,related_name="faqs")
    question = models.CharField(max_length=100)
    answer = models.TextField()

    def __str__(self):
        return self.question
#----------------------------------------------------------------------------------------------
class shop(models.Model):
    name = models.CharField(max_length=100)
    address = models.TextField()
    postal_code = models.CharField(max_length=10)
    phone = models.CharField(max_length=10)
    image = models.ImageField(upload_to='web_shop/banners/')


    def __str__(self):
        return self.name
#----------------------------------------------------------------------------------------------
class banner(models.Model):
    bigTitle = models.CharField(max_length=200)
    smallTitle = models.CharField(max_length=200)
    image = models.ImageField(upload_to='web_shop/banners/%Y/%m/%d/')
    for_what = models.CharField(max_length=2,choices=for_what_choices)
    main_link = models.CharField(max_length=200)
    out_link = models.CharField(max_length=200)
    button = models.CharField(max_length=200,null=True,blank=True)
    arg = models.CharField(max_length=200,null=True,blank=True)



    def get_absolute_url(self):
        args = []
        if(self.arg):
            args = self.arg.split(',')
        return reverse(f"{self.main_link}:{self.out_link}",args=args)

    def __str__(self):
        return self.bigTitle

    @staticmethod
    def filter():
        banners = banner.objects.all()
        result = {}

        for what in for_what_choices:
            reason = what[0]
            result[reason] = banners.filter(for_what=reason)

        return result







