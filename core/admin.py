from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import (
    HomeBanner, Feature, AboutSection, Service, FunFact,
    ChooseUsSection, ChooseUsPoint, CTASection, RecycleMaterial,
    Testimonial, Project, NewsPost,
)

# ---- Dashboard branding (optional but nice) ----
admin.site.site_header = "BRTL Website Dashboard"
admin.site.site_title = "BRTL Admin"
admin.site.index_title = "Manage Home Page Content"


@admin.register(HomeBanner)
class HomeBannerAdmin(admin.ModelAdmin):
    list_display = ('heading', 'subtitle', 'order', 'is_active')
    list_editable = ('order', 'is_active')
    list_filter = ('is_active',)
    search_fields = ('heading', 'subtitle')


@admin.register(Feature)
class FeatureAdmin(admin.ModelAdmin):
    list_display = ('title', 'icon_class', 'order', 'is_active')
    list_editable = ('order', 'is_active')
    list_filter = ('is_active',)


@admin.register(AboutSection)
class AboutSectionAdmin(admin.ModelAdmin):
    list_display = ('heading', 'is_active')
    list_filter = ('is_active',)

    def has_add_permission(self, request):
        # keep it a "singleton" style section - only allow one row
        if self.model.objects.exists():
            return False
        return super().has_add_permission(request)


@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    list_display = ('title', 'icon_class', 'order', 'is_active')
    list_editable = ('order', 'is_active')
    list_filter = ('is_active',)


@admin.register(FunFact)
class FunFactAdmin(admin.ModelAdmin):
    list_display = ('label', 'number', 'suffix', 'order')
    list_editable = ('order',)


class ChooseUsPointInline(admin.TabularInline):
    model = ChooseUsPoint
    extra = 1


@admin.register(ChooseUsSection)
class ChooseUsSectionAdmin(admin.ModelAdmin):
    list_display = ('heading', 'emergency_phone', 'is_active')
    inlines = [ChooseUsPointInline]

    def has_add_permission(self, request):
        if self.model.objects.exists():
            return False
        return super().has_add_permission(request)


@admin.register(CTASection)
class CTASectionAdmin(admin.ModelAdmin):
    list_display = ('heading', 'is_active')

    def has_add_permission(self, request):
        if self.model.objects.exists():
            return False
        return super().has_add_permission(request)


@admin.register(RecycleMaterial)
class RecycleMaterialAdmin(admin.ModelAdmin):
    list_display = ('name', 'order')
    list_editable = ('order',)


@admin.register(Testimonial)
class TestimonialAdmin(admin.ModelAdmin):
    list_display = ('name', 'designation', 'rating', 'order', 'is_active')
    list_editable = ('order', 'is_active')
    list_filter = ('is_active', 'rating')
    search_fields = ('name', 'designation')


@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ('title', 'category', 'order', 'is_active')
    list_editable = ('order', 'is_active')
    list_filter = ('is_active',)


@admin.register(NewsPost)
class NewsPostAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'post_date', 'comment_count', 'is_active')
    list_editable = ('is_active',)
    list_filter = ('is_active', 'author')
    search_fields = ('title', 'excerpt')
    date_hierarchy = 'post_date'