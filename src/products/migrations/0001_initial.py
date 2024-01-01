# Generated by Django 5.0 on 2023-12-30 02:10

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product_name', models.CharField(max_length=255, verbose_name='产品名称')),
                ('description', models.TextField(blank=True, null=True, verbose_name='产品描述')),
                ('price', models.DecimalField(decimal_places=2, max_digits=10, verbose_name='价格')),
                ('quantity', models.IntegerField(default=0, verbose_name='数量')),
                ('name', models.CharField(max_length=255, verbose_name='收件人姓名')),
                ('address', models.CharField(max_length=255, verbose_name='地址')),
                ('phone', models.CharField(max_length=255, verbose_name='电话号码')),
                ('buy_date', models.DateTimeField(verbose_name='购买')),
            ],
            options={
                'verbose_name': '产品',
                'verbose_name_plural': '产品',
            },
        ),
    ]