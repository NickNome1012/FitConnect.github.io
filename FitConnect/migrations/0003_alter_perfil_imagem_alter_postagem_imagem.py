# Generated by Django 5.0.2 on 2024-06-07 14:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('FitConnect', '0002_rename_text_postagem_texto_alter_perfil_imagem_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='perfil',
            name='imagem',
            field=models.ImageField(blank=True, upload_to='pfp/'),
        ),
        migrations.AlterField(
            model_name='postagem',
            name='imagem',
            field=models.ImageField(blank=True, upload_to='post_img/'),
        ),
    ]
