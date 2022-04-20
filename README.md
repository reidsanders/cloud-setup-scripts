# cloud-setup-scripts
Some simple scripts I've used for setting up TPU VMs for Tensorflow Research Cloud. I've used these for the tpu-vm-pt-1.10 image with python 3.8. You may need to adjust.


### generate-tpus.py 

Just calls gcloud commands, so those must be set up. Has a region check you can set if you need certain machines to be restricted to certain zones (useful for Tensorflow Research Cloud). 

### Conda Setup

Push the remote-scripts directory to your tpu vm.

Run from with
For some reason conda init does not work in a bash script. So run these commands

```sh
$ conda create -n diffusion python=3.8
$ conda init bash
$ conda activate diffusion
$ cd YOUR_PROJECT
$ pip install -r requirements.txt
$ pip install https://storage.googleapis.com/cloud-tpu-tpuvm-artifacts/wheels/libtpu-nightly/libtpu_nightly-0.1.dev20211015-py3-none-any.whl
$ pip install torch_xla[tpuvm] -f https://storage.googleapis.com/tpu-pytorch/wheels/tpuvm/torch_xla-1.10-cp38-cp38-linux_x86_64.whl
```

### TPU Setup

Running this script will set some required environment variables, install a useful tmux config, set default python to python3, and enable vi mode in shell.


With thanks to Tensorflow Research Cloud for generous tpu credits!


