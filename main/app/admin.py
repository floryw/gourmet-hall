from django.contrib import admin
from app.models import ProfileUser, Category,CardFood,Order,Cart,reservation

admin.site.register(ProfileUser)
admin.site.register(Category)
admin.site.register(CardFood)
admin.site.register(Order)
admin.site.register(Cart)
admin.site.register(reservation)