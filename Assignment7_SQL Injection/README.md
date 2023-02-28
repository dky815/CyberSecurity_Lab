## SQL Injection

In this assignment, you will get familiar with SQL Injection attacks and tools. SQL injection is one the most common and dangerous web hacking techniques targeting database systems in which malicious SQL statements are injected to exploit unfiltered entry fields. This type of attack is used to gain information from databases, create new entries or even delete a table and so on.

## Setup

You will be given a server and a client both written in JavaScript. The server is using SQLite to store its data and is susceptible to SQL Injection. The server listens to port 8084 and has many endpoints susceptible to SQL injection.

To run the backend and frontend in Kali perform the following steps:

* Download the backend (server) and frontend (client) code from [here](https://canvas.sfu.ca/courses/71722/files/20231018?wrap=1 "sql-injection.zip")[ **Download here**](https://canvas.sfu.ca/courses/71722/files/20231018/download?download_frd=1)and unzip it.

To bring up the backend and frontend, we'll use docker-compose as done in Assignment 6.

**Using docker-compose up**

* Install docker and docker-compose (If not already installed)
* Go to the sql-injection directory with docker-compose.yml file and run `docker compose up`
* This will create the environment and bring up the backend and frontend on ports 8084 and 3000 respectively.
* If you make changes to the code, you need to do a `docker compose build` to rebuild the images and then run `docker compose up` to run the new version.

After one of these steps, visit [http://localhost:3000![]()Links to an external site.](http://localhost:3000/) and you should be able to see the website.

### sqlmap

In this set of tasks you are going to use a tool called `sqlmap`. sqlmap is an open source penetration testing tool that automates the process of detecting and exploiting SQL injection vulnerabilities.

In order to run sqlmap open a console in Kali and type:

```
sqlmap -u http://<vulnerable-website>/<vulnerable endpoint>
```

The server running at `http://localhost:8084` has a vulnerable endpoint at `/vulnerable`. You can visit the endpoint by opening a web browser in Kali and entering `http://localhost:8084/vulnerable?q=user`. You should see the username `user`. This endpoint takes a username as a query parameter and returns it if it exists in the database.

**Task 1 (15%)** : Using `sqlmap` list all the tables in the database by exploiting the vulnerable endpoint `/vulnerable`. What command did you use? What are the tables you found?

**Task 2 (10%)** : Using `sqlmap` list all the usernames and passwords you found in the tables. What command did you use?

### SQL injection

In the following set of tasks you are going to perform SQL injection without using `sqlmap`. Please do not use `sqlmap` for any of the tasks below.

**Task 3 (5%)** : In the home page of the provided website click Login User and try to gain access to the webpage using SQL injection ( **The User panel should show the data for this to be a valid submission)** . Report what you did.

*Hint* : `user` is a sample username for website users, and `admin` is the username of website admin.

**Task 4 (20%)** : Figure out an SQL injection that leads to the user-data API call not returning anything / The user panel doesn't show any details. Report what you did. Explain in detail why this is happening and also point to the part of the backend code that's causing this behavior.

**Task 5 (15%)** : After gaining access, logout and go to User Login. Try to change the password of the `user` using SQL injection. Report how you did it.

**Task 6 (15%)** : After exploiting SQL injection in the User Login go to the User Panel (after you login with the proper user's credentials) with the newly set password and now, you can see the `user`’s data. You can update all of the data fields except the `user`’s salary. Try to exploit SQL injection from the User's Panel to double the `user`’s salary. Report what you did.

**NOTE:  Any SQL Injection from your part that treats salary as a TEXT and not as a NUMERIC is not considered a valid answer. The problem is that salary is defined as NUMERIC but sqlite treats TEXT as a NUMERIC without complaints. So for example if you do**

<pre><strong>&#39; , salary=&#39;20000<br/></strong></pre>

**will not be considered a valid answer.**

**Task 7 (5%)** : Try to delete the users table using SQL injection from the login page. What actions did you do? How can you confirm that the table was deleted?

**Task 8 (15%)** : Try to fix the bug in the server for the vulnerable endpoint `/vulnerable`. The bug makes the endpoint vulnerable to SQL injection. The bug exists in the backend directory in the file index.js towards the end of the file and the corresponding code is:

```
app.get("/vulnerable", async (req, res, next) => {
  const db = await dbPromise;
  let ret;
  try {
    ret = await db.get(
      `SELECT username FROM users WHERE username='${req.query.q}'`
    );
  } catch(err) {
    ret = "error";
  }
  res.send(ret);
});
```

Submit the correct code. You do not need to submit the whole index.js, just the corrected code as above.

*Hint* : You may find useful the documentation of SQLite package [here](https://www.npmjs.com/package/sqlite)
