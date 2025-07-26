# Generated manually for DevShowcase refactoring

from django.db import migrations

def update_template_names(apps, schema_editor):
    Account = apps.get_model('showcase', 'Account')
    
    # Mapping of old template names to new ones
    template_mapping = {
        'portfolio_template1.html': 'showcase_theme1.html',
        'portfolio_template2.html': 'showcase_theme2.html',
        'portfolio_template3.html': 'showcase_theme3.html',
        'portfolio_template4.html': 'showcase_theme4.html',
    }
    
    for old_name, new_name in template_mapping.items():
        Account.objects.filter(portfolio_template=old_name).update(portfolio_template=new_name)

def reverse_template_names(apps, schema_editor):
    Account = apps.get_model('showcase', 'Account')
    
    # Reverse mapping
    template_mapping = {
        'showcase_theme1.html': 'portfolio_template1.html',
        'showcase_theme2.html': 'portfolio_template2.html',
        'showcase_theme3.html': 'portfolio_template3.html',
        'showcase_theme4.html': 'portfolio_template4.html',
    }
    
    for old_name, new_name in template_mapping.items():
        Account.objects.filter(portfolio_template=old_name).update(portfolio_template=new_name)

class Migration(migrations.Migration):

    dependencies = [
        ('showcase', '0003_auto_20201227_1354'),
    ]

    operations = [
        migrations.RunPython(update_template_names, reverse_template_names),
    ]
