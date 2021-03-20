# UCLA Toxic Course Combination Survey. 


## Get Started!  

1. Make sure you are using the same version of python as me for best results.
<code>python --version</code> 
Python 3.7.4


2. Clone the repository
<code>git clone https://github.com/oyavuzjr/UCLA-Toxic-Combo</code>

3. Download the requirements.
<code>pip -r requirements.txt</code> 

4. Initialize the Database
<code>python manage.py makemigrations</code>
<code>python manage.py migrate</code>

5. Create a super user to be able to log into the admin interface.
<code>python manage.py createsuperuser</code>

6. Now we are ready to start adding questions to our survey.  Let’s run the server.
<code>python manage.py runserver</code> 

7. Visit localhost:8000/admin and modify the “surveys” page.
The answers that students give will be collected in the sets of answers page.
