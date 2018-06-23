#!/usr/bin/env python3
"""
Estimates the size of all containers hosted in Berkadia's AWS ECR

This module will connect to Amazon Web Services and will pull
containers from the Elastic Container Registry.  The purpose
of this tool is to produce a report about the containers that
exist in the ECR.

Attributes:


Todo:


"""


def main():
    """

    """

    import boto3

    ecr_client = boto3.client('ecr')

    paginator = ecr_client.get_paginator('describe_repositories')
    pages = paginator.paginate()
    for page in pages:
        for obj in page['repositories']:
            repositories = []
            repositories[i].append(dict(obj))
            print(type(obj))

    print(repositories)


if __name__=='__main__':
    main()
