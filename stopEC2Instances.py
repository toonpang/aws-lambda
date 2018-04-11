import boto3
import logging

#define the connection

ec2 = boto3.resource('ec2',region_name='ap-southeast-1')
def lambda_handler(event, context):

    filters = [
        {
            'Name': 'tag:AutoStop',
            'Values': ['True']
        },
        {
            'Name': 'instance-state-name', 
            'Values': ['running']
        }
    ]

    instances = ec2.instances.filter(Filters=filters)
    StartUpInstances = [instance.id for instance in instances]
    print len(StartUpInstances)

    if len(StartUpInstances) > 0:

        #print the instances for logging purposes
        print StartUpInstances
        result = ec2.instances.filter(InstanceIds=StartUpInstances).stop()
        print result
    else:
        print "Nothing to do here"

