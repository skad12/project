from django.shortcuts import render, get_object_or_404

from django.utils import timezone
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse, reverse_lazy

from django.core.mail import send_mail
from django.conf import settings


#########################main shit starts here ###########################

def IndexView(request):

	if request.method == "POST":
		amount = request.POST.get("amount")
		pub_date = timezone.now()	
		donation = Donation.objects.create(amount=amount, pub_date=pub_date)
		donation.save()
		return HttpResponseRedirect(reverse("donation", args=(donation.id,)))
		
	else:
		return render(request, 'sammy/index.html')
		
	