## conda install
mkdir downloads
cd downloads

wget https://repo.anaconda.com/miniconda/Miniconda3-latest-Linux-x86_64.sh
MINICONDA_PREFIX=/usr/local
chmod +x ./Miniconda3-latest-Linux-x86_64.sh
./Miniconda3-latest-Linux-x86_64.sh -b -f -p $MINICONDA_PREFIX


git clone --branch patch-1 https://github.com/computertoucher/tmux-config.git
./tmux-config/install.sh
sleep .5
cp .inputrc ~/
sudo apt install python-is-python3

printf 'export XRT_TPU_CONFIG="localservice;0;localhost:51011"\n' >> ~/.bashrc
printf 'export XLA_USE_BF16=1\n' >> ~/.bashrc
