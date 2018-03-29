import os
import boto3
import datetime

MAIL_FROM = os.environ['MAIL_FROM']
MAIL_TO   = os.environ['MAIL_TO']

def lambda_handler(event, context):

    billing = getBilling()
    send_email(billing)

    return

def send_email(billing):
    ses_client = boto3.client('ses', region_name='us-east-1')

    return ses_client.send_email(
        Source=MAIL_FROM,
        Destination={
            'ToAddresses': [
                MAIL_TO,
            ]
        },
        Message={
            'Subject': {
                'Data': '【システムメール】現在のAWS利用料金',
            },
            'Body': {
                'Text': {
                    'Data': '現在のAWS利用料は、$' + str(billing) + ' です。' ,
                },
            }
        }
    )

def getBilling():
    cloud_watch_client = boto3.client('cloudwatch', region_name='us-east-1')
    start_time = datetime.datetime.today() - datetime.timedelta(days=1)
    end_time   = datetime.datetime.today()

    statistics = cloud_watch_client.get_metric_statistics(
                        Namespace='AWS/Billing',
                        MetricName='EstimatedCharges',
                        Dimensions=[
                            {
                                'Name': 'Currency',
                                'Value': 'USD'
                            }
                        ],
                        StartTime=start_time,
                        EndTime=end_time,
                        Period=3600*24,
                        Statistics=['Maximum']
                        )

    return statistics['Datapoints'][0]['Maximum']
