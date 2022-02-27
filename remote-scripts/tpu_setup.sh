git clone --branch patch-1 https://github.com/computertoucher/tmux-config.git
./tmux-config/install.sh
sleep .5
cp .inputrc ~/
sudo apt install python-is-python3

printf 'export XRT_TPU_CONFIG="localservice;0;localhost:51011"\n' >> ~/.bashrc
printf 'export XLA_USE_BF16=1\n' >> ~/.bashrc
