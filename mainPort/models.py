from django.db import models

# Create your models here.


class ProjectModel(models.Model):
    projectField = models.TextField(
        default= """ 
        <div class="swiper mySwiper">
        <div class="swiper-wrapper">
          <div class="swiper-slide">
              <img src="https://drive.google.com/uc?export=view&id=1m09zIqXaCEuN_zEwgYgXwVNJ2g5iskFh" alt="" /></a>
            <center><em>School Management</em></center>
          <div class="swiper-slide">
            <img src="https://drive.google.com/uc?export=view&id=1cyW0esSTcYLR-SiUv--Pd5RzW-i0bStG" alt="" />
            <center><em>Arshskool</em></center>

          </div>
          <div class="swiper-slide">
            <img src="https://drive.google.com/uc?export=view&id=1QyxnsKv6smF2NmABYhdx3ci3ZGPX9g_p" alt="" />
            <center><em>Donation App</em></center>

          </div>
          <div class="swiper-slide">
            <img src="https://drive.google.com/uc?export=view&id=11_KCAaYyeNgPUAL7kbPJ1ybuWNzxp43j" alt="" />
            <center><em>Phishing Google SignIn</em></center>

          </div>
        </div>
        <div class="swiper-pagination"></div>
      </div>
      </div>
    </div>
    </div>
               
                    """
    
    
    )


class AboutMeModel(models.Model):
    aboutField = models.TextField()


    def __str__(self):
        return self.aboutField[:50]


class LearntModel(models.Model):
    learnField = models.TextField()

    def __str__(self):
        return self.learnField[:50]



class StyleModel(models.Model):
    styleField = models.TextField(
        default= """        


        """
    )

    def __str__(self):
        return self.styleField[:50]    



  
class SkillsModel(models.Model):
  python = models.CharField(max_length=2)
  django = models.CharField(max_length=2)
  fsd = models.CharField(max_length=2)
  dsa = models.CharField(max_length=2)
  machine = models.CharField(max_length=2)
  db = models.CharField(max_length=2)
  problemSolving = models.CharField(max_length=2)
  java = models.CharField(max_length=2)
  graphicDesign = models.CharField(max_length=2)
  