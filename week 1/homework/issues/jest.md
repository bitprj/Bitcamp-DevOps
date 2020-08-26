# Testing with Jest

As previously mentioned, Jest is a popular tool used to test JavaScript code. This week's homework is to take the test file, filterByTerm.spec.js, and use GitHub Actions to automate its testing of the main file, filterByTerm.js, in a new repository. A significant portion of using GitHub Actions is figuring out how to use specific actions, but during the course of this week's livestream you should have already been told everything you need to know on how to do this. See how far you can get by yourself!

__Requirements__
  - The test should run on both a push and a pull request made to the master branch.
  - Ubuntu-latest should be used

If you're stuck, here are some hints:

<details><summary> Hint #1!</summary>
you'll probably want 3 files in your repo for this one. "src" should store filterByTerm.js, "__test__" should  store filterByTerm.spec.js, and ".github/workflows" should store the .yml file you'll need to write.</details>

<details><summary> Hint #2!</summary>
Jest doesn't need a community based action, it's built right in to GitHub Actions. See if the workflow you made in the CI intro could be adapted.</details>

<details><summary> Hint #3!</summary>
Node.js is a JavaScript-based framework - google "node.js github actions" and see if you can find a templated workflow you can make some minor changes to, and put it in your .github/workflows directory. </details>
