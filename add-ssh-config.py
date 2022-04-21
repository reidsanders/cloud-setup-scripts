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
    parser = argparse.ArgumentParser(description='tpu creation script')
    parser.add_argument(
        '--prefix',
        type=str,
        default='gcloud-',
        help='prefix to use for ssh configs',
    )
    parser.add_argument(
        '--project',
        type=str,
        default='trc-generative',
        help='gcloud project name',
    )
    parser.add_argument(
        '--name',
        type=str,
        default='tpu',
        help='Name to use for tpu vm',
    )
    parser.add_argument(
        '--zone',
        type=str,
        default='europe-west4-a',
        help='zone',
    )
    parser.add_argument(
        '--identityfile',
        type=str,
        default='~/.ssh/google_compute_engine',
        help='ssh identity file path',
    )
    parser.add_argument(
        '--user',
        type=str,
        default='user',
        help='remote username',
    )
    parser.add_argument(
        '--outfile',
        type=str,
        default='sshconfig',
        help='file to append config to',
    )


    args = parser.parse_args(arg_input)
    return args


def get_tpu_ips(args):
    #list_result = subprocess.check_output(["gcloud", "alpha", "compute", "tpus", "tpu-vm", "list"])
    ##print(list_result)
    #name = re.search(r".*STATUS\n(.*) ", str(list_result)).expand(r"\1")
    #print(name)

    describe_result = subprocess.check_output(["gcloud", "alpha", "compute", "tpus", "tpu-vm", "describe", args.name, "--zone", args.zone])
    #print(f"Describe returned: {describe_result}")
    ip = re.search(r"externalIp: ([0-9]*\.[0-9]*\.[0-9]*\.[0-9]*)", str(describe_result)).expand(r"\1")
    if ip:
        print(f"Found IP: {ip}")
    else:
        print(f"Could not find ip")
        return

    text = f"""Host {args.prefix}{args.name}
        Hostname {ip}
        IdentityFile {args.identityfile}
        User {args.user}
        IdentitiesOnly yes
        """
    answer = input(f"Append this hostname to {args.outfile}?:\n{text}\n(y/n)?")
    if answer.lower() not in ["y","yes"]:
        print("Cancelling operation")
        return
    else:
        print("Writing")
        with open(args.outfile, "a") as f:
            f.write(f"\n{text}\n")

def main(args=None):
    if args == None:
        arg_input = sys.argv[1:]
        args = get_args(arg_input)

    get_tpu_ips(args)


if __name__ == '__main__':
    main()
