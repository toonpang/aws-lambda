import boto3
import logging

#setup simple logging for INFO
logger = logging.getLogger()
logger.setLevel(logging.INFO)

#define the connection
ec2 = boto3.resource('ec2',region_name='ap-southeast-1')

def lambda_handler(event, context):
    # Use the filter() method of the instances collection to retrieve
    # all stopped EC2 instances.
    
    filters = [
        {
            'Name': 'tag:AutoOn',
            'Values': ['True']
        },
        {
            'Name': 'instance-state-name', 
            'Values': ['stopped']
        }
    ]
    
    #filter the instances
    instances = ec2.instances.filter(Filters=filters)

    #locate all stopped instances
    StoppedInstances = [instance.id for instance in instances]
    print len(StoppedInstances)
    #print the instances for logging purposes
    #print StoppedInstances 
    
    #make sure there are actually instances to shut down. 
    if len(StoppedInstances) > 0:
        #perform the startup
        startUp = ec2.instances.filter(InstanceIds=StoppedInstances).start()
        print startUp
    else:
        print "Nothing to see here"
        
    allinstances = ec2.instances.filter()
    print allinstances

