from django.shortcuts import render, redirect, get_object_or_404
from .models import Subscriber, Campaign
from django.contrib import messages
from .tasks import send_email

def add_subscriber(request):
    if request.method == 'POST':
        email = request.POST['email']
        first_name = request.POST['first_name']
        subscriber, created = Subscriber.objects.get_or_create(email=email, defaults={'first_name': first_name})
        if created:
            messages.success(request, f'Subscribed successfully: {email}')
        else:
            messages.info(request, f'Already subscribed: {email}')
    return render(request, 'campaign/add_subscriber.html')

def unsubscribe(request, email):
    try:
        subscriber = Subscriber.objects.get(email=email)
        subscriber.is_active = False
        subscriber.save()
        messages.success(request, f'Unsubscribed successfully: {email}')
    except Subscriber.DoesNotExist:
        messages.error(request, f'Subscriber not found: {email}')
    return redirect('add_subscriber')

def send_campaign(request, campaign_id):
    campaign = get_object_or_404(Campaign, pk=campaign_id)
    
    recipients = Subscriber.objects.filter(is_active=True).values_list('email', flat=True)
    
    for recipient in recipients:
        send_email.delay(
            subject=campaign.subject,
            message=campaign.plain_text_content,
            from_email='your@email.com',
            recipient_list=[recipient],
        )
    
    messages.success(request, f'Campaign is being sent to {len(recipients)} subscribers in the background.')
    return render(request, 'campaign/sent_campaign.html', {'campaign': campaign})



