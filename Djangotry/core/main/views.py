from typing import Any
from django.http import HttpRequest, HttpResponse
from django.shortcuts import render 
from django.views.generic import ListView
from .models import *
from .forms import ContactUsForm




class HommeListView(ListView):
    template_name = 'index.html'


    def get(self, request):

        context = self._extract_all_data()

        return render(request ,self.template_name , context)
     
    @staticmethod
    def _extract_all_data():
        intros = Introduction.objects.all()
        service = Service.objects.get()
        icons = Icon.objects.all()
        our_galleries = OurGallery.objects.all()
        about_us = AboutUs.objects.get()
        homebgs = HomeBG.objects.get()

        context = {
            'intros':intros,
            'service':service,
            'icons':icons,
            'our_galleries':our_galleries,
            'about_us':about_us,
            'homebgs':homebgs,
        }

        return context



    def post(self , request):

        form = ContactUsForm(request.POST)

        context = self._extract_all_data()

        if form.is_valid():
            form.save()
        else:
            form = ContactUsForm()


        context.update({'form':form})

        return render(request ,self.template_name , context)

