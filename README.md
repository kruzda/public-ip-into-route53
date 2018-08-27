# public-ip-into-route53
Updates an AWS Route 53 Record Set with the public IP address gathered from http://icanhazip.com

An update is only attempted if a connection to the specified port test_port is not successful in 60 seconds.

Configuration required:
 * record_set_name - the domain name that needs to be updated
 * test_port - a network port that when not connectible makes it likely that the public IP address has changed (e.g. a DSL router's remote administration interface listening on a non-standard port)
 * hostedzone_id - the Hosted Zone's ID from Route 53

Modules required:
 * boto3 - https://aws.amazon.com/sdk-for-python/
