from django.views.generic import TemplateView


# class Homepage(APIView):
#     http_method_names = ['get', 'put', 'patch', 'delete', 'head', 'options', 'trace']
#
#     def get(self, request):
#         return render(
#             request,
#             'base_generic.html',
#         )


# class HomePageView(TemplateView):
#
#     template_name = "base_generic.html"
#
#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         return context
