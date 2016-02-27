from django.contrib import admin

from .models import Question
from .models import Watches_Main
from .models import Watches_Men
from .models import Watches_Women
from .models import Collection_Model

admin.site.register(Watches_Main)
admin.site.register(Watches_Men)
admin.site.register(Watches_Women)
admin.site.register(Collection_Model)

# Register your models here.
