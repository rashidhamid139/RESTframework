from django.shortcuts import render

# Create your views here.
def default_map(request):
    # return render(request, 'maps/default.html', {})
    mapbox_access_token = 'pk.eyJ1IjoicmFzaGlkaGFtaWQxMzkiLCJhIjoiY2s1MmY2ZGhzMDY4cjNrbnRrOG43ajVjOCJ9.PgQPjZuq5sHT2jlwVQRTOw'
    return render(request, 'maps/default.html',  { 'mapbox_access_token': mapbox_access_token })