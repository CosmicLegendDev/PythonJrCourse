# What is github?

Github is a version control system to manage and share large code base with others.

## Terminology

### Repository

Its a place where all the files of a project are stored. It can be public or private.

### Branch

A branch is a separate line of development in a repository. It allows developers to work independently on a specific task/feature without effecting the main branch.

### Pull Request

A pull request is a way to propose changes to a repository. It allows developers to review and discuss the changes before merging them into the main branch.

### Pull/Fetch from remote

Pulling or fetching from a remote repository is the process of getting the latest changes from the remote repository to your local repository. "Pull" will fetch and merge the changes, while "fetch" will only download the changes without merging.  
`git pull origin <branch-name>`

### Add and Commit local changes

To add and commit local changes, you first stage the changes using `git add <file>` and then commit them using `git commit -m "commit message"`.

- git add, move the modified files to staging area.
- git commit, save the changes to the local repository (creates commit hashes).

### Push local changes to remote

To push local changes to a remote repository, you use the command `git push origin <branch-name>`. This will upload your local commits to the remote repository.

## Workflow

Initial: Clone Repo -> Modify files -> Add files -> Commit change -> Push
Update from Remote: Pull -> Modify files -> Add files -> Commit change -> Push
