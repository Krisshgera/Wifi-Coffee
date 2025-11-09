from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from django.conf import settings
from django.db.models import Q
from .models import Cafe, Review


def homepage(request):
    """Homepage with city selection and cafe list."""
    selected_city = request.GET.get('city', 'Jaipur')
    search_query = request.GET.get('search', '')
    sort_by = request.GET.get('sort', 'name')
    
    # Filter cafes by city
    cafes = Cafe.objects.filter(city=selected_city)
    
    # Apply search filter if provided
    if search_query:
        cafes = cafes.filter(Q(name__icontains=search_query))
    
    # Sort cafes
    if sort_by == 'rating':
        cafes = sorted(cafes, key=lambda x: x.average_rating, reverse=True)
    else:
        cafes = cafes.order_by('name')
    
    cities = ['Jaipur', 'Delhi', 'Gurgaon']
    
    context = {
        'cafes': cafes,
        'cities': cities,
        'selected_city': selected_city,
        'search_query': search_query,
        'sort_by': sort_by,
    }
    return render(request, 'cafes/homepage.html', context)


def cafe_detail(request, cafe_id):
    """Cafe details page with reviews and review form."""
    cafe = get_object_or_404(Cafe, pk=cafe_id)
    
    if request.method == 'POST':
        # Handle review submission
        review_text = request.POST.get('review_text', '').strip()
        email = request.POST.get('email', '').strip()
        
        if review_text:
            Review.objects.create(
                cafe=cafe,
                text=review_text,
                email=email if email else None
            )
            messages.success(request, 'Your review has been submitted successfully!')
            return redirect('cafe_detail', cafe_id=cafe.id)
        else:
            messages.error(request, 'Please enter a review.')
    
    reviews = cafe.reviews.all()
    
    context = {
        'cafe': cafe,
        'reviews': reviews,
    }
    return render(request, 'cafes/cafe_detail.html', context)


def review_vote(request, review_id, vote_type):
    """Handle agree/disagree votes on reviews."""
    review = get_object_or_404(Review, pk=review_id)
    
    if vote_type == 'agree':
        review.agree_count += 1
    elif vote_type == 'disagree':
        review.disagree_count += 1
    
    review.save()
    
    return redirect('cafe_detail', cafe_id=review.cafe.id)


def edit_page(request):
    """Secret key protected edit page for CRUD operations."""
    # Check if the secret key is provided and matches
    secret_key = request.GET.get('key', '')
    
    if secret_key != settings.ADMIN_SECRET_KEY:
        messages.error(request, 'Invalid access key. Access denied.')
        return redirect('homepage')
    
    cafes = Cafe.objects.all().order_by('city', 'name')
    
    context = {
        'cafes': cafes,
        'secret_key': secret_key,
    }
    return render(request, 'cafes/edit.html', context)


def add_cafe(request):
    """Add a new cafe."""
    secret_key = request.GET.get('key', '')
    
    if secret_key != settings.ADMIN_SECRET_KEY:
        messages.error(request, 'Invalid access key. Access denied.')
        return redirect('homepage')
    
    if request.method == 'POST':
        name = request.POST.get('name', '').strip()
        city = request.POST.get('city', '')
        coffee_rating = request.POST.get('coffee_rating', 0)
        wifi_rating = request.POST.get('wifi_rating', 0)
        ambiance_rating = request.POST.get('ambiance_rating', 0)
        has_power = request.POST.get('has_power', 'off') == 'on'
        map_url = request.POST.get('map_url', '').strip()
        
        if name and city and map_url:
            try:
                Cafe.objects.create(
                    name=name,
                    city=city,
                    coffee_rating=float(coffee_rating),
                    wifi_rating=float(wifi_rating),
                    ambiance_rating=float(ambiance_rating),
                    has_power=has_power,
                    map_url=map_url
                )
                messages.success(request, f'Cafe "{name}" has been added successfully!')
            except Exception as e:
                messages.error(request, f'Error adding cafe: {str(e)}')
        else:
            messages.error(request, 'Please fill in all required fields.')
        
        return redirect(f'/edit/?key={secret_key}')
    
    return redirect(f'/edit/?key={secret_key}')


def edit_cafe(request, cafe_id):
    """Edit an existing cafe."""
    secret_key = request.GET.get('key', '')
    
    if secret_key != settings.ADMIN_SECRET_KEY:
        messages.error(request, 'Invalid access key. Access denied.')
        return redirect('homepage')
    
    cafe = get_object_or_404(Cafe, pk=cafe_id)
    
    if request.method == 'POST':
        cafe.name = request.POST.get('name', '').strip()
        cafe.city = request.POST.get('city', '')
        cafe.coffee_rating = float(request.POST.get('coffee_rating', 0))
        cafe.wifi_rating = float(request.POST.get('wifi_rating', 0))
        cafe.ambiance_rating = float(request.POST.get('ambiance_rating', 0))
        cafe.has_power = request.POST.get('has_power', 'off') == 'on'
        cafe.map_url = request.POST.get('map_url', '').strip()
        
        try:
            cafe.save()
            messages.success(request, f'Cafe "{cafe.name}" has been updated successfully!')
        except Exception as e:
            messages.error(request, f'Error updating cafe: {str(e)}')
        
        return redirect(f'/edit/?key={secret_key}')
    
    return redirect(f'/edit/?key={secret_key}')


def delete_cafe(request, cafe_id):
    """Delete a cafe."""
    secret_key = request.GET.get('key', '')
    
    if secret_key != settings.ADMIN_SECRET_KEY:
        messages.error(request, 'Invalid access key. Access denied.')
        return redirect('homepage')
    
    cafe = get_object_or_404(Cafe, pk=cafe_id)
    cafe_name = cafe.name
    
    try:
        cafe.delete()
        messages.success(request, f'Cafe "{cafe_name}" has been deleted successfully!')
    except Exception as e:
        messages.error(request, f'Error deleting cafe: {str(e)}')
    
    return redirect(f'/edit/?key={secret_key}')
