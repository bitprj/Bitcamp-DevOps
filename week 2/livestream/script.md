## Intro

- welcome back - this week, we'll be covering:
    - Continuous Deployment,
    - writing custom action files
- but first...

## Homework

- go over last week's homework - just read out the solution, the code is in week 1 script
    - note similarities to template from [https://docs.github.com/en/actions/language-and-framework-guides/using-nodejs-with-github-actions](https://docs.github.com/en/actions/language-and-framework-guides/using-nodejs-with-github-actions)
        - not the exact same though - so long as the build works, it's alright
    - obviously answer questions, etc.

## Part 3 (continued from week 1, use lesson 3)

A quick note of caution!

This course requires your name to not contain any capital letters! It causes an error down the line. If your username contains a capital letter, it's recommended to change it now.

- show how this is done ([https://docs.github.com/en/github/setting-up-and-managing-your-github-user-account/changing-your-github-username](https://docs.github.com/en/github/setting-up-and-managing-your-github-user-account/changing-your-github-username))

### What is Docker?

Docker is an engine that allows you to run containers.

- you can gloss over this section mostly - just remind people of the quick definition of containers from week 1 as sorta-VMs, and this just being how exactly they're different from VMs. You can go over this stuff, but tell students it doesn't matter too much and they don't need to really worry about it.

Because a `Dockerfile` is a text file, we are able to create a new version of it as source code. This *configuration as code* allows us a single point of truth for our application.

- [https://en.wikipedia.org/wiki/Single_source_of_truth](https://en.wikipedia.org/wiki/Single_source_of_truth)
- give a quick definition - a thing where "every data element is edited in one place"

[Edit the current workflow file in our repository]({{ repoUrl }}/blob/docker-workflow/.github/workflows/ci-workflow.yml)

2. Rename `ci-workflow.yml` to `cd-workflow.yml`:

3. On line 1, change the name from `Node CI` to `Docker CD`

`yaml name: Docker CD`

4. Add the following job to your workflow file:

```yaml
Build-and-Push-Docker-Image:
    runs-on: ubuntu-latest
    needs: test
    name: Docker Build, Tag, Push

    steps:
    - name: Checkout
      uses: actions/checkout@v1
    - name: Download built artifact
      uses: actions/download-artifact@master
      with:
        name: webpack artifacts
        path: public
    - name: Build container image
      uses: docker/build-push-action@v1
      with:
        username: {% raw %}${{github.actor}}{% endraw %}
        password: {% raw %}${{secrets.GITHUB_TOKEN}}{% endraw %}
        registry: docker.pkg.github.com
        repository: {{ user.login }}/github-actions-for-packages/tic-tac-toe
        tag_with_sha: true
```

- the code above will have some differences on the actual lesson - use the lesson's code
    - most of this stuff is kinda intuitive, but explain it

2. Paste the following contents inside of the Docker file:

```docker
FROM nginx:1.17
COPY . /usr/share/nginx/html
```

- this works just like the dockerfile from part 1 - we're using something called nginx instead of debian

Whoa, now things are running! This may take a few minutes.

After committing the `Dockerfile`, the repository had the components it needed to start the CD workflow.

This might take a tiny amount of time, so grab your popcorn 🍿 and wait. I'll respond one your pipeline has finished running, until then... sit tight!

- take questions during this wait

**Before we can use this Docker image, you will need to generate a [personal access token](https://help.github.com/en/github/authenticating-to-github/creating-a-personal-access-token-for-the-command-line) that contains the following permissions:**

- it might not be immediately obvious, but this link isn't just more reading info, it's the directions on how to do this. Click it, and show students how to do it.

## Part 4

Intro: this part teaches with JavaScript, but knowing JavaScript isn't necessary to understand the principles being taught. Interpret it as pseudocode.

### Activity: Modify my-workflow.yml to remove boilerplate steps

- boilerplate essentially means excess code, if any students don't know the term.

1. Using your code editor, navigate into each file and modify them so that each one is similar to the code in the examples shown above:

- you can give the students a bit of time to do this on their own, before going in and doing it.

### Activity: Try these things

- prompt the students to tell you what happens when they do the things here.

The most common types of API at the time this course was written are:

- REST
- SOAP
- XML-RPC
- JSON-RPC
- optionally mention very basically what these do. don't have to, but you can.

### Activity: Configure your second action

Now that you have all the necessary tools installed locally, follow these steps to ensure your environment is configured and ready for actions.

- depending on the OS you might need to use \ instead of / for these commands.

```jsx
const getJoke = require("./joke");
const core = require("@actions/core");

async function run() {
  const joke = await getJoke();
  console.log(joke);
  core.setOutput("joke-output", joke);
}

run();
```

- you can explain what async means if you want (waits for the await command to be filled before continuing)

### Activity: Create the final JavaScript file

- give this a try,  but don't worry about it too much if you can't do it bc you don't know javascript. still, try to figure it out based on the prior examples.

## Homework

- we have part 5, which is extremely similar to part 4, except with a different language to write actions
    - do it independently, and create the action files required of you from it
