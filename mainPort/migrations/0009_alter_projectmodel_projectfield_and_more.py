# Generated by Django 4.0.3 on 2022-05-10 13:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainPort', '0008_alter_projectmodel_projectfield'),
    ]

    operations = [
        migrations.AlterField(
            model_name='projectmodel',
            name='projectField',
            field=models.TextField(default=' <div class="swiper mySwiper">\n        <div class="swiper-wrapper">\n          <div class="swiper-slide">\n            <a href="#modal"><img src="https://swiperjs.com/demos/images/nature-1.jpg" /></a>\n            <center><em>Click or Swipe</em></center>\n          </div>\n          <div class="swiper-slide">\n            <img src="https://swiperjs.com/demos/images/nature-2.jpg" />\n          </div>\n          <div class="swiper-slide">\n            <img src="https://swiperjs.com/demos/images/nature-3.jpg" />\n          </div>\n          <div class="swiper-slide">\n            <img src="https://swiperjs.com/demos/images/nature-4.jpg" />\n          </div>\n          <div class="swiper-slide">\n            <img src="https://swiperjs.com/demos/images/nature-5.jpg" />\n          </div>\n          <div class="swiper-slide">\n            <img src="https://swiperjs.com/demos/images/nature-6.jpg" />\n          </div>\n          <div class="swiper-slide">\n            <img src="https://swiperjs.com/demos/images/nature-7.jpg" />\n          </div>\n          <div class="swiper-slide">\n            <img src="https://swiperjs.com/demos/images/nature-8.jpg" />\n          </div>\n          <div class="swiper-slide">\n            <img src="https://swiperjs.com/demos/images/nature-9.jpg" />\n          </div>\n        </div>\n        <div class="swiper-pagination"></div>\n      </div>\n      </div>\n    </div>\n    </div>\n                    \n                    <! -- here modal box start add and change the name as required -->\n                     <!-- Modal -->\n                    <div class="modal-wrapper" id="modal">\n                    <div class="modal-body card">\n                        <div class="modal-header">\n                            <h2 class="heading">ProjectName</h2>\n                        </div>\n                        <h6>Why does it made?</h6>\n                        <p>this is made for</p>\n                        <h6>Things which made it possible.</h6>\n                        <p>java, html, css</p>\n                        <h6>What you learn?</h6>\n                        <p>I learn deeply</p>\n                    </div>\n                    <a href="#!" class="outside-trigger"></a>\n                </div>\n                    \n                    '),
        ),
        migrations.AlterField(
            model_name='stylemodel',
            name='styleField',
            field=models.TextField(default='        \n<style>\n.modal-header {\n  align-items: baseline;\n  display: flex;\n  justify-content: space-between;\n  z-index: 2;\n  color:white;\n  margin: 0px auto;\n}\n\n\n.modal-wrapper {\n  z-index: 2;\n  align-items: center;\n  background: rgba(0, 0, 0, 0.7);\n  bottom: 0;\n  display: flex;\n  justify-content: center;\n  left: 0;\n  position: fixed;\n  right: 0;\n  top: 0;\n  color:white;\n}\n\n#modal {\n    color:white;\n  opacity: 0;\n  transition: opacity 0.25s ease-in-out;\n  visibility: hidden;\n}\n#modal:target {\n  opacity: 1;\n  visibility: visible;\n}\n#modal:target .modal-body {\n  opacity: 1;\n  transform: translateY(1);\n}\n#modal .modal-body {\n  background-color: rgb(31, 32, 32);\n\n  max-width: 500px;\n  opacity: 0;\n  transform: translateY(-100px);\n  transition: opacity 0.25s ease-in-out;\n  width: 100%;\n  z-index: 2;\n\n}\n\n.outside-trigger {\n  bottom: 0;\n  cursor: default;\n  left: 0;\n  position: fixed;\n  right: 0;\n  top: 0;\n}\n\n</style>\n\n        '),
        ),
    ]