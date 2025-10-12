from django.shortcuts import render
from .models import GeneratedCopy
from .services import generate_ad_copy

def generator_view(request):
    if request.method == 'POST':
        product_name = request.POST.get('product_name')
        audience = request.POST.get('audience')
        tone = request.POST.get('tone')
        output = generate_ad_copy(product_name, audience, tone)
        GeneratedCopy.objects.create(
            user=request.user, product_name=product_name,
            audience=audience, tone=tone, output=output
        )
        return render(request, 'generator/generator_results.html', {'output': output})
    return render(request, 'generator/generator_form.html')
