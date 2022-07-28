## Exercie
	* >>> - Create your xware-bootcamp repository on Github.
	* >>> - Clone xware-bootcamp repo to your Desktop.
	* >>> - Create a new folder week1 using command line mkdir.
	* >>> - Create new file inside week1 called README.md using touch.
	* >>> - Add this line # Hello World From My New Shiny Repository xware-bootcamp to the file README.md using echo "" > README.md
	* >>> - add the folder week1 to the staging.
	* >>> - Commit the staged files.
	* >>> - See your tracking status using git status to make sure all files are committed.
	* >>> - Push your changes to Gitlab using git push.






=================================================================================================================================================
## Solution



### Create your xware-bootcamp repository on Github.


* >>> - In the upper-right corner of any page, use the + drop-down menu, and select New repository.
* >>> - Type a short, memorable name for your repository. For example, "xware-bootcamp".
* >>> - Optionally, add a description of your repository. For example, "My first repository on GitHub."
* >>> - Choose a repository visibility.
* >>> - Select Initialize this repository with a README.
* >>> - Click Create repository.




### Clone xware-bootcamp repo to your Desktop.


* >>> - On GitHub.com, navigate to the main page of the repository.
* >>> - Above the list of files, click Code.
* >>> - Copy the URL for the repository.
	* To clone the repository using HTTPS, under "HTTPS", click copy
	* To clone the repository using an SSH key, including a certificate issued by your organization's SSH certificate authority, click SSH, then click.
	* To clone a repository using GitHub CLI, click GitHub CLI, then click.

* >>> - Open Terminal.
* >>> - Change the current working directory to the location where you want the cloned directory.
* >>> - Type git clone, and then paste the URL you copied earlier.
	`$ git clone https://github.com/YOUR-USERNAME/YOUR-REPOSITORY`
* >>> - Press Enter to create your local clone. 
	
```
	$ git clone https://github.com/YOUR-USERNAME/YOUR-REPOSITORY
	> Cloning into xware-bootcamp...
	> remote: Counting objects: 10, done.
	> remote: Compressing objects: 100% (8/8), done.
	> remove: Total 10 (delta 1), reused 10 (delta 1)
	> Unpacking objects: 100% (10/10), done.
```

====================================================================================================================================================
## Create a new folder week1 using command line mkdir.

* Open the terminal application in Linux
* The mkdir command is is used to create new directories or folders.
* Say you need to create a folder name week1 in Linux, type:
	`mkdir week1`



====================================================================================================================================================
## Create new file inside week1 called README.md using touch.

* `touch Readme.md`


====================================================================================================================================================
## Add this line # Hello World From My New Shiny Repository xware-bootcamp to the file README.md using echo "" > README.md
* `echo "Hello World From My New Shiny Repository xware-bootcamp" > README.md`



====================================================================================================================================================
## add the folder week1 to the staging.
* `git add .`


====================================================================================================================================================
## Commit the staged files.
* `git commit -m ""`

====================================================================================================================================================
## See your tracking status using git status to make sure all files are committed.
* `git status`

====================================================================================================================================================
## Push your changes to Gitlab using git push.
* `git push <remote> <branch>`



























