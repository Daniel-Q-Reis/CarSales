from django.db.models.signals import pre_save, post_save, post_delete
from django.db.models import Sum
from django.dispatch import receiver
from .models import Car, CarInventory
from ai_integration.client import generate_car_bio


@receiver(pre_save, sender=Car)
def car_pre_save(sender, instance, **kwargs):
    """
    Before a Car instance is saved, check if the bio is empty.
    If it is, generate one using the AI client.
    """
    if not instance.bio:
        generated_bio = generate_car_bio(instance)
        if generated_bio:
            instance.bio = generated_bio


def update_car_inventory():
    """
    Calculates the total count and value of all cars and creates a new inventory record.
    """
    cars_count = Car.objects.all().count()
    total_value = Car.objects.aggregate(
        total_value=Sum('value')
    )['total_value']
    
    if total_value is None:
        total_value = 0

    CarInventory.objects.create(
        cars_count=cars_count,
        cars_value=total_value
    )

@receiver(post_save, sender=Car)
def car_post_save(sender, instance, **kwargs):
    """
    After a car is saved, trigger the inventory update.
    """
    update_car_inventory()

@receiver(post_delete, sender=Car)
def car_post_delete(sender, instance, **kwargs):
    """
    After a car is deleted, trigger the inventory update.
    """
    update_car_inventory()