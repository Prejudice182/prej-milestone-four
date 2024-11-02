from storages.backends.s3boto3 import S3Boto3Storage


class MediaStorage(S3Boto3Storage):
    '''
    Class that pushes media files up to Amazon S3 bucket
    '''
    location = 'media'
    default_acl = 'public-read'
    file_overwrite = False


class StaticStorage(S3Boto3Storage):
    '''
    Class that pushes static files up to Amazon S3 bucket
    '''
    location = 'static'
    default_acl = 'public-read'
