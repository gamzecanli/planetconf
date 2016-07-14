import datetime
from django.shortcuts import render
from planetconf import settings

from .forms import *
from django.http import HttpResponse


def configuration(request):
    if request.method=="POST":
        planet_form = PlanetForm(request.POST, prefix="planetform")
        blogger_form = BloggerForm(request.POST, prefix="bloggerform")
        if all([planet_form.is_valid(), blogger_form.is_valid()]):
            Planet.objects.all().delete()
            Blogger.objects.all().delete()
            planet = planet_form.save()
            blogger = blogger_form.save()

            planet_conf = settings.planet_conf_template
            planet_conf = planet_conf.replace("##planet_name##", planet.planet_name)
            planet_conf = planet_conf.replace("##link##", planet.link)
            planet_conf = planet_conf.replace("##planet_directory_name##", planet.planet_directory_name)
            planet_conf = planet_conf.replace("##blogger_name##", blogger.blogger_name)
            planet_conf = planet_conf.replace("##blogger_link##", blogger.blogger_link)
            print planet_conf

            with open("planetconf.txt", "w") as file:
                file.write(planet_conf)

    planet_instance = Planet.objects.all()
    blogger_instance = Blogger.objects.all()

    if len(planet_instance) > 0:
        planet_form = PlanetForm(prefix="planetform", instance=planet_instance[0])
    else:
       planet_form = PlanetForm(prefix="planetform")

    if len(blogger_instance) > 0:
        blogger_form = BloggerForm(prefix="bloggerform", instance=blogger_instance[0])
    else:
        blogger_form = BloggerForm(prefix="bloggerform")

    return render(request, "planet/configuration.html", {'planet_form': planet_form, 'blogger_form':blogger_form})

