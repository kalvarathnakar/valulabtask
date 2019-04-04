from django.urls import path
from pollsapp import routers

from . import views
from . import api
from polls.views import *

router = routers.DefaultRouter()
router.register(r'questions', api.QuesViewSet)
router.register(r'choices', api.ChoiceViewSet)

urlpatterns = [
    path('', views.index, name='index'),
   	path('tracklist', TrackListViewSet.as_view(),name='tracklist'),
    path('tracklist/add', TrackListViewSet.as_view(),name='create_track'),
    path('tracklist/edit/<int:track_id>/', TrackListViewSet.as_view(),name='update_track'),
    path('questions/<int:track_id>/', GetQuestionsByTrackIdViewSet.as_view(),name='update_track'),
    path('question/answer_status_count/<int:question_id>/', GetTotalCountQuestionStatus.as_view(),name='question_answer_status_count')
]
