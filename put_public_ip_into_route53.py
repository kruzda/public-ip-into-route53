#!/usr/bin/env python3
import socket

record_set_name = ''
test_port = 80
hostedzone_id = ''

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.settimeout(60)
result = sock.connect_ex((record_set_name, test_port))

if not result == 0:
    import urllib3
    import ipaddress
    import boto3

    http = urllib3.PoolManager()
    public_ip_address_request = http.request('GET', 'http://icanhazip.com')
    new_public_ip_address = public_ip_address_request.data.decode().strip()
    ipaddress.ip_address(new_public_ip_address)
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
