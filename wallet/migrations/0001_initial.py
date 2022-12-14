# Generated by Django 4.1 on 2022-08-24 10:27

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Account',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('account_type', models.CharField(max_length=20)),
                ('account_name', models.CharField(max_length=20)),
                ('savings', models.IntegerField()),
                ('destination', models.CharField(max_length=15)),
            ],
        ),
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=20)),
                ('last_name', models.CharField(max_length=20)),
                ('gender', models.CharField(choices=[('a', 'Male'), ('b', 'Female')], max_length=15)),
                ('address', models.CharField(max_length=15)),
                ('age', models.PositiveIntegerField(max_length=15)),
                ('nationality', models.CharField(max_length=15)),
                ('phonenumber', models.CharField(max_length=15)),
                ('email', models.EmailField(max_length=15)),
                ('profile_picture', models.ImageField(upload_to='profile_pictures/')),
                ('marital_status', models.CharField(choices=[('a', 'Married'), ('b', 'Single'), ('b', 'Others')], max_length=15)),
                ('signature', models.ImageField(upload_to='signature_pictures/')),
                ('date_created', models.DateTimeField(default=django.utils.timezone.now)),
                ('employment_status', models.BooleanField()),
            ],
        ),
        migrations.CreateModel(
            name='Notifications',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_created', models.DateTimeField(default=django.utils.timezone.now)),
                ('message', models.CharField(max_length=15)),
                ('isactive', models.BooleanField()),
                ('image', models.ImageField(upload_to='profile_pictures/')),
            ],
        ),
        migrations.CreateModel(
            name='Receipts',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('receipt_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('recipt_File', models.FileField(upload_to='wallet/')),
            ],
        ),
        migrations.CreateModel(
            name='ThirdParty',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=15)),
                ('email', models.EmailField(max_length=254)),
                ('phone_Number', models.IntegerField()),
                ('transaction_cost', models.IntegerField()),
                ('active', models.BooleanField()),
                ('account', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='ThirdPary_account', to='wallet.account')),
            ],
        ),
        migrations.CreateModel(
            name='Wallet',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('balance', models.IntegerField()),
                ('pin', models.SmallIntegerField(max_length=6)),
                ('active', models.BooleanField()),
                ('date_created', models.DateTimeField(default=django.utils.timezone.now)),
                ('type', models.CharField(max_length=20)),
                ('customer', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='Wallet_customer', to='wallet.customer')),
            ],
        ),
        migrations.CreateModel(
            name='Transaction',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('transaction_type', models.CharField(max_length=10)),
                ('transaction_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('status', models.CharField(max_length=15)),
                ('receipt', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Transaction_receipts', to='wallet.receipts')),
                ('thirdParty', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Transaction_third_party', to='wallet.thirdparty')),
            ],
        ),
        migrations.CreateModel(
            name='Reward',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('points', models.CharField(max_length=25)),
                ('date', models.DateTimeField(default=django.utils.timezone.now)),
                ('gender', models.CharField(choices=[('a', 'Male'), ('b', 'Female')], max_length=15)),
                ('transaction', models.ForeignKey(choices=[('a', 'receipts'), ('b', 'purchases'), ('c', 'sales'), ('d', 'payments')], on_delete=django.db.models.deletion.CASCADE, related_name='Reward_transaction', to='wallet.transaction')),
                ('wallet', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Reward_wallet', to='wallet.wallet')),
            ],
        ),
        migrations.AddField(
            model_name='receipts',
            name='transaction',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Reciepts_transaction', to='wallet.transaction'),
        ),
        migrations.CreateModel(
            name='Loan',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('loan_type', models.CharField(max_length=25)),
                ('amount', models.IntegerField()),
                ('date', models.DateTimeField(default=django.utils.timezone.now)),
                ('loan_term', models.IntegerField()),
                ('due_date', models.DateField(default=django.utils.timezone.now)),
                ('loan_balance', models.IntegerField()),
                ('duration', models.CharField(max_length=15)),
                ('interest_rate', models.IntegerField()),
                ('status', models.CharField(max_length=15)),
                ('wallet', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Loan_wallet', to='wallet.wallet')),
            ],
        ),
        migrations.CreateModel(
            name='Card',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_Issued', models.DateTimeField(default=django.utils.timezone.now)),
                ('card_status', models.CharField(max_length=15)),
                ('security_code', models.IntegerField()),
                ('signature', models.ImageField(upload_to='signature_pictures/')),
                ('issuer', models.CharField(max_length=15)),
                ('account', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Card_account', to='wallet.account')),
            ],
        ),
        migrations.AddField(
            model_name='account',
            name='wallet',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Account_wallet', to='wallet.wallet'),
        ),
    ]
