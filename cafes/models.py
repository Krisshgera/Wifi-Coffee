from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator


class Cafe(models.Model):
    """Model representing a cafe with ratings and location information."""
    
    CITY_CHOICES = [
        ('Jaipur', 'Jaipur'),
        ('Delhi', 'Delhi'),
        ('Gurgaon', 'Gurgaon'),
    ]
    
    name = models.CharField(max_length=200)
    city = models.CharField(max_length=50, choices=CITY_CHOICES)
    coffee_rating = models.FloatField(
        validators=[MinValueValidator(0.0), MaxValueValidator(5.0)],
        help_text="Coffee rating out of 5"
    )
    wifi_rating = models.FloatField(
        validators=[MinValueValidator(0.0), MaxValueValidator(5.0)],
        help_text="WiFi rating out of 5"
    )
    ambiance_rating = models.FloatField(
        validators=[MinValueValidator(0.0), MaxValueValidator(5.0)],
        help_text="Ambiance rating out of 5"
    )
    has_power = models.BooleanField(default=False, help_text="Power socket available")
    map_url = models.URLField(max_length=500, help_text="Google Maps link")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        ordering = ['city', 'name']
        verbose_name = 'Cafe'
        verbose_name_plural = 'Cafes'
    
    def __str__(self):
        return f"{self.name} ({self.city})"
    
    @property
    def average_rating(self):
        """Calculate the average rating across all categories."""
        return (self.coffee_rating + self.wifi_rating + self.ambiance_rating) / 3


class Review(models.Model):
    """Model representing a review for a cafe."""
    
    cafe = models.ForeignKey(Cafe, on_delete=models.CASCADE, related_name='reviews')
    email = models.EmailField(blank=True, null=True, help_text="Optional email address")
    text = models.TextField(help_text="Review text")
    agree_count = models.PositiveIntegerField(default=0)
    disagree_count = models.PositiveIntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        ordering = ['-created_at']
        verbose_name = 'Review'
        verbose_name_plural = 'Reviews'
    
    def __str__(self):
        reviewer = self.email if self.email else "Anonymous"
        return f"Review by {reviewer} for {self.cafe.name}"
