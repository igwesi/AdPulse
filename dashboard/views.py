from django.shortcuts import render
from .models import Campaign

def dashboard_home(request):
    campaigns = Campaign.objects.filter(user=request.user)
    total_spent = sum(c.cost for c in campaigns)
    avg_ctr = 0
    if campaigns.exists():
        avg_ctr = sum(c.ctr for c in campaigns) / campaigns.count()
    return render(request, 'dashboard/index.html', {
        'campaigns': campaigns,
        'total_spent': total_spent,
        'avg_ctr': round(avg_ctr, 2),
    })
