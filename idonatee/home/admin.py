from django.contrib import admin

from .models import Signupp
from .models import Detail
from .models import Detail2
from .models import Rdetail
from .models import Odetail

# Register your models here.

admin.site.register(Signupp)
admin.site.register(Detail)
admin.site.register(Detail2)
admin.site.register(Rdetail)
admin.site.register(Odetail)
