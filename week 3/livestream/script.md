## Intro

- welcome back - this week, we'll be wrapping things up and covering
    - GitHub script
    - some functionality with Microsoft Azure
        - *again this might be cut out entirely. I'm not a fan of it.*

## Homework

- last week's homework should have been pretty independent, but here's a chance to ask any questions if they arose.

## Part 6

### Activity: Respond to an issue when it gets opened

- this time I've left the quick link since this is really just review, but you can still recommend for people to type it out

- Use expressions to determine `if` a step should execute
- type out this bit and explain what's going on.

## Part 7

note: you'll need to install [https://docs.microsoft.com/en-us/cli/azure/install-azure-cli?view=azure-cli-latest](https://docs.microsoft.com/en-us/cli/azure/install-azure-cli?view=azure-cli-latest) and use [https://education.github.com/pack](https://education.github.com/pack) for access to azure

We'll learn how to create a workflow that enables Continuous Delivery with the help of Microsoft Azure.

- this won't be something in the homework or anything, but it's a useful third party application we'll cover (for the general ideas of how it works more than anything)
- We covered CD last week, but there is a lot of flexibility in how you approach the CI/CD process,  whether it solely be with github actions or with the help of a third party action

```yaml
env:
     DOCKER_IMAGE_NAME: USER-azure-ttt
     IMAGE_REGISTRY_URL: docker.pkg.github.com
     #################################################
     ### USER PROVIDED VALUES ARE REQUIRED BELOW   ###
     #################################################
     #################################################
     ### REPLACE USERNAME WITH GH USERNAME         ###
     AZURE_WEBAPP_NAME: USER-ttt-app
     #################################################
```

- remember # is how yaml formats comments - that second bottom line is the only one that actually matters, everything else is there just for readability.
- obviously actually change the USER name with your github username!
- I'd recommend copying and pasting this one rather than just typing it out just to preserve readability (and that it needs to be changed if you ever try to copy and paste into another user's repo)
    - *moreso bc every other given code fragment in the lesson assumes you did it like this*

use what you learned in lesson 2 to add steps that check out the repository, initialize and build the app using npm, and upload the build artifacts.

- *give them a bit, but don't worry if they can't remember - it's very similar to what was done with CI though.*
- *let them use this time to try steps 2, 3, and 4 - they probably won't figure it all out, but stress that that's okay and we're just seeing how far they can get.*

GitHub Actions is cloud agnostic, so any cloud will work. We'll show how to deploy to Azure in this course.

- to clarify, if you learn some other cloud resource than azure it would work with github actions too!

## Homework

- This final review problem isn't meant to be some incredibly difficult final problem, but it is meant to demonstrate a relatively realistic implementation of GitHub Actions
    - the main thing being demonstrated - community based actions!
    - you won't be given the actions, you'll be given a goal and need to find a community based action on your own to accomplish that task

- two separate tasks: you have a sample .md file that you need to spellcheck, and a python file you need to test. Automate the spellcheck test, and automate the python test on pull requests to the master branch.
    - you can have two separate workflow files, or one combined one. You'll have a lot of flexibility here - just get it working!
