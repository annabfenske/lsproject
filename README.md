### Redis delay
Note that there is a <10 second delay between when an id is reported lost and when that change is reflected in the client.

### Configuring Go Packages
1. If you haven't already, install Go with `brew install go`
2. Add the following lines to your `~/.bash_profile`
```
export GOPATH=$HOME/golang
export GOROOT=/usr/local/opt/go/libexec
export GOBIN=$GOPATH/bin
export PATH=$PATH:$GOPATH
export PATH=$PATH:$GOROOT/bin
export PATH=$GOPATH/bin:$PATH
```
3. Navigate to the root directory of the project. In this case, that would be the `lsproject` folder
4. Install the primary Go packages using `go install ./cmd/going_going_gone`
5. Now, you should be able to test the app locally using `heroku local`
