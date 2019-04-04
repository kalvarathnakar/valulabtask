Deploying Steps
```
1)Python manage.py makemigrations
2)python mangage.py migrate
3)python manage.py insert_test_data
4)python manage.py runserver 8001
```
```
1) Get Track List:

 
  URL:http://localhost:8001/polls/tracklist
  method:GET
 Response:
	[
    {
        "id": 1,
        "name": "EAMCET"
    },
    {
        "id": 2,
        "name": "AIEEE"
    },
    {
        "id": 3,
        "name": "IIT"
    }
]
```
```
2)Create Track:
 
 URL: http://localhost:8001/polls/tracklist/add
 params ={"name":"<track_name>"}
 method:POST
 
 Response:
	{
    "success": true,
    "message": "Record Created Successfully"
	}
```
```
3) Edit Track 
 URL:http://localhost:8001/polls/tracklist/edit/<track_id>/
 params ={"name":"<track_name>"}
 method :POST
 Response:{
    "success": true,
    "message": "Record Updated Successfully"
}
```
```
4)Get Questions By Track ID
 URL:http://localhost:8001/polls/questions/<track_id>/
 method:GET
 Response:
 {
    "success": true,
    "data": [
        {
            "question_text": "what is your age?"
        },
        {
            "question_text": "what is your college name?"
        },
        {
            "question_text": "what is your percentage?"
        }
    ]
}
```
```
5)Get Total Count of correct and Wrong answer of Question ID
  URL:http://localhost:8001/polls/question/answer_status_count/<question_id>/
  method:GET
  Response:
  {
    "success": true,
    "data": {
        "total_wrong_answer_count": 4,
        "total_correct_answer_count": 1
    }
}
```
  
 	
  
