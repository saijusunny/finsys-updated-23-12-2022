# Generated by Django 4.0.4 on 2023-01-06 06:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0065_balance_sheet_amount'),
    ]

    operations = [
        migrations.CreateModel(
            name='itemstock',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('items', models.CharField(max_length=100, null=True)),
                ('date', models.DateField(null=True)),
                ('qty', models.IntegerField(null=True)),
                ('amount', models.IntegerField(null=True)),
                ('transactions', models.CharField(max_length=100, null=True)),
                ('details', models.CharField(max_length=100, null=True)),
                ('details1', models.CharField(blank=True, default='', max_length=100)),
                ('stocks', models.CharField(blank=True, max_length=100)),
                ('bill', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='app1.purchasebill')),
                ('cid', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='app1.company')),
                ('debit', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='app1.purchasedebit')),
                ('inv', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='app1.invoice')),
                ('stock', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='app1.stockadjust')),
            ],
        ),
        migrations.AddField(
            model_name='itemtable',
            name='amount',
            field=models.IntegerField(blank=True, default='0', null=True),
        ),
        migrations.DeleteModel(
            name='item',
        ),
    ]
