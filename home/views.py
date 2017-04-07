from django.views.generic.base import TemplateView


class HomeView(TemplateView):
    template_name = 'home.html'


class AboutView(TemplateView):
    template_name = 'about.html'


class ShowcaseView(TemplateView):
    template_name = 'showcase.html'


class GetStartedView(TemplateView):
    template_name = 'getStarted.html'


class EventsView(TemplateView):
    template_name = 'events.html'


class SponsorsView(TemplateView):
    template_name = 'sponsors.html'


class CommunityView(TemplateView):
    template_name = 'community.html'


class TripsView(TemplateView):
    template_name = 'trips.html'


class ProjectsView(TemplateView):
    template_name = 'projects.html'


class ProductsView(TemplateView):
    template_name = 'products.html'

class LinksView(TemplateView):
    template_name = 'links.html'

class ChangelogsView(TemplateView):
    template_name = 'logs.html'



