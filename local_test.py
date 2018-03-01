## LOCAL TESTING
from index import * 

#sample event

#to change the event type, paste in the message line from the sample event that you want to use from below. 

event = {
    'Records': [{
        'EventSource': 'aws:sns',
        'EventVersion': '1.0',
        'EventSubscriptionArn': 'arn:aws:sns:us-west-2:905007184296:eventsToSlack:0cf0e80c-1fef-4421-9cc0-b3c102ac7836',
        'Sns': {
            'Type': 'Notification',
            'MessageId': 'd59748d6-f529-532f-bf13-1a1e438fde5c',
            'TopicArn': 'arn:aws:sns:us-west-2:905007184296:eventsToSlack',
            'Subject': 'Dome9 Continuous compliance: Entity status change detected',
            'Message': '{"policy":{"name":"sns_failed_events","description":""},"bundle":{"name":"Copy of sns_send_event_failures","description":""},"reportTime":"2018-01-30T03:05:14.489Z","rule":{"name":"s3 should fail","description":"","remediation":"","complianceTags":"AUTO: sg_rules_delete","severity":"High"},"status":"Failed","account":{"id":"726853184812","vendor":"Aws"},"region":"us-west-2","entity":{"logging":{"targetBucketName":null,"targetPrefix":null,"grants":[],"enabled":false},"acl":{"grants":[{"canonicalUser":"db1b62654bda37f8a0d7ea765caa232a3950af8a64ef30f976417454e644bfa5","displayName":"alex","emailAddress":null,"premission":"FULL_CONTROL","premissionHeaderName":"x-amz-grant-full-control","type":"CanonicalUser","uri":null}],"ownerDisplayName":"alex","ownerId":"db1b62654bda37f8a0d7ea765caa232a3950af8a64ef30f976417454e644bfa5"},"policy":{"Version":"2012-10-17","Statement":[{"Sid":"AWSCloudTrailAclCheck20150319","Effect":"Allow","Principal":{"Service":"cloudtrail.amazonaws.com"},"Action":"s3:GetBucketAcl","Resource":"arn:aws:s3:::sg-663eb256"},{"Sid":"AWSCloudTrailWrite20150319","Effect":"Allow","Principal":{"Service":"cloudtrail.amazonaws.com"},"Action":"s3:PutObject","Resource":"arn:aws:s3:::sg-663eb256/AWSLogs/905007184296/*","Condition":{"StringEquals":{"s3:x-amz-acl":"bucket-owner-full-control"}}}]},"versioning":{"status":"Off","mfaDelete":false},"website":{"indexDocumentSuffix":null,"errorDocument":null,"routingRules":[],"redirectAllRequestsTo":{"hostName":"","httpRedirectCode":"","protocol":"","replaceKeyPrefixWith":"","replaceKeyWith":""}},"encryption":{"serverSideEncryptionRules":[]},"replication":{"role":"","rules":[]},"vpc":null,"id":"sg-08fa4770","type":"S3Bucket","name":"sg-08fa4770","dome9Id":"1|89ff48fc-9c8b-4292-a169-d6e938af2dd2|rg|s3Bucket|sg-663eb256-62362","accountNumber":"905007184296","region":"us-west-2","source":"db","tags":[]}}',
            'Timestamp': '2018-01-04T23:10:30.652Z',
            'SignatureVersion': '1',
            'Signature': 'fKnhCGtvNIKIKslbL54A2ZjIiGc/NPw==',
            'SigningCertUrl': 'https://sns.us-west-2.amazonaws.com/SimpleNotificationService-433026a4050d206028891664da859041.pem',
            'UnsubscribeUrl': 'https://sns.us-west-2.amazonaws.com/?Action=Unsubscribe&SubscriptionArn=arn:aws:sns:us-west-2:905007184296:eventsToSlack:0cf0e80c-1fef-4421-9cc0-b3c102ac7836',
            'MessageAttributes': {}
        }
    }]
}


"AUTO: ec2_tag mykey myvalue","AUTO: ec2_tag mykey my value", "AUTO: ec2_tag \"my key\" myvalue","AUTO: ec2_tag mykey \"my value\"","AUTO: ec2_tag \"my key\" \"my value\""]

#export SNS_TOPIC_ARN="arn:aws:sns:us-west-2:905007184296:eventsToSlack"
SNS_TOPIC_ARN = "arn:aws:sns:us-west-2:905007184296:eventsToSlack"

context = ""


lambda_handler(event,context)

