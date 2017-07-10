from . import views

urlpatterns = [
    url(
        regex=r'^$',
        view=views.LocationsListView.as_view(),
        name='locations'
    ),
    url(
        regex=r'^(?P<username>[\w.@+-]+)/$',
        view=views.UserDetailView.as_view(),
        name='detail'
    ),
    url(
        regex=r'^~update/$',
        view=views.LocationUpdateView.as_view(),
        name='update'
    ),
]
