from django.db import models
from django.contrib.auth.models import User

from django.db.models.signals import post_save
from django.dispatch import receiver
    
     
class Profile(models.Model):

    user = models.OneToOneField(User, on_delete=models.CASCADE)

    photo = models.ImageField(
        upload_to='user-photos',
        default=None,
        null=True
    )

    location = models.CharField(
        max_length=100,
        default=None,
        blank=True,
        null=True
    )

    def __str__(self):
        return self.user.username + " profile"


@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()
    

class ProfileContact(models.Model):
    
    link_re = {
        'mail': r'([A-Za-z0-9]+[.-_])*[A-Za-z0-9]+@[A-Za-z0-9-]+(\.[A-Z|a-z]{2,})+',
        'phone': r'^\\+?\\d{1,4}?[-.\\s]?\\(?\\d{1,3}?\\)?[-.\\s]?\\d{1,4}[-.\\s]?\\d{1,4}[-.\\s]?\\d{1,9}$',
        't.me': [r'https://t.me/(\w+)', r'@(\w+)', r'(\w+)'],
        'vk': [r'https://vk.com/(\w+)', r'(\w+)']
    }
    
    link_placeholder = {
        'mail': 'example@site.domain',
        'phone': '+NNN (NNN) NN-NN',
        't.me': 'https://t.me/<login> or @<login> or <login>',
        'vk': 'https://vk.com/<login or id> or <login or id>'
    }
    
    default_icons = {
        'mail': 'contacts/mail.png',
        'phone': 'contacts/phone.png',
        't.me': 'contacts/telegram.png',
        'vk': 'contacts/vk.png'
    }
    
    link_template = {
        'mail': 'mailto:{}',
        'phone': 'tel:{}',
        't.me': 'https://t.me/{}',
        'vk': 'https://vk.com/{}'
    }
    
    contact_type = models.CharField(
        max_length=7,
        choices=(
            ('mail', 'Email'),
            ('phone', 'Phone'),
            ('t.me', 'Telegram'),
            ('vk', 'VK'),
        )
    )
    
    is_active = models.BooleanField(default=True)
    contact = models.CharField(max_length=40, null=True, blank=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='contacts')
    
    @property
    def link_url(self):
        return self.link_template[self.contact_type].format(self.contact)
    
    @property
    def contact_icon(self):
        return self.default_icons[self.contact_type]