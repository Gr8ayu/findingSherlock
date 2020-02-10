from django.urls import path

from . import views

urlpatterns = [
	# (? url(r'^departments/(?P<pk>[0-9]+)/$', views.BranchDetail.as_view(), name="branchDetail"))
    # path('(?P<pk>[0-9]+)/$/', views.index, name='level1'),
    path('message/', views.message, name="message"),
    path('1/', views.level1, name='level1'),
    path('2/', views.level2, name='level2'),
    path('3/', views.level3, name='level3'),
    path('4/', views.level4, name='level4'),
    path('5/', views.level5, name='level5'),
    # TODO
    path('6/', views.level6, name='level6'),
    # TODO
    path('7/', views.level7, name='level7'),
    # TODO
    path('8/', views.level8, name='level8'),
    # TODO
    path('9/', views.level9, name='level9'),
    # TODO
    path('10/', views.level10, name='level10'),

    path('11/', views.level11, name='level11'),

    # path('submit/',views.submit, name='submit'),
    path('leaderboard/', views.leaderboard, name='leaderboard'),
    path('submissions/', views.submissions, name='submissions'),
]