from django.contrib import admin
from .models import Collection_Model
from .models import Watches
from .models import Collections
from .models import Brands
from .models import Carts
from .models import Cart_Items
from .models import Purchases


admin.site.register(Brands)
admin.site.register(Carts)
admin.site.register(Cart_Items)
admin.site.register(Collections)
admin.site.register(Watches)
admin.site.register(Collection_Model)
admin.site.register(Purchases)

# Register your models here.
