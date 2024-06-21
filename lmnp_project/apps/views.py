from django.views.generic import TemplateView


class PreviewConfig(TemplateView):
    template_name = "preview_config.html"

    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)
        return ctx
