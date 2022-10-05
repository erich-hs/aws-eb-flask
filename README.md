[![Python application test with Github Actions](https://github.com/erich-hs/aws-eb-flask/actions/workflows/main.yml/badge.svg)](https://github.com/erich-hs/aws-eb-flask/actions/workflows/main.yml)
<div align="center">

# Flask App Deployment with AWS ElasticBeanstalk

![AWS-EB-Flask](https://user-images.githubusercontent.com/77303576/194011905-240fb936-5960-4d5a-bc80-3a58a4e1d9ba.png)

Template repository for a Continuous Delivery Flask application deployment with AWS ElasticBeanstalk
</div>

---
## GitHub Repository
* Create a GitHub repository and:
    * Add a README.md and a .gitignore file with a Python template
    * Copy your Github SSH link `git@github.com:[your_github_username]/aws-eb-flask.git` under 'Code > Clone > SSH'

## AWS Cloud9 Development Environment Setup
* Initiate an AWS Cloud9 cloud IDE and cd to your environment folder
```bash
$ cd ~/environment/
```
* Install the ElasticBeanstalk CLI from [AWS current setup](https://github.com/aws/aws-elastic-beanstalk-cli-setup)
```
$ git clone https://github.com/aws/aws-elastic-beanstalk-cli-setup.git
$ python ./aws-elastic-beanstalk-cli-setup/scripts/ebcli_installer.py
```
* Ensure `eb` is in `PATH`
```bash
$ echo 'export PATH="/home/ec2-user/.ebcli-virtual-env/executables:$PATH"' >> ~/.bash_profile && source ~/.bash_profile
```
* You can now check your currently installed ElasticBeanstalk CLI and current Python Interpreter
```c
$ eb --version
EB CLI 3.20.3 (Python 3.7.1)
```
---
### For new Cloud9 EC2 instances
* Setup your encripted bi-direction communication with SSH keys
```c
$ ssh-keygen -t rsa
```
It will place your identification and public key on your current home directory
```c
Your identification has been saved in /home/ec2-user/.ssh/id_rsa.
Your public key has been saved in /home/ec2-user/.ssh/id_rsa.pub.
```
* Copy the public key. This is not a secret key and can be stored publicly
```bash
$ cat /home/ec2-user/.ssh/id_rsa.pub
```
* Under your GitHub account set up a new SSH Authentication Key
    * Copy the output key from cat command
    * Under Github Account > Settings > SSH and GPG keys > New SSH key
    * Paste key and name it to identify your Cloud9 EC2 instance
    * Confirm password / authentication
---
### For Cloud9 EC2 instances with existing SSH permissions
* Clone your repository and cd to its root folder
```bash
$ git clone git@github.com:{your_github_username}/aws-eb-flask.git
$ cd aws-eb-flask
```

## Base Project Structure
* Initializie your base project structure with:
    * flask_app.py
    * test_flask_app.py
    * Makefile
    * requirements.txt
```bash
$ touch flask_app.py
$ touch test_flask_app.py
$ touch Makefile
$ touch requirements.txt
```

## Virtual Environment and Basic Dependencies
* Create a Python3 virtual environment and activate it
```bash
$ python3 -m venv venv
$ source venv/bin/activate
(venv) ec2-user:~/environment/aws-eb-flask (main) $
```
* Install the working version of Flask for your application
```c
$ pip install flask==2.0.3
```
* pip freeze your current packages to your requirements.txt file and check its contents.
```c
$ pip freeze > requirements.txt
$ cat requirements.txt
click==8.1.3
Flask==1.0.2
importlib-metadata==5.0.0
itsdangerous==2.1.2
Jinja2==3.1.2
MarkupSafe==2.1.1
typing-extensions==4.3.0
Werkzeug==2.2.2
zipp==3.8.1
```

## Flask Application
* Develop your base Flask Application. A simple running example [flask_app.py](flask_app.py) from this repository.
* You can now run locally and test your `flask_app.py`
```c
$ python flask_app.py
```
* And on another terminal
```bash
$ curl http://127.0.0.1:5000
Continuous Delivery Demo!
$ curl http://127.0.0.1:5000/echo/Erich
{
  "new-name": "Erich"
}
```

## ElasticBeanstalk Environment
Before starting a new EB Environment, make sure that your current `.gitignore` or `.ebignore` file indicates that the EB CLI should ignore your current `.venv` folder when deploying. It will avoid pusshing your local virtual environment to your EB referenced GitHub repository, which would lead to conflicts.

Important: Note that if an `.ebignore` file isn't present, but a `.gitignore` is, the EB CLI ignores files specified in `.gitignore`. If `.ebignore` is present, the EB CLI doesn't read `.gitignore`.
* Initializie your EB project
```c
eb init -p python-3.7 eb-flask-app
Application eb-flask-app has been created.
```
* Create an EB environment
```c
eb create eb-flask-app-env
```
This will set up your complete ElasticBeanstalk Environment within your initialized project with:
* EC2 Instances
* Load Balancer
* Auto Scaling
* CloudWatch Alarm
* Corresponding Security Groups

## GitHub Actions
You can now set your Makefile for GitHub actions. You can find a [sample Makefile](Makefile) in this repository. Remember to update the `eb deploy` command with your app name.

Before running a `make all` make sure to include these extra packages to your requirements.txt according to your Makefile:
```
pylint
pytest
black
pytest-cov
```
* Setup GitHub Actions
   * In your GitHub repository, under Actions, select `set up a workflow yourself`.
   * Configure your main.yml file to make use of your Makefile scripts.
 
Here is a [sample workflow](/.github/workflows/main.yml) for Continuous Develivery with GitHub actions.
