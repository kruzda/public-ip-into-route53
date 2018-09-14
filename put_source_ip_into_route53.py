import boto3
hostedzone_id = ''
record_set_name = ''

def lambda_handler(event, context):
    new_public_ip_address = event['requestContext']['identity']['sourceIp']
    print("new ip: {ip}".format(ip=new_public_ip_address))
    r53_client = boto3.client('route53')
    response = r53_client.change_resource_record_sets(
        HostedZoneId = hostedzone_id,
        ChangeBatch = {
            'Changes': [
                {
                    'Action': 'UPSERT',
                    'ResourceRecordSet': {
                        'Name': record_set_name,
                        'Type': 'A',
                        'TTL': 300,
                        'ResourceRecords': [
                            {
                                'Value': new_public_ip_address
                            },
                        ]
                    }
                },
            ]
        } 
    )
    print(response)
    return {
        "statusCode": response['ResponseMetadata']['HTTPStatusCode'],
        "body": "Call to Route53 API complete."
    }
