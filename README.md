## lambda-runtime-update-helper

### Getting started

This project is created to help for update AWS Lambda function runtime by batch. The function will update Lambda runtime in $LATEST version.

### Pre-request

- [ ] [Complete basic AWS CLI Configuration with Admin right](https://docs.aws.amazon.com/cli/latest/userguide/cli-configure-quickstart.html)
- [ ] boto3 is required for the project

### How to run

Update region and runtime info in [app.py](handler/app.py)

```
# List runtime needs to be update here
# 'nodejs'|'nodejs4.3'|'nodejs6.10'|'nodejs8.10'|'nodejs10.x'|'nodejs12.x'|'nodejs14.x'|'nodejs16.x'|'java8'|'java8.al2'|'java11'|'python2.7'|'python3.6'|'python3.7'|'python3.8'|'python3.9'|'dotnetcore1.0'|'dotnetcore2.0'|'dotnetcore2.1'|'dotnetcore3.1'|'dotnet6'|'nodejs4.3-edge'|'go1.x'|'ruby2.5'|'ruby2.7'|'provided'|'provided.al2'
sourceRuntimeList = ('nodejs12.x','nodejs14.x')

# Target update runtime
targetRuntime = 'nodejs16.x'

# Client config
client_config = Config(
    region_name='us-east-1'
)
```

Run the function
```
python handler/app.py
```

## Security

See [CONTRIBUTING](CONTRIBUTING.md#security-issue-notifications) for more information.

## License

This library is licensed under the MIT-0 License. See the LICENSE file.

