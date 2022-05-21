from django.db import models

# Create your models here.


class ProjectModel(models.Model):
    projectField = models.TextField(
        default= """ 



       <div class="swiper mySwiper">
          <div class="swiper-wrapper">
            <div class="swiper-slide">
              <img src="https://drive.google.com/uc?export=view&id=11_KCAaYyeNgPUAL7kbPJ1ybuWNzxp43j" alt="SchoolManagement" />
              <center><em>School Management</em></center>
            </div>
            <div class="swiper-slide">
              <img src="https://drive.google.com/uc?export=view&id=1m09zIqXaCEuN_zEwgYgXwVNJ2g5iskFh" alt="Arshskool" />
              <center><em>Arshskool</em></center>
            </div>
            <div class="swiper-slide">
              <img src="https://drive.google.com/uc?export=view&id=1cyW0esSTcYLR-SiUv--Pd5RzW-i0bStG" alt="DonationApp" />
              <center><em>Donation App</em></center>
            </div>
            <div class="swiper-slide">
              <img src="https://drive.google.com/uc?export=view&id=1QyxnsKv6smF2NmABYhdx3ci3ZGPX9g_p" alt="PhisingGoogle" />
              <center><em>Phishing Google SignIn</em></center>
            </div>         
          </div>
        </div>
        </div>
      </div>
      </div>
    
  """
    
    
    )




class LearntModel(models.Model):
    learnField = models.TextField(default="""
    Hey again! Through out the year I learn alot, 
    learn to work with different languages learn to workwith APIs, 
    I always try to push myself, to challenge myself more and more to know what’s my potential is, 
    what am I capable of doing better, I failed many times many of my projects got failed, I lost interest, 
    but I didn’t give up, maybe my 
    projects aren’t good as we compare to others, but I’m proud of it, 
    it helped me learn, and always challenge to go futher. Still have a long way, 
    I still didn’t know my potential yet!
    """)

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


class SEO(models.Model):
  textArea = models.TextField(default="""
  <title>ArshErgon</title>
    <meta charset="utf-8">
    <meta name="TITLE" content="ArshErgon">
    <meta name="creator" content="ArshErgon">
    <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
    <meta name="KEYWORDS" content="arshergon, programmer, web development">
    <meta name="DESCRIPTION" content="ArshErgon is a web developer and designer based in Dehradun, Uttarakhand, India. He is a self-taught web developer and designer with a background in graphic design and digital media.">
  """
  )


  

