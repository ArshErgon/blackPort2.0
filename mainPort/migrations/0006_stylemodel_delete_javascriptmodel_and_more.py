# Generated by Django 4.0.3 on 2022-05-10 13:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainPort', '0005_alter_javascriptmodel_javascriptfield_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='StyleModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('styleField', models.TextField(default='        \n<style>\n\n\n.modal-header {\n  align-items: baseline;\n  display: flex;\n  justify-content: space-between;\n  z-index: 2;\n}\n\n.close {\n  background: none;\n  border: none;\n  cursor: pointer;\n  display: flex;\n  height: 16px;\n  text-decoration: none;\n  width: 16px;\n  z-index: 2;\n}\n.close svg {\n  width: 16px;\n}\n\n.modal-wrapper {\n  z-index: 2;\n  align-items: center;\n  background: rgba(0, 0, 0, 0.7);\n  bottom: 0;\n  display: flex;\n  justify-content: center;\n  left: 0;\n  position: fixed;\n  right: 0;\n  top: 0;\n}\n\n#modal {\n  opacity: 0;\n  transition: opacity 0.25s ease-in-out;\n  visibility: hidden;\n}\n#modal:target {\n  opacity: 1;\n  visibility: visible;\n}\n#modal:target .modal-body {\n  opacity: 1;\n  transform: translateY(1);\n}\n#modal .modal-body {\n  max-width: 500px;\n  opacity: 0;\n  transform: translateY(-100px);\n  transition: opacity 0.25s ease-in-out;\n  width: 100%;\n  z-index: 2;\n\n}\n\n.outside-trigger {\n  bottom: 0;\n  cursor: default;\n  left: 0;\n  position: fixed;\n  right: 0;\n  top: 0;\n}\n\n.button__link {\n  text-decoration: none;\n}\n</style>\n\n        ')),
            ],
        ),
        migrations.DeleteModel(
            name='JavaScriptModel',
        ),
        migrations.AlterField(
            model_name='projectmodel',
            name='projectField',
            field=models.TextField(default='<div class="swiper-slide">\n                        <a href="#modal"\n                        <img src="https://swiperjs.com/demos/images/nature-1.jpg" />\n                        <center><em>Caption goes here</em></center>\n                    </div>\n                    <div class="swiper-slide">\n                        <img src="https://swiperjs.com/demos/images/nature-2.jpg" />\n                    </div>\n                    <div class="swiper-slide">\n                        <img src="https://swiperjs.com/demos/images/nature-3.jpg" />\n                    </div>\n                    <div class="swiper-slide">\n                        <img src="https://swiperjs.com/demos/images/nature-4.jpg" />\n                    </div>\n                    <div class="swiper-slide">\n                        <img src="https://swiperjs.com/demos/images/nature-5.jpg" />\n                    </div>\n                    <div class="swiper-slide">\n                        <img src="https://swiperjs.com/demos/images/nature-6.jpg" />\n                    </div>\n                    <div class="swiper-slide">\n                        <img src="https://swiperjs.com/demos/images/nature-7.jpg" />\n                    </div>\n                    <div class="swiper-slide">\n                        <img src="https://swiperjs.com/demos/images/nature-8.jpg" />\n                    </div>\n                    <div class="swiper-slide">\n                        <img src="https://swiperjs.com/demos/images/nature-9.jpg" />\n                    </div>\n                    \n                    <! -- here modal box start add and change the name as required -->\n                     <!-- Modal -->\n                    <div class="modal-wrapper" id="modal">\n                        <div class="modal-body card">\n                            <div class="modal-header">\n                                <h2 class="heading">Modal Header</h2>\n                                <a href="#!" role="button" class="close" aria-label="close this modal">\n                                    <svg viewBox="0 0 24 24">\n                                        <path d="M24 20.188l-8.315-8.209 8.2-8.282-3.697-3.697-8.212 8.318-8.31-8.203-3.666 3.666 8.321 8.24-8.206 8.313 3.666 3.666 8.237-8.318 8.285 8.203z" />\n                                    </svg>\n                                </a>\n                            </div>\n                            <p>Simple example using the <code>:target</code> selector to open a modal.</p>\n                        </div>\n                        <a href="#!" class="outside-trigger"></a>\n                    </div>\n                    \n                    '),
        ),
    ]
