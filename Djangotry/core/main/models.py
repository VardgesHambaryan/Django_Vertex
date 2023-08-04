from django.db import models

class Introduction(models.Model):
    img = models.ImageField('Blog Image' , upload_to='media')
    title = models.CharField('Blog Title' , max_length=255) 
    content = models.TextField('Blog Content', max_length=255)
    date = models.DateTimeField('Blog Date')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Introduction'
        verbose_name_plural = 'Introductions'   

class Service(models.Model):

    content1 = models.TextField('First Content')
    content2 = models.TextField('Second Content')

    def __str__(self) -> str:
        return "Service"
    
    class Meta:
        verbose_name = 'Service'
        verbose_name_plural = 'Services'

    

class Icon(models.Model):

    icon = models.CharField('Icon', max_length=255)
    text = models.TextField('Icon Text')

    def __str__(self) -> str:
        return self.icon
    
    class Meta:
        verbose_name = 'Icon'
        verbose_name_plural = 'Icons'


class OurGallery(models.Model):

    img = models.ImageField('Image: ' , upload_to='media')
    title = models.CharField('Title: ', max_length=255)
    subtitle = models.CharField('Title: ', max_length=255)

    def __str__(self) -> str:
        return self.title
    

    class Meta:
        verbose_name = 'Our Gallery'
        verbose_name_plural = 'Our Galleries'



class AboutUs(models.Model):

    content1 = models.TextField('First Content')
    content2 = models.TextField('Second Content')
    content3 = models.TextField('Third Content')


    def __str__(self) -> str:
        return "About Us"
    
    class Meta:
        verbose_name = 'About Us'
        verbose_name_plural = 'About Us'

class ContactUs(models.Model):


    name = models.CharField("User Name" , max_length=255)
    email = models.EmailField("User Email")
    message = models.TextField('User Text')


    def __str__(self) -> str:
        return self.name
    

    class Meta:
        verbose_name = 'Contact Us'
        verbose_name_plural = 'Contact Us'
        
class HomeBG(models.Model):

    bg1 = models.ImageField("Image 1" , upload_to='media')
    bg2 = models.ImageField("Image 2" , upload_to='media')
    bg3 = models.ImageField("Image 3" , upload_to='media')
    bg4 = models.ImageField("Image 4" , upload_to='media')

    
    def __str__(self) -> str:
        return "Home BackGround"
    
    class Meta:
        verbose_name = "Home BackGround"
        verbose_name_plural = "Home BackGround"
