import json
from django.shortcuts import render
from django.http import JsonResponse, HttpResponseServerError
from django.views import View
from .models import PartnerPreferences, StudentPartnerPreferences, StudentUser
from django.views.decorators.csrf import ensure_csrf_cookie
from django.utils.decorators import method_decorator

class StudentPartnerPreferencesReorder(View):
    template_name = "student_partner_preference_reorder.tmpl"


# Ensure we have a CSRF cooke set
    @method_decorator(ensure_csrf_cookie)
    def get(self, request, pk):
        return render(self.request, self.template_name, 
        {'pk': pk, 'partnerpreferences': PartnerPreferences.objects.filter(studentpartnerpreferences__studentuser_id=pk)
        .order_by('studentpartnerpreferences__order'), 'studentuser': StudentUser.objects.get(id=pk)})

 # Process POST AJAX Request
    def post(self, request, pk):
        if request.method == "POST" and request.is_ajax():
            try:
                # Parse the JSON payload
                data = json.loads(request.body)[0]
                # Loop over our list order. The id equals the question id. Update the order and save
                for idx,partnerpreferences in enumerate(data):
                    spp = StudentPartnerPreferences.objects.get(studentuser=pk, partnerpreferences=partnerpreferences['id']) 
                    spp.order = idx + 1
                    spp.save()

            except KeyError:
                HttpResponseServerError("Malformed data!")

            return JsonResponse({"success": True}, status=200)
        else:
            return JsonResponse({"success": False}, status=400)
