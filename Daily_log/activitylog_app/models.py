# Create your models here.
from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
# from django.utils.text import slugify
# from django.core.validators import MinValueValidator, MaxValueValidator
# from account.models import Profile

class Satellite(models.Model):
    satellite=models.CharField(max_length=50)
    def __str__(self):
        return self.satellite

class Comment(models.Model):
    user=models.ForeignKey(User, models.SET_DEFAULT,default="old user")
    # user=models.ForeignKey(User, on_delete=SET_DEFAULT)
    # user=models.ForeignKey(User, on_delete=models.CASCADE,blank=True,null=True)
    #IF user is deleted all the comments by user is deleted

    #Ticket generation part
    # date=models.DateField() 
    # date=models.DateField(default=timezone.localdate) # USE_TZ  for UTC
    # time=models.TimeField(verbose_name="Time (HH:MM:SS)",null=True,blank=True )
    date_time=models.DateTimeField(default=timezone.now,editable=True,null=True,blank=True )
    # date_time=models.DateTimeField(auto_now_add=True,null=True,blank=True )
    satellite = models.ForeignKey(Satellite,on_delete=models.CASCADE,related_name='comments')
    subsystem_CHOICES = [('AOCS', 'AOCS'),('IMAGE', 'IMAGE PAYLOAD'),('THERMAL','THERMAL'),('POWER','POWER'),('TTC','TTC')]
    subsystem_type=models.CharField(max_length=50,choices=subsystem_CHOICES,default='IMAGE PAYLOAD')
    details = models.TextField()
    photo = models.ImageField(upload_to='uploads/%Y/%m/%d/',null=True,blank=True)
    upload = models.FileField(upload_to='uploads/%Y/%m/%d/',null=True,blank=True)
    # slug = models.SlugField(max_length=250,unique_for_date='created',blank=True)
    created = models.DateTimeField(auto_now_add=True,blank=True)
    updated = models.DateTimeField(auto_now=True)
    class Meta:
        pass
        # ordering = ('-created',)
        # ordering = ('-created',)
    def __str__(self):
        return f'Satellite {self.satellite}{self.date_time}' 

    def get_absolute_url(self):
        from django.urls import reverse
        return reverse("activitylog_app:comment_detail",kwargs={'pk' : self.pk})
        # return reverse("xpndr:comment_detail",args=[self.id, self.slug,self.publish.year,self.publish.month,self.publish.day])
        # return reverse("xpndr:comment_detail",args={self.satellite,self.transponder,self.transponder.transponder_number})
    
    # def get_absolute_url(self):
    #     return reverse("xpndr:comment_delete",args=[self.id,]) (self.date).replace('-', '')

    
    def save1(self, *args, **kwargs):
        complaint_type1=" "
        sat=" "
        if self.complaint_type=="Interference":
            complaint_type1="I"
        elif self.complaint_type=="Signal_Degradation":
            complaint_type1="SD"
        elif self.complaint_type=="Overdrive":
            complaint_type1="S"
        else :
            complaint_type1="SA"
        sat=str(self.satellite)
        
        self.ticket=f"MCF/{sat[0]+sat[-2:]}{self.transponder}{complaint_type1}{(self.date.strftime('%Y''%m''%d'))}"
        # self.ticket=f"MCF/{sat.replace('SAT','')}{self.transponder}{complaint_type1}{(self.date.strftime('%Y''%m''%d'))}"
        if not self.slug:
            self.slug = slugify(str(timezone.now()))
        super().save(*args, **kwargs)


    def delete(self, *args, **kwargs):
        if self.upload:
            self.upload.delete()
        if self.photo:
            self.photo.delete()
        super().delete(*args, **kwargs)
