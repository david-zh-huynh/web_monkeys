from django.contrib import admin
from .models import Service, Portfolio, PortfolioModal, Team


# Register your models here.
class InlinePortfolioModal(admin.StackedInline):
    model = PortfolioModal
    extra = 0


class PortfolioAdmin(admin.ModelAdmin):
    inlines = [InlinePortfolioModal]


admin.site.register(Service)
admin.site.register(Portfolio, PortfolioAdmin)
admin.site.register(Team)
