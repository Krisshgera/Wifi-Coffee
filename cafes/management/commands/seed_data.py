from django.core.management.base import BaseCommand
from cafes.models import Cafe, Review


class Command(BaseCommand):
    help = 'Populate the database with sample cafe data'

    def handle(self, *args, **options):
        # Clear existing data
        self.stdout.write('Clearing existing cafes and reviews...')
        Review.objects.all().delete()
        Cafe.objects.all().delete()
        
        # Sample cafes for Jaipur
        jaipur_cafes = [
            {
                'name': 'The Brew Story',
                'city': 'Jaipur',
                'coffee_rating': 4.5,
                'wifi_rating': 4.2,
                'ambiance_rating': 4.7,
                'has_power': True,
                'map_url': 'https://maps.google.com/?q=The+Brew+Story+Jaipur'
            },
            {
                'name': 'Café Coffee Day - MI Road',
                'city': 'Jaipur',
                'coffee_rating': 3.8,
                'wifi_rating': 3.5,
                'ambiance_rating': 3.9,
                'has_power': True,
                'map_url': 'https://maps.google.com/?q=CCD+MI+Road+Jaipur'
            },
            {
                'name': 'Tapri Central',
                'city': 'Jaipur',
                'coffee_rating': 4.0,
                'wifi_rating': 3.8,
                'ambiance_rating': 4.5,
                'has_power': False,
                'map_url': 'https://maps.google.com/?q=Tapri+Central+Jaipur'
            },
            {
                'name': 'Brown Sugar',
                'city': 'Jaipur',
                'coffee_rating': 4.3,
                'wifi_rating': 4.0,
                'ambiance_rating': 4.6,
                'has_power': True,
                'map_url': 'https://maps.google.com/?q=Brown+Sugar+Jaipur'
            }
        ]
        
        # Sample cafes for Delhi
        delhi_cafes = [
            {
                'name': 'Blue Tokai Coffee Roasters',
                'city': 'Delhi',
                'coffee_rating': 4.8,
                'wifi_rating': 4.5,
                'ambiance_rating': 4.7,
                'has_power': True,
                'map_url': 'https://maps.google.com/?q=Blue+Tokai+Coffee+Roasters+Delhi'
            },
            {
                'name': 'Café Turtle',
                'city': 'Delhi',
                'coffee_rating': 4.2,
                'wifi_rating': 3.9,
                'ambiance_rating': 4.4,
                'has_power': True,
                'map_url': 'https://maps.google.com/?q=Cafe+Turtle+Delhi'
            },
            {
                'name': 'Indian Coffee House',
                'city': 'Delhi',
                'coffee_rating': 3.5,
                'wifi_rating': 2.8,
                'ambiance_rating': 4.0,
                'has_power': False,
                'map_url': 'https://maps.google.com/?q=Indian+Coffee+House+Delhi'
            },
            {
                'name': 'Kunzum Travel Café',
                'city': 'Delhi',
                'coffee_rating': 4.0,
                'wifi_rating': 4.3,
                'ambiance_rating': 4.5,
                'has_power': True,
                'map_url': 'https://maps.google.com/?q=Kunzum+Travel+Cafe+Delhi'
            }
        ]
        
        # Sample cafes for Gurgaon
        gurgaon_cafes = [
            {
                'name': 'Starbucks - Cyber Hub',
                'city': 'Gurgaon',
                'coffee_rating': 4.3,
                'wifi_rating': 4.6,
                'ambiance_rating': 4.4,
                'has_power': True,
                'map_url': 'https://maps.google.com/?q=Starbucks+Cyber+Hub+Gurgaon'
            },
            {
                'name': 'The Grammar Room',
                'city': 'Gurgaon',
                'coffee_rating': 4.5,
                'wifi_rating': 4.4,
                'ambiance_rating': 4.8,
                'has_power': True,
                'map_url': 'https://maps.google.com/?q=The+Grammar+Room+Gurgaon'
            },
            {
                'name': 'Café Delhi Heights',
                'city': 'Gurgaon',
                'coffee_rating': 4.0,
                'wifi_rating': 3.7,
                'ambiance_rating': 4.2,
                'has_power': True,
                'map_url': 'https://maps.google.com/?q=Cafe+Delhi+Heights+Gurgaon'
            },
            {
                'name': 'Café Wanderlust',
                'city': 'Gurgaon',
                'coffee_rating': 4.2,
                'wifi_rating': 4.1,
                'ambiance_rating': 4.6,
                'has_power': False,
                'map_url': 'https://maps.google.com/?q=Cafe+Wanderlust+Gurgaon'
            }
        ]
        
        # Combine all cafes
        all_cafes = jaipur_cafes + delhi_cafes + gurgaon_cafes
        
        # Create cafe objects
        created_cafes = []
        for cafe_data in all_cafes:
            cafe = Cafe.objects.create(**cafe_data)
            created_cafes.append(cafe)
            self.stdout.write(
                self.style.SUCCESS(f'Created cafe: {cafe.name} in {cafe.city}')
            )
        
        # Add some sample reviews
        sample_reviews = [
            {
                'cafe': created_cafes[0],  # The Brew Story
                'email': 'john@example.com',
                'text': 'Amazing coffee and great ambiance! Perfect place to work.',
                'agree_count': 15,
                'disagree_count': 2
            },
            {
                'cafe': created_cafes[0],  # The Brew Story
                'email': None,
                'text': 'Love the WiFi speed here. Can work for hours without any issues.',
                'agree_count': 8,
                'disagree_count': 0
            },
            {
                'cafe': created_cafes[4],  # Blue Tokai
                'email': 'sarah@example.com',
                'text': 'Best coffee in Delhi! The pour-over is exceptional.',
                'agree_count': 22,
                'disagree_count': 1
            },
            {
                'cafe': created_cafes[8],  # Starbucks Cyber Hub
                'email': None,
                'text': 'Reliable WiFi and plenty of power outlets. Great for meetings.',
                'agree_count': 12,
                'disagree_count': 3
            },
        ]
        
        for review_data in sample_reviews:
            review = Review.objects.create(**review_data)
            reviewer = review_data['email'] if review_data['email'] else 'Anonymous'
            self.stdout.write(
                self.style.SUCCESS(f'Created review by {reviewer} for {review_data["cafe"].name}')
            )
        
        self.stdout.write(
            self.style.SUCCESS(
                f'\nSuccessfully created {len(created_cafes)} cafes and {len(sample_reviews)} reviews!'
            )
        )
