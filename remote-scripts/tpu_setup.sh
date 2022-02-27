## conda install
mkdir downloads
cd downloads
wget https://repo.anaconda.com/miniconda/Miniconda3-latest-Linux-x86_64.sh
bash ./Miniconda3-latest-Linux-x86_64.sh

## TODO run installation of v-diffusion-pytorch
## move to outer dir

#git clone https://github.com/samoshkin/tmux-config.giit
git clone --branch patch-1 https://github.com/computertoucher/tmux-config.git
./tmux-config/install.sh
sleep .5
cp .inputrc ~/
sudo apt install python-is-python3

printf 'export XRT_TPU_CONFIG="localservice;0;localhost:51011"\n' >> ~/.bashrc
#printf 'export PT_XLA_DEBUG=1' >> ~/.bashrc
printf 'export XLA_USE_BF16=1\n' >> ~/.bashrc
