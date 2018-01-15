# intouchapp_be

1. I have used python 3.6, django 2.0 and mongodb 3.6 for creating the application potentail merge candidates

2. I have created a project in django as intouchapp_be and created a app as MergeCandiadtes in intouchapp_be project

3. Merge Candidates have python files like url.py which is used for routing, controller.py which is used for fetching the request data
and pass it to the blmanager.py and sending response data to the client, blmanager.py is responsible for managing the business logic of the app
and finally the dbmanager.py which handles connection and querying data from the database.

4. I have hosted mongodb on mlab which provide mongodb as a service

5. Go to the project directory and start the server by running "python manage.py runserver 8000" in cmd or terminal

6. I have created four APIs which are listed below:-

    a.  URL: http://127.0.0.1:8000/api/save-user
        REQUEST_TYPE: POST
        REQUEST:
        {
	        "firstName":"ayush",
	        "lastName": "chauhan",
	        "email": "imayushchauhan@gmail.com",
	        "phoneNumber": 9968439442
        }
        RESPONSEE:
        {"responseData": null, "message": "user added successfully", "code": 200}

    b.  URL: http://127.0.0.1:8000/api/update-user
        REQUEST_TYPE: POST
        REQUEST:
        {
	        "_id": "26qm0pu1ghuiz40ut0tq7kyl",
	        "firstName": "nishant",
	        "lastName": "srivastava",
	        "email": "imnishantsrivastava@gmail.com",
	        "phoneNumber": 9968439442,
	        "contactList": {
		        "c1": [{
			        "type": "email",
			        "value": "e1"
		        }, {
			        "type": "phone",
			        "value": "p1"
		        }],
		        "c2": [{
			        "type": "email",
			        "value": "e2"
		        }, {
			        "type": "phone",
			        "value": "p2"
		        }],
		        "c3": [{
			        "type": "email",
			        "value": "e3"
		        }, {
			        "type": "phone",
			        "value": "p2"
		        }],
		        "c4": [{
			        "type": "email",
			        "value": "e3"
		        }, {
			        "type": "phone",
			        "value": "p4"
		        }],
		        "c5": [{
			        "type": "email",
			        "value": "e2"
		        }, {
			        "type": "phone",
			        "value": "p5"
		        }],
		        "c6": [{
			        "type": "phone",
			        "value": "p3"
		        }, {
			        "type": "email",
			        "value": "e4"
		        }, {
			        "type": "phone",
			        "value": "p6"
		        }],
		        "c7": [{
			        "type": "email",
			        "value": "e4"
		        }],
		        "c8": [{
			        "type": "phone",
			        "value": "p6"
		        }, {
			        "type": "email",
			        "value": "e5"
		        }]
	        }
        }
        RESPONSEE:
        {"responseData": null, "message": "user updated successfully", "code": 200}

    c.  URL: http://127.0.0.1:8000/api/get-user-list
        REQUEST_TYPE: POST
        REQUEST:
        {}
        RESPONSEE:
        {"responseData": [{"_id": "13kzr3zfw378idv7aok69qg4", "firstName": "ayush", "lastName": "chauhan", "email": "imayushchauhan@gmail.com", "phoneNumber": 9968439442, "contactList": [{"c1": [{"type": "email", "value": "e1"}, {"type": "phone", "value": "p1"}]}, {"c2": [{"type": "email", "value": "e2"}, {"type": "phone", "value": "p2"}]}, {"c3": [{"type": "email", "value": "e3"}, {"type": "phone", "value": "p2"}]}, {"c4": [{"type": "email", "value": "e3"}, {"type": "phone", "value": "p4"}]}]}], "message": "user list fetched successfully", "code": 200}

    d. URL: http://127.0.0.1:8000/api/get-potential-merge-candidates
        REQUEST_TYPE: POST
        REQUEST:
        {
	        "userID": "13kzr3zfw378idv7aok69qg4"
        }
        RESPONSEE:
        {"responseData": [["c1"], ["c2", "c3", "c4", "c5"], ["c6", "c7", "c8"]], "message": "potential merge candidates fetched successfully", "code": 200}