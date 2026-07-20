from django.db import models

# ---------- 1. Banner (hero slider) ----------
class HomeBanner(models.Model):
    subtitle = models.CharField(max_length=100, help_text="e.g. Waste Management")
    heading = models.CharField(max_length=200, help_text="e.g. Reliable waste collection across Dhaka")
    description = models.TextField()
    image = models.ImageField(upload_to='banner/')
    button_text = models.CharField(max_length=50, default='Read More')
    button_url = models.CharField(max_length=200, default='/')
    order = models.PositiveIntegerField(default=0)
    is_active = models.BooleanField(default=True)

    class Meta:
        ordering = ['order']
        verbose_name = "Banner Slide"
        verbose_name_plural = "Banner Slides"

    def __str__(self):
        return self.heading


# ---------- 2. Feature blocks (Waste Collection / Recycling / Pickup Schedule) ----------
class Feature(models.Model):
    icon_class = models.CharField(max_length=50, help_text="e.g. icon-8 (from theme font-icons)")
    title = models.CharField(max_length=100)
    description = models.TextField()
    link_url = models.CharField(max_length=200, default='/')
    order = models.PositiveIntegerField(default=0)
    is_active = models.BooleanField(default=True)

    class Meta:
        ordering = ['order']

    def __str__(self):
        return self.title


# ---------- 3. About section (singleton-style, only one active row is used) ----------
class AboutSection(models.Model):
    subtitle = models.CharField(max_length=100, default='About Us')
    heading = models.CharField(max_length=200)
    description = models.TextField()
    list_item_1 = models.CharField(max_length=100, blank=True)
    list_item_2 = models.CharField(max_length=100, blank=True)
    list_item_3 = models.CharField(max_length=100, blank=True)
    button_text = models.CharField(max_length=50, default='Contact Us')
    button_url = models.CharField(max_length=200, default='/')
    image_1 = models.ImageField(upload_to='about/')
    image_2 = models.ImageField(upload_to='about/')
    image_3 = models.ImageField(upload_to='about/')
    is_active = models.BooleanField(default=True)

    class Meta:
        verbose_name = "About Section"
        verbose_name_plural = "About Section"

    def __str__(self):
        return self.heading


# ---------- 4. Service cards ----------
class Service(models.Model):
    image = models.ImageField(upload_to='services/')
    icon_class = models.CharField(max_length=50, help_text="e.g. icon-12")
    title = models.CharField(max_length=100)
    description = models.TextField()
    link_url = models.CharField(max_length=200, default='/')
    order = models.PositiveIntegerField(default=0)
    is_active = models.BooleanField(default=True)

    class Meta:
        ordering = ['order']

    def __str__(self):
        return self.title


# ---------- 5. Fun facts / counters ----------
class FunFact(models.Model):
    icon_class = models.CharField(max_length=50)
    number = models.PositiveIntegerField(help_text="e.g. 20")
    suffix = models.CharField(max_length=10, blank=True, help_text="e.g. k, +, 5k")
    label = models.CharField(max_length=100)
    order = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ['order']

    def __str__(self):
        return self.label


# ---------- 6. "Why Choose Us" section ----------
class ChooseUsSection(models.Model):
    subtitle = models.CharField(max_length=100, default='Why Choose Us')
    heading = models.CharField(max_length=200)
    description = models.TextField()
    image = models.ImageField(upload_to='chooseus/')
    emergency_label = models.CharField(max_length=50, default='For Emergency')
    emergency_phone = models.CharField(max_length=30)
    button_text = models.CharField(max_length=50, default='Contact Us')
    button_url = models.CharField(max_length=200, default='/')
    is_active = models.BooleanField(default=True)

    class Meta:
        verbose_name = "Choose Us Section"
        verbose_name_plural = "Choose Us Section"

    def __str__(self):
        return self.heading


class ChooseUsPoint(models.Model):
    section = models.ForeignKey(ChooseUsSection, related_name='points', on_delete=models.CASCADE)
    icon_class = models.CharField(max_length=50)
    title = models.CharField(max_length=100)
    description = models.TextField()
    order = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ['order']

    def __str__(self):
        return self.title


# ---------- 7. CTA section ----------
class CTASection(models.Model):
    background_image = models.ImageField(upload_to='cta/')
    heading = models.CharField(max_length=200)
    button_1_text = models.CharField(max_length=50, default='Contact Us')
    button_1_url = models.CharField(max_length=200, default='/')
    button_2_text = models.CharField(max_length=50, default='Get a Quotes')
    button_2_url = models.CharField(max_length=200, default='/')
    is_active = models.BooleanField(default=True)

    class Meta:
        verbose_name = "CTA Section"
        verbose_name_plural = "CTA Section"

    def __str__(self):
        return self.heading


# ---------- 8. Recycle materials list ----------
class RecycleMaterial(models.Model):
    name = models.CharField(max_length=100)
    order = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ['order']

    def __str__(self):
        return self.name


# ---------- 9. Testimonials ----------
class Testimonial(models.Model):
    RATING_CHOICES = [(i, i) for i in range(1, 6)]

    client_image = models.ImageField(upload_to='testimonials/')
    name = models.CharField(max_length=100)
    designation = models.CharField(max_length=100)
    rating = models.PositiveSmallIntegerField(choices=RATING_CHOICES, default=5)
    review = models.TextField()
    order = models.PositiveIntegerField(default=0)
    is_active = models.BooleanField(default=True)

    class Meta:
        ordering = ['order']

    def __str__(self):
        return self.name


# ---------- 10. Projects / gallery ----------
class Project(models.Model):
    image = models.ImageField(upload_to='projects/')
    category = models.CharField(max_length=100, default='Waste Pickup')
    title = models.CharField(max_length=100)
    link_url = models.CharField(max_length=200, default='/')
    order = models.PositiveIntegerField(default=0)
    is_active = models.BooleanField(default=True)

    class Meta:
        ordering = ['order']

    def __str__(self):
        return self.title


# ---------- 11. News / blog posts ----------
class NewsPost(models.Model):
    image = models.ImageField(upload_to='news/')
    post_date = models.DateField()
    author = models.CharField(max_length=100, default='Admin')
    comment_count = models.PositiveIntegerField(default=0)
    title = models.CharField(max_length=200)
    excerpt = models.TextField()
    link_url = models.CharField(max_length=200, default='/')
    is_active = models.BooleanField(default=True)

    class Meta:
        ordering = ['-post_date']

    def __str__(self):
        return self.title