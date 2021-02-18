
-- Ref: https://aws.amazon.com/blogs/developer/getting-started-with-the-aws-cloud-development-kit-and-python/

-- see: readme.md

    cdk init --language python sample-app

-- It should create the virtual environment, so just activate it.
-- Please run 'python -m venv .venv'!
-- Executing Creating virtualenv...
-- All done!

    PS C:\cdk\aws-python-topic> .venv\Scripts\activate.bat

-- Then install the requirements.txt

    pip install -r requirements.txt

-- then create the template using synth
    cdk synth

-- changet the environment in app.py (default to US)

-- cdk deploy but must be wrapped in "aws2-wrap"

    PS C:\cdk\aws-python-topic> aws sso login --profile ssocloudopsaccess
    PS C:\cdk\aws-python-topic> aws2-wrap --profile ssocloudopsaccess cdk deploy 

-- cleanup

    PS C:\cdk\aws-python-topic> aws2-wrap --profile ssocloudopsaccess cdk destroy