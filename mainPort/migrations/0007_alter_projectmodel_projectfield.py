# Generated by Django 4.0.3 on 2022-05-10 13:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainPort', '0006_stylemodel_delete_javascriptmodel_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='projectmodel',
            name='projectField',
            field=models.TextField(default=' <div class="swiper mySwiper">\n        <div class="swiper-wrapper">\n          <div class="swiper-slide">\n            <a href="#modal"><img src="https://swiperjs.com/demos/images/nature-1.jpg" /></a>\n          </div>\n          <div class="swiper-slide">\n            <img src="https://swiperjs.com/demos/images/nature-2.jpg" />\n          </div>\n          <div class="swiper-slide">\n            <img src="https://swiperjs.com/demos/images/nature-3.jpg" />\n          </div>\n          <div class="swiper-slide">\n            <img src="https://swiperjs.com/demos/images/nature-4.jpg" />\n          </div>\n          <div class="swiper-slide">\n            <img src="https://swiperjs.com/demos/images/nature-5.jpg" />\n          </div>\n          <div class="swiper-slide">\n            <img src="https://swiperjs.com/demos/images/nature-6.jpg" />\n          </div>\n          <div class="swiper-slide">\n            <img src="https://swiperjs.com/demos/images/nature-7.jpg" />\n          </div>\n          <div class="swiper-slide">\n            <img src="https://swiperjs.com/demos/images/nature-8.jpg" />\n          </div>\n          <div class="swiper-slide">\n            <img src="https://swiperjs.com/demos/images/nature-9.jpg" />\n          </div>\n        </div>\n        <div class="swiper-pagination"></div>\n      </div>\n      </div>\n    </div>\n    </div>\n                    \n                    <! -- here modal box start add and change the name as required -->\n                     <!-- Modal -->\n                    <div class="modal-wrapper" id="modal">\n                        <div class="modal-body card">\n                            <div class="modal-header">\n                                <h2 class="heading">Modal Header</h2>\n                                <a href="#!" role="button" class="close" aria-label="close this modal">\n                                    <svg viewBox="0 0 24 24">\n                                        <path d="M24 20.188l-8.315-8.209 8.2-8.282-3.697-3.697-8.212 8.318-8.31-8.203-3.666 3.666 8.321 8.24-8.206 8.313 3.666 3.666 8.237-8.318 8.285 8.203z" />\n                                    </svg>\n                                </a>\n                            </div>\n                            <p>Simple example using the <code>:target</code> selector to open a modal.</p>\n                        </div>\n                        <a href="#!" class="outside-trigger"></a>\n                    </div>\n                    \n                    '),
        ),
    ]
