from django.db import models

# Create your models here.


class ProjectModel(models.Model):
    projectField = models.TextField(
        default= """ 
        <div class="swiper mySwiper">
        <div class="swiper-wrapper">
          <div class="swiper-slide">
            <a href="#modal">
              <img src="https://drive.google.com/uc?export=view&id=1m09zIqXaCEuN_zEwgYgXwVNJ2g5iskFh" alt="" /></a>
            <center><em>Click or Swipe</em></center>
          </div>
          <div class="swiper-slide">
            <img src="https://drive.google.com/uc?export=view&id=1cyW0esSTcYLR-SiUv--Pd5RzW-i0bStG" alt="" />
          </div>
          <div class="swiper-slide">
            <img src="https://drive.google.com/uc?export=view&id=1QyxnsKv6smF2NmABYhdx3ci3ZGPX9g_p" alt="" />
          </div>
          <div class="swiper-slide">
            <img src="https://drive.google.com/uc?export=view&id=11_KCAaYyeNgPUAL7kbPJ1ybuWNzxp43j" alt="" />
          </div>
        </div>
        <div class="swiper-pagination"></div>
      </div>
      </div>
    </div>
    </div>
                    
                    <! -- here modal box start add and change the name as required -->
                     <!-- Modal -->
                    <div class="modal-wrapper" id="modal">
                    <div class="modal-body card">
                        <div class="modal-header">
                            <h2 class="heading">ProjectName</h2>
                        </div>
                        <h6>Why does it made?</h6>
                        <p>this is made for</p>
                        <h6>Things which made it possible.</h6>
                        <p>java, html, css</p>
                        <h6>What you learn?</h6>
                        <p>I learn deeply</p>
                    </div>
                    <a href="#!" class="outside-trigger"></a>
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
<style>
.modal-header {
  align-items: baseline;
  display: flex;
  justify-content: space-between;
  z-index: 2;
  color:white;
  margin: 0px auto;
}


.modal-wrapper {
  z-index: 2;
  align-items: center;
  background: rgba(0, 0, 0, 0.7);
  bottom: 0;
  display: flex;
  justify-content: center;
  left: 0;
  position: fixed;
  right: 0;
  top: 0;
  color:white;
}

#modal {
    color:white;
  opacity: 0;
  transition: opacity 0.25s ease-in-out;
  visibility: hidden;
}
#modal:target {
  opacity: 1;
  visibility: visible;
}
#modal:target .modal-body {
  opacity: 1;
  transform: translateY(1);
}
#modal .modal-body {
  background-color: rgb(31, 32, 32);

  max-width: 500px;
  opacity: 0;
  transform: translateY(-100px);
  transition: opacity 0.25s ease-in-out;
  width: 100%;
  z-index: 2;

}

.outside-trigger {
  bottom: 0;
  cursor: default;
  left: 0;
  position: fixed;
  right: 0;
  top: 0;
}

</style>

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
  