import boto3

### Turn off EC2 instance ###
def run_action(rule,entity,params,boto_connections):
    instance = entity['id']

    result = boto_connections['ec2_client'].stop_instances(InstanceIds=[instance])

    responseCode = result['ResponseMetadata']['HTTPStatusCode']
    if responseCode >= 400:
        text_output = "Unexpected error: %s \n" % str(result)
    else:
        text_output = "Instance stopped: %s \n" % instance

    return text_output 


