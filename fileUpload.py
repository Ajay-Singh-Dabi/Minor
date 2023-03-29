
import os
import boto3

ACCESS_ID = 'DO00QUPV42Q6RWQC3RAK'
SECRET_KEY = 'fKtjBTxyDNUSxKNaf61Uk245sqPjkLaGaMq1SCQm7BM'

session = boto3.session.Session()
client = session.client('s3',
                        region_name='nyc3',
                        endpoint_url='https://cloud-minor.nyc3.digitaloceanspaces.com',
                        aws_access_key_id=ACCESS_ID,
                        aws_secret_access_key=SECRET_KEY)

def upload_to_cloud(filepath,user):
    client.put_object(Bucket=user,
                  Key=filepath,
                  Body=b'The contents of the file.',
                  ACL='private',
                  Metadata={
                      'x-amz-meta-my-key': 'user'
                  }
                )
    return client.generate_presigned_url('get_object',
                                    Params={'Bucket': user,
                                            'Key': f'{filepath}'},
                                    ExpiresIn=60*60*24)

print(upload_to_cloud('test.mp4','test'))