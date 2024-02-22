

# Configure

  `pip3 freeze > requirements.txt`

# Run



1. navigate to /backend

2. run:

  `uvicorn main:app --reload --host 0.0.0.0 --port 8080`

3. use "reload" flag only for development

4. find swagger docs here:

   [http://127.0.0.1:8080/docs](https://www.chefmaezaki.com/)
5. set schema for username

  `ALTER ROLE postgres IN DATABASE readmission SET search_path TO demo;`

6. Update .env file with JWT password.  You can use utils/secret_gen to create new secrets

7. Load demo data by calling this URL with "post" from Postman:

  http://localhost:8080/api/testing/data/create


