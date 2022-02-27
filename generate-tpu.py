import subprocess
import os
import sys
import argparse
import re

def get_args(arg_input):
    """Takes args input and returns them as a argparse parser

    Parameters 
    -------------

    arg_input : list, shape (n_nargs,)
        contains list of arguments passed to function

    Returns
    -------------

    args : namespace
        contains namespace with keys and values for each parser argument

    """
    parser = argparse.ArgumentParser(description='danbooru2018 utility script')
    parser.add_argument(
        '--name',
        type=str,
        default='gen-tpu',
        help='Name to use for tpu vm',
    )
    parser.add_argument(
        '--zone',
        type=str,
        default='europe-west4-a',
        help='zone',
    )
    parser.add_argument(
        '--version',
        type=str,
        default='tpu-vm-pt-1.10',
        help='software version to load',
    )
    parser.add_argument(
        '--accelerator-type',
        type=str,
        default='v3-8',
        help='accelerator type. Eg v3-8, v2-8',
    )
    parser.add_argument(
        '--project',
        type=str,
        default='trc-generative',
        help='gcloud project name',
    )
    parser.add_argument(
        '-n',
        '--number_of_tpus',
        type=int,
        default=1,
        help='Minimum number of atleast_tags required.',
    )

    args = parser.parse_args(arg_input)
    return args


def create_tpu(args):
    #for tpunum in range(0,args.number_of_tpus):
        #subprocess.run(["gcloud", "alpha", "compute", "tpus", "tpu-vm", "create", f"{args.name}{tpunum}"])

    print(f"Running gcloud with: {args}")
    create_result = subprocess.check_output(["gcloud", "alpha", "compute", "tpus", "tpu-vm", "create", args.name, "--zone", args.zone, "--accelerator-type", args.accelerator_type, "--project", args.project, "--version", args.version])
    describe_result = subprocess.check_output(["gcloud", "alpha", "compute", "tpus", "tpu-vm", "describe", args.name, "--zone", args.zone])
    print(f"Describe returned: {describe_result}")
    ip = re.search(r"externalIp: ([0-9]*\.[0-9]*\.[0-9]*\.[0-9]*)", str(describe_result)).expand(r"\1")
    if ip:
        print(f"Found IP: {ip}")
    else:
        print(f"Could not find ip")


    ## TODO set TPU_IP
    # TODO rsync over scripts folder
    # and execute install script
        

def main(args=None):
    if args == None:
        arg_input = sys.argv[1:]
        args = get_args(arg_input)
    if args.accelerator_type == "v3-8" and args.zone != 'europe-west4-a' or args.accelerator_type == "v2-8" and args.zone != 'us-central1-f':
        answer = input(f"{args.accelerator_type} requested in {args.zone}, which is not covered by TRC. Are you sure? (y/n):")
        if answer.lower() not in ["y","yes"]:
            print("Cancelling operation")
            return

    ## Generate tpu
    create_tpu(args)


if __name__ == '__main__':
    main()
