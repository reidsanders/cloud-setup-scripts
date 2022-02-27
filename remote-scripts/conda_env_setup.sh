#conda create -n diffusion python=3.8
#sleep 1
#conda init bash
#sleep 1
#conda activate diffusion
#sleep 1
pip install -r requirements.txt
sleep 1
pip3 install torch_xla[tpuvm] -f https://storage.googleapis.com/tpu-pytorch/wheels/tpuvm/torch_xla-1.10-cp38-cp38-linux_x86_64.whl ## TODO try setting in requrements.txt
sleep 1
sudo pip3 install https://storage.googleapis.com/cloud-tpu-tpuvm-artifacts/wheels/libtpu-nightly/libtpu_nightly-0.1.dev20211015-py3-none-any.whl
sleep 1
pip install --upgrade wandb
sleep 1
pip install --upgrade git+https://github.com/PytorchLightning/pytorch-lightning.git

