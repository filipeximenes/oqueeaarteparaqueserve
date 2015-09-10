
from django.core.urlresolvers import reverse
from django.shortcuts import redirect
from django.views import generic

from .models import What


class WhatArtIs(generic.DetailView):
    model = What
    template_name = 'art_is.html'

    def get(self, request, **kwargs):
        try:
            self.object = self.get_object()
        except:
            return redirect(reverse('what-is-it-for'))

        context = self.get_context_data(object=self.object)
        return self.render_to_response(context)

    def post(self, request, **kwargs):
        what_is = request.POST.get('what_is', None)
        if what_is:
            try:
                what = What.objects.create(art_is=what_is)
            except:
                return redirect(reverse('what-is-it-for'))
            else:
                return redirect(reverse('what-art-is', kwargs={'pk': what.id}))

        return redirect(reverse('what-is-it-for'))


class WhatIsItFor(generic.RedirectView):
    permanent = False

    def get_redirect_url(self, *args, **kwargs):
        what = What.objects.order_by('?').first()
        return reverse('what-art-is', kwargs={'pk': what.id})
