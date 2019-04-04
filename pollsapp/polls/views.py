from django.http import HttpResponse
from rest_framework.views import APIView
from rest_framework.response import Response
from polls.api import *
from polls.models import *

def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")


class TrackListViewSet(APIView):
    def get(self,request,track_id=None):
        if track_id is not None:
            track_obj_list = Track.objects.get(pk=track_id)
            serializer = TrackListViewSerializer(track_obj_list)
        else:
            track_obj_list = Track.objects.all()        
            serializer = TrackListViewSerializer(track_obj_list ,many=True)
        return Response(serializer.data)
    def post(self,request,track_id=None):
        serializer = TrackListCreateViewSerializer(data=request.data)
        if serializer.is_valid():
            if track_id is not None:
                try:                    
                    track_obj = Track.objects.get(pk=track_id)
                    track_obj.name = request.data['name']
                    track_obj.save()
                    context_data = {"success":True,'message':'Record Updated Successfully'}
                except Track.DoesNotExist as e:
                    context_data = {"success":False,'message':'Record already DoesNotExist'}
            else:
                try:
                    track_obj = Track.objects.get(name=request.data['name'])
                    context_data = {"success":False,'message':'Record already DExist'}
                except Track.DoesNotExist as e:
                    track_obj = Track.objects.create(name=request.data['name'])
                    context_data = {"success":True,'message':'Record Created Successfully'}
        else:            
            context_data = {"success" : False, "errors" : {"message":serializer.errors}}
        return Response(context_data)
class DeleteTrackIDViewSet(APIView):
    def get(self, request, track_id=None):        
        if track_id is not None:
            try:
                track_obj = Track.objects.get(pk=track_id)
                track_obj.delete()
                context_data = {"success":True,'message':'Record deleted Successfully'}
            except Exception as e:
                context_data = {"success":True,'message':'Record does not exist'}
        else:
            context_data = {"success":True,'message':'track id is none'}
        return Response(context_data)

class GetQuestionsByTrackIdViewSet(APIView):
    def get(self,request,track_id=None):
        if track_id is not None:
            question_obj_list = Question.objects.filter(track_name_id = track_id)
            if len(question_obj_list)>0:
                context_data = {"success":True,'data':question_obj_list.values('question_text')}
            else:
                context_data = {"success":False,'message':'{0} Records found'.format(len(question_obj_list))}

        else:
            context_data = {"success":False,'message':'track id is none'}
        return Response(context_data)


class GetTotalCountQuestionStatus(APIView):
    def get(self,request,question_id=None):
        if question_id is not None:
            question_status_list = QuestionAnswer.objects.filter(question_id=question_id)
            correct_answer_list = question_status_list.filter(answer_status='Correct')
            wrong_answer_count = len(question_status_list)-len(correct_answer_list)
            context_data = {"success":True,"data":{"total_correct_answer_count":len(correct_answer_list),"total_wrong_answer_count":wrong_answer_count}}
        else:
            context_data = {"success":False,'message':'question_id is none'}

        return Response(context_data)
