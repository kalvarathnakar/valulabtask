from django.core.management.base import BaseCommand
from django.utils import timezone
import random
from polls.models import *

class Command(BaseCommand):
    help = 'Displays current time'

    def handle(self, *args, **kwargs):
        time = timezone.now().strftime('%X')
        self.stdout.write("It's now %s" % time)
        track_names =['EAMCET','AIEEE','IIT']
        question_names = ['what is your age?','what is your branch?','what is your college name?','what is your percentage?']
        # create track names
        for each in track_names:
            try:
                track_obj = Track.objects.get(name=each)
            except Track.DoesNotExist as e:
                track_obj = Track.objects.create(name=each)
        track_obj_list = Track.objects.all()
        # cretae question names
        for each_q in question_names:
            track_id = random.choice(track_obj_list).id
            try:
                question_obj = Question.objects.get(question_text=each_q,track_name_id = track_id)
            except Exception as e:
                question_obj = Question.objects.create(question_text=each_q,track_name_id=track_id)
        question_obj_list = Question.objects.all()
        #create question choice with answer status correct or wrong
        q1_choice = ['15','17','>18','21']
        answer_status_list = ['Correct','Wrong']
        q2_choice = ['MPC','BIPC','CEC','HEC']
        q3_choice = ['college1','college2','college3','college4']
        q4_chocice = ['35','>35','<35']
        question_choice_list ={
        "1" : ['15','17','>18','21'],        
        "2" : ['MPC','BIPC','CEC','HEC'],
        "3" : ['college1','college2','college3','college4'],
        "4" :['35','>35','<35']
        }
        for each in question_obj_list:
            for choice in question_choice_list:
                count=1
                for choice_text in question_choice_list[str(each.id)]:
                    if count ==1:                                   
                        try:
                            question_choice_obj = Choice.objects.get(question_id=each.id,choice_text=choice_text,answer_status='Correct')
                        except Exception as e:
                            question_choice_obj = Choice.objects.create(question_id=each.id,choice_text=choice_text,answer_status='Correct')
                        count =0
                    else:
                        try:
                            question_choice_obj = Choice.objects.get(question_id=each.id,choice_text=choice_text,answer_status='Wrong')
                        except Exception as e:
                            question_choice_obj = Choice.objects.create(question_id=each.id,choice_text=choice_text,answer_status='Wrong')
                        
        question_choice_obj_list = Choice.objects.all()
        for i in range(10):
            choice_obj = random.choice(question_choice_obj_list)

            question_answer = QuestionAnswer.objects.create(question_id=choice_obj.question.id,answer_status=choice_obj.answer_status)



