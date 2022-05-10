from django.db import models

# Create your models here.


class ProjectModel(models.Model):
    projectField = models.TextField(
        default= """<div class="swiper-slide">
                        <img src="https://swiperjs.com/demos/images/nature-1.jpg" 
                        onclick="myFirstFun()" />
                        <center><em>Caption goes here</em></center>
                    </div>
                    <div class="swiper-slide">
                        <img src="https://swiperjs.com/demos/images/nature-2.jpg" onclick="myFirstFun()" />
                    </div>
                    <div class="swiper-slide">
                        <img src="https://swiperjs.com/demos/images/nature-3.jpg" />
                    </div>
                    <div class="swiper-slide">
                        <img src="https://swiperjs.com/demos/images/nature-4.jpg" />
                    </div>
                    <div class="swiper-slide">
                        <img src="https://swiperjs.com/demos/images/nature-5.jpg" />
                    </div>
                    <div class="swiper-slide">
                        <img src="https://swiperjs.com/demos/images/nature-6.jpg" />
                    </div>
                    <div class="swiper-slide">
                        <img src="https://swiperjs.com/demos/images/nature-7.jpg" />
                    </div>
                    <div class="swiper-slide">
                        <img src="https://swiperjs.com/demos/images/nature-8.jpg" />
                    </div>
                    <div class="swiper-slide">
                        <img src="https://swiperjs.com/demos/images/nature-9.jpg" />
                    </div>"""
    
    
    )


class AboutMeModel(models.Model):
    aboutField = models.TextField()


    def __str__(self):
        return self.aboutField[:50]


class LearntModel(models.Model):
    learnField = models.TextField()

    def __str__(self):
        return self.learnField[:50]



class JavaScriptModel(models.Model):
    javascriptField = models.TextField(
        default= """function myFirstFun() {
                    Swal.fire({
                            title: 'Custom width, padding, color, background.',
                            width: 600,
                            padding: '3em',
                            color: '#fff',
                            background: '#1A1110',
                            })
                }
        """
    )

    def __str__(self):
        return self.javascriptField[:50]    