import boto3
from pytz import timezone

session = boto3.Session(profile_name='<profile name>')
#session = boto3.Session(aws_access_key_id='<access key id>', aws_secret_access_key='<secret access key>', region_name='<region>')

s3 = session.resource('s3')

# Print out bucket names
#for bucket in s3.buckets.all():
#    print(bucket.name)

bucket = s3.Bucket(name='<bucket-name>')

print('Last Modified:')

for file in bucket.objects.all():
    d = file.last_modified.replace(tzinfo=timezone('US/Pacific'))
    print(file.key + ': ' + d.strftime('%c'))
    #print(file.key + ': ' + file.last_modified.strftime("%c %Z"))
