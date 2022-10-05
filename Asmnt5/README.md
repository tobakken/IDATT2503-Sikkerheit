# Assignment 5

## Running CI
### On gitlab
Just push the code to gitlab and the gitlab runner should run automaticly

### Locally using gitlab-runner
Make sure you have Docker installed first.
Then:
* Download the latest Gitlab-runner
* Clone the project and copy the folder for ```Asmnt5``` to a new folder
* initialize local git repo with ```git init```
* Commit all the files in the folder with ```git add . && git commit -m "Fuzzer testing init"```
* run ```sudo gitlab-runner exec docker fuzzer-testing```


