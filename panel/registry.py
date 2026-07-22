# panel/registry.py
# Ei file e shob model register kora, jate generic CRUD view gula
# kono model er jonno kaj korte pare. Notun model add korte hole
# shudhu ei dict e ekta entry add korle hobe -- view/template kichu
# change korte hobe na.

from core.models import (
    HomeBanner, Feature, AboutSection, Service, FunFact,
    ChooseUsSection, ChooseUsPoint, CTASection, RecycleMaterial,
    Testimonial, Project, NewsPost,
)

MODEL_REGISTRY = {
    'banners': {
        'model': HomeBanner,
        'label': 'Home Banners',
        'fields': '__all__',
        'list_fields': ['heading', 'subtitle', 'order', 'is_active'],
    },
    'features': {
        'model': Feature,
        'label': 'Features',
        'fields': '__all__',
        'list_fields': ['title', 'order', 'is_active'],
    },
    'about': {
        'model': AboutSection,
        'label': 'About Section',
        'fields': '__all__',
        'list_fields': ['heading', 'subtitle', 'is_active'],
    },
    'services': {
        'model': Service,
        'label': 'Services',
        'fields': '__all__',
        'list_fields': ['title', 'order', 'is_active'],
    },
    'funfacts': {
        'model': FunFact,
        'label': 'Fun Facts',
        'fields': '__all__',
        'list_fields': ['label', 'number', 'suffix', 'order'],
    },
    'chooseus': {
        'model': ChooseUsSection,
        'label': 'Why Choose Us',
        'fields': '__all__',
        'list_fields': ['heading', 'emergency_phone', 'is_active'],
    },
    'choosepoints': {
        'model': ChooseUsPoint,
        'label': 'Choose Us Points',
        'fields': '__all__',
        'list_fields': ['title', 'section', 'order'],
    },
    'cta': {
        'model': CTASection,
        'label': 'CTA Section',
        'fields': '__all__',
        'list_fields': ['heading', 'is_active'],
    },
    'materials': {
        'model': RecycleMaterial,
        'label': 'Recycle Materials',
        'fields': '__all__',
        'list_fields': ['name', 'order'],
    },
    'testimonials': {
        'model': Testimonial,
        'label': 'Testimonials',
        'fields': '__all__',
        'list_fields': ['name', 'designation', 'rating', 'is_active'],
    },
    'projects': {
        'model': Project,
        'label': 'Projects',
        'fields': '__all__',
        'list_fields': ['title', 'category', 'order', 'is_active'],
    },
    'news': {
        'model': NewsPost,
        'label': 'News Posts',
        'fields': '__all__',
        'list_fields': ['title', 'author', 'post_date', 'is_active'],
    },
}