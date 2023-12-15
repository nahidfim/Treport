# Generated by Django 4.2 on 2023-12-13 02:30

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Admin_code_master',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Admin_code', models.CharField(max_length=30)),
                ('Admin_name', models.CharField(max_length=30)),
                ('Admin_password', models.CharField(max_length=30)),
                ('last_login', models.CharField(max_length=30)),
                ('registration_time', models.TimeField(default=datetime.datetime(2023, 12, 13, 2, 30, 54, 613596))),
            ],
        ),
        migrations.CreateModel(
            name='company_master',
            fields=[
                ('company_name', models.CharField(max_length=30, primary_key=True, serialize=False)),
                ('post_number', models.CharField(max_length=30)),
                ('address_1', models.CharField(max_length=30)),
                ('address_2', models.CharField(max_length=30)),
                ('phone', models.CharField(max_length=30)),
                ('fax', models.CharField(max_length=30)),
                ('mail', models.CharField(max_length=30)),
                ('order_number_count', models.IntegerField()),
                ('registration_time', models.TimeField(default=datetime.datetime(2023, 12, 13, 2, 30, 54, 612538))),
            ],
        ),
        migrations.CreateModel(
            name='message_master',
            fields=[
                ('message_id', models.IntegerField(auto_created=True, primary_key=True, serialize=False)),
                ('order_confirmation_message_en', models.CharField(max_length=100)),
                ('order_confirmation_message_jp', models.CharField(max_length=100)),
                ('order_confirmation_message_ch', models.CharField(max_length=100)),
                ('stuff_call_message_en', models.CharField(max_length=100)),
                ('stuff_call_message_jp', models.CharField(max_length=100)),
                ('stuff_call_message_ch', models.CharField(max_length=100)),
                ('confirm_checkout_message_en', models.CharField(max_length=100)),
                ('confirm_checkout_message_jp', models.CharField(max_length=100)),
                ('confirm_checkout_message_ch', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='operator_code_master',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('operator_code', models.CharField(max_length=30)),
                ('operator_name', models.CharField(max_length=30)),
                ('operator_password', models.CharField(max_length=30)),
                ('last_login', models.CharField(max_length=30)),
                ('registration_time', models.TimeField(default=datetime.datetime(2023, 12, 13, 2, 30, 54, 613481))),
            ],
        ),
        migrations.CreateModel(
            name='order_transactions',
            fields=[
                ('order_no', models.CharField(max_length=100, primary_key=True, serialize=False)),
                ('product_name_en', models.CharField(max_length=30)),
                ('lane_no', models.IntegerField(max_length=5)),
                ('table_no', models.IntegerField(max_length=5)),
                ('language_type', models.CharField(max_length=30)),
                ('product_code', models.CharField(max_length=30)),
                ('product_unit_price', models.CharField(max_length=30)),
                ('order_amount', models.IntegerField(max_length=30)),
                ('status', models.CharField(default='active', max_length=30)),
                ('order_time', models.TimeField(default=datetime.datetime(2023, 12, 13, 2, 30, 54, 612174))),
                ('provider_operator_code', models.CharField(max_length=30)),
                ('provision_completion_flag', models.BooleanField(default=False)),
                ('delivery_completion_time', models.TimeField(default=datetime.datetime(2023, 12, 13, 2, 30, 54, 612300))),
                ('order_cancellation_flag', models.BooleanField(default=False)),
                ('order_cancellation_time', models.TimeField(default=datetime.datetime(2023, 12, 13, 2, 30, 54, 612360))),
                ('product_image_link_dest', models.TextField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='product_category_master',
            fields=[
                ('product_category_no', models.IntegerField(primary_key=True, serialize=False)),
                ('product_category', models.CharField(max_length=30)),
                ('product_category_name_en', models.CharField(max_length=30)),
                ('product_category_name_jp', models.CharField(max_length=30)),
                ('product_category_name_ch', models.CharField(max_length=30)),
                ('registration_time', models.TimeField(default=datetime.datetime(2023, 12, 13, 2, 30, 54, 612666))),
            ],
        ),
        migrations.CreateModel(
            name='product_info_master',
            fields=[
                ('product_id', models.IntegerField(auto_created=True, primary_key=True, serialize=False)),
                ('product_category_no', models.CharField(max_length=100, null=True)),
                ('product_code', models.CharField(max_length=100, null=True)),
                ('product_name_en', models.CharField(max_length=50)),
                ('product_name_jp', models.CharField(max_length=50)),
                ('product_name_ch', models.CharField(max_length=50)),
                ('product_price_en', models.CharField(max_length=50)),
                ('product_price_jp', models.CharField(max_length=50)),
                ('product_price_ch', models.CharField(max_length=50)),
                ('category_name', models.CharField(default='Sushi', max_length=90, null=True)),
                ('page_number', models.IntegerField(default=1, max_length=90, null=True)),
                ('registration_time', models.TimeField(default=datetime.datetime(2023, 12, 13, 2, 30, 54, 613108))),
                ('image', models.ImageField(default=None, upload_to='static/media')),
                ('product_image_link_dest', models.TextField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='page_master',
            fields=[
                ('tablet_page_no', models.IntegerField(primary_key=True, serialize=False)),
                ('category_page_no', models.IntegerField()),
                ('product_code', models.CharField(max_length=100)),
                ('registration_time', models.TimeField(default=datetime.datetime(2023, 12, 13, 2, 30, 54, 612778))),
                ('product_category_no', models.ManyToManyField(to='core.product_category_master', verbose_name='Product Category Number')),
            ],
            options={
                'unique_together': {('tablet_page_no', 'category_page_no')},
            },
        ),
    ]
