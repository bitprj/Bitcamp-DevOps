# Intro

- introduce yourself, and welcome students to the bootcamp
- Ask: What is DevOps?
    - System development life cycle can be long and arduous - once changes are made to code, have to be tested, committed, placed into production, etc.
    - DevOps automates this process - code is automatically tested, integrated, etc.
- To learn about DevOps, we'll be using GitHub Actions
    - Relatively beginner-friendly, and most people are already familiar with github.
- What's being covered this session?
    - Intro to how github actions operates, and a basic overview of Continuous Integration (CI) operates (we'll elaborate on what this is later)

### Part 1

[https://lab.github.com/michaelloughnane/bitcamp-devops-1](https://lab.github.com/michaelloughnane/bitcamp-devops-1)

- *The primary focus of this will be following along with the above tutorial. Use these notes to follow along and add additional info as necessary.*
- *note: since I'm the author of the github learning lab, I can't go through the lab to take screenshots. I'll copy and paste relevant parts of the lesson*

GitHub Actions are a flexible way to automate nearly every aspect of your team's software workflow. Here are just a few of the ways teams are using GitHub Actions:

- Automated testing (CI)
- Continuous delivery and deployment
- Responding to workflow triggers using issues, @ mentions, labels, and more
- Triggering code reviews
- Managing branches
- Triaging issues and pull requests

- define triaging (not a common word) - assigning levels of urgency to
- we'll be going over all of these in the coming weeks

Actions come in two types: **container actions** and **JavaScript actions**.

Docker **container actions** allow the environment to be packaged with the GitHub Actions code and can only execute in the GitHub-Hosted Linux environment.

**JavaScript actions** decouple the GitHub Actions code from the environment allowing faster execution but accepting greater dependency management responsibility.

- knowing what these actions look like in code is important, but we'll be focusing on the actual writing of actions next week.

Our action will use a Docker container so it will require a `Dockerfile`. The action we later write will be executed in an environment defined by this file.

- But first, what exactly *is* a docker container?
- Docker containers are like virtual machines - they simulate a particular operating system or environment that code is then run on
    - (they actually work a bit differently than virtual machines, and we can elaborate on that more later, but the important thing to know is that, like we said already, they set up the environment)

1. Fill the `Dockerfile` with the content below:

```docker
FROM debian:9.5-slim

ADD entrypoint.sh /entrypoint.sh
RUN chmod +x /entrypoint.sh
ENTRYPOINT ["/entrypoint.sh"]
```

- you'll need to explain what's going on with this code, and obviously type it out (it's only written in the lesson so that students can go back and review later if they want)
    - also, encourage students to type it out themselves rather than just copying and pasting, since it helps comprehension
    - 'FROM debian:9.5-slim' - we said before that docker containers are like virtual machines - this command makes it so that Debian, a form of Linux, is the operating system in question, and the foundation of our container
    - 'ADD [entrypoint.sh](http://entrypoint.sh) /entrypoint.sh' - this command finds a local file named entrypoint.sh (which we'll be writing in a few minutes), and copies it to the container so that the container can run it.
    - 'RUN chmod +x /[entrypoint.sh](http://entrypoint.sh)' - you don't need to worry about this line too much, but it essentially makes the container's entrypoint.sh executable
    - 'ENTRYPOINT ["/entrypoint.sh"]' - this is the line that actually executes entrypoint.sh. When we run the container, this command will make it run /entrypoint.sh

    2. Add the following content to the `entrypoint.sh` file:

    ```bash
    #!/bin/sh -l
    sh -c "echo Hello world my name is $INPUT_MY_NAME"
    ```

    - This is all just basic syntax for .sh files, so don't worry about specific commands - like previously stated, this simply outputs a "Hello World" statement

    2. Add the following content to the `action.yml` file:

    ```yaml
    name: "Hello Actions"
       description: "Greet someone"
       author: "octocat@github.com"

       inputs:
         MY_NAME:
           description: "Who to greet"
           required: true
           default: "World"

       runs:
         using: "docker"
         image: "Dockerfile"

       branding:
         icon: "mic"
         color: "purple"
    ```

    - The code here is fairly self explanatory, but we'll be going over the specific makeup of a .yaml file later in part 2 of today's lesson.

    Workflows are defined in special files in the `.github/workflows` directory, named `main.yml`.

    - Note: You can actually have multiple different workflow files that run simultaneously, so long as you put them all in this directory. We'll only be using one right now, but you might find it useful later on.
        - *(this is foreshadowing for week 2's project. don't tell them that.)*

    (the creation of the main.yml file is fairly well explained in the lesson text, so following along there should be sufficient, with the exception of...)

    - uses: actions/checkout@v1 uses a community action called checkout to allow the workflow to access the contents of the repository
    - Community actions are invaluable tools that you can (and should) make free use of in your projects. This is only one action of many at your disposal, and if you ever need to do some particular specialized task with github actions, start with a quick google search - you'll never know what somebody else has already made for you!

    ```yaml
    MY_NAME: "Michael"
    ```

    - for this line, if you (the teacher) aren't me and your name isn't Michael, feel free to write in your own name and/or for students to write in theirs.

### Part 2

The power of ***GitHub**** Actions lies in access to actions written by the :sparkles: GitHub community. Here, we'll use two Actions officially written and supported by GitHub:

- `actions/checkout@v2` is used to ensure our virtual machine has a copy of our codebase. The checked out code will be used to run tests against.
- `actions/setup-node@v1` is used to set up proper versions of Node.js since we'll be performing testing against multiple versions.
- something not relevant right at this second but useful to know - these actions may be "official" community actions, but they're implemented just like any other community action. The only difference is that github has made templates with the relevant code prewritten.

This pull request introduces [Jest](https://jestjs.io/), a popular JavaScript testing framework. We'll use it to learn how to use it for continuous integration.

- Remember this - your homework for this week will be using Jest as well, and we'll talk more about it later.

### Activity: Tell the bot which test is failing so we can fix it

1. Navigate to the log output

2. Identify a name of a failing test

3. Comment the name of the failing test here

- give the students ~30 seconds to do this, then go through and demonstrate the solution
    - it's looking for "Initializes with two players"

### Activity: Edit the file that's causing the test to fail

Edit the `src/game.js` file directly, or accept the suggestion below.

- whether the students edit directly is up to them, but you (the teacher) should manually edit the file.
    - I'm not going to write this out every time, but whenever the option for doing an edit manually comes up, do it manually.

Now that we've learned how to quickly set up CI, let's try a more realistic use case.

Our fictional team has a custom workflow that goes beyond the template we've used so far. We would like the following features:

- after reading off this list, clarify that we'll be going into more detail on what each of these things mean later

## Step 17: Automate approvals

```yaml

        runs-on: ubuntu-latest
        steps:
        - name: Label when approved
          uses: pullreminders/label-when-approved-action@master
          env:
            APPROVALS: "1"
            GITHUB_TOKEN: {% raw %}${{ secrets.GITHUB_TOKEN }}{% endraw %}
            ADD_LABEL: "approved"
 
```

- here's the solution. Give students a bit to try it on their own with the given hints, then write it in.

End of part 2!

### Homework:

- without any template, try using jest to automate this javascript program!
    - You'll want to make the test trigger on a push or pull request to the master branch.
    - (don't have the code yet, but they'll be given a repo with nothing but a javascript program, and a test program. No folders, definitely no .yaml stuff. They'll need to figure it out.)
    - google is your friend here, as are the lessons we just went through.

Hints (to send out through the week if people haven't gotten it):

- the folders you'll want are ".github/workflows", "__tests__" and "src" - the file we're testing goes in src, and you can probably figure out the other two.
- Our Node.js template used jest, if you remember - maybe see what you can do with the code from that?

Solution for the .yml:

```yaml
name: Jest CI

on:
  push:
    branches: [ master ]
  pull_request:
    branches: [ master ]
    
jobs:
  test:
    runs-on: ubuntu-latest

    steps:
      - uses: actions/checkout@v1
      - name: Use Node.js 12.x
        uses: actions/setup-node@v1
        with:
          node-version: "12.x"
      - name: npm install, and test
        run: |
          npm install
          npm test
        env:
          CI: true
```

### Conclusion:

- finished up the basics of GitHub actions
- next week, Continuous Deployment and more on writing action statements
- we'll start next week by going over the homework
