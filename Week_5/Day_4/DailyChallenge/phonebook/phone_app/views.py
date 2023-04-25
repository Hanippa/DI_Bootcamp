from django.shortcuts import render
from .models import Person
from phone_app.forms import onefourForm


def search(model, value):

    result = None
    try:
        model_instance = model.objects.get(name = value)
        result = model_instance
    except model.DoesNotExist:
        pass
    try:
        model_instance = model.objects.get(phone_number = value)
        result = model_instance
    except model.DoesNotExist:
        pass

    return result


def search_person(request, search_value: str):

    context = {}

    person_info = search(Person,  search_value)

    if person_info is not None:
        context = {'person': person_info}

    return render(request, 'person_info.html', context)


def profile_view(request, search_value: str):

    context = {}

    person_info = search(Person,  search_value)

    if person_info is not None:
        person_profile = person_info.profile
        
        profile_languages = person_profile.languages.all().order_by('name')

        context = {'person_info': person_info, 'person_profile': person_profile, 'languages': profile_languages}

    return render(request, 'profile.html', context)

def home(request):
    if request.method == "POST":
        form = onefourForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, "todos.html")
    else:
        form = onefourForm()
    return render(request, "home.html", {"form": form})








# def search(model, field: str, value: str):

#     result = None
#     try:
#         x = field
#         res = "%s = %s " % (x, value)

#         print("RES", res)
#         model_instance = model.objects.get("%s = %s " % (x, value))
#         result = model_instance
#     except model.DoesNotExist:
#         pass

#     return result