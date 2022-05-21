# Generated by Django 4.0.3 on 2022-05-21 07:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainPort', '0017_alter_projectmodel_projectfield'),
    ]

    operations = [
        migrations.CreateModel(
            name='newHome',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('newField', models.TextField()),
            ],
        ),
        migrations.AlterField(
            model_name='projectmodel',
            name='projectField',
            field=models.TextField(default=' \n\n      <div class="swiper mySwiper">\n        <div class="swiper-wrapper">\n          <div class="swiper-slide">\n            <img src="https://drive.google.com/uc?export=view&id=1m09zIqXaCEuN_zEwgYgXwVNJ2g5iskFh" alt="SchoolManagement" />\n            <center><em>School Management</em></center>\n          </div>\n          <div class="swiper-slide">\n            <img src="https://drive.google.com/uc?export=view&id=1cyW0esSTcYLR-SiUv--Pd5RzW-i0bStG" alt="Arshskool" />\n            <center><em>Arshskool</em></center>\n          </div>\n          <div class="swiper-slide">\n            <img src="https://drive.google.com/uc?export=view&id=1QyxnsKv6smF2NmABYhdx3ci3ZGPX9g_p" alt="DonationApp" />\n            <center><em>Donation App</em></center>\n          </div>\n          <div class="swiper-slide">\n            <img src="https://drive.google.com/uc?export=view&id=11_KCAaYyeNgPUAL7kbPJ1ybuWNzxp43j" alt="PhisingGoogle" />\n            <center><em>Phishing Google SignIn</em></center>\n          </div>         \n        </div>\n        <div class="swiper-pagination"></div>\n      </div>\n      </div>\n    </div>\n    </div>\n    \n  '),
        ),
    ]
