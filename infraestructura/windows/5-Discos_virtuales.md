Si encontramos discos virtuales, podemos cargarlos en linux con la herramienta guestmount

### VMDK
  guestmount -a SQL01-disk1.vmdk -i --ro /mnt/vmdk

### VHD/VHDX
  guestmount --add WEBSRV10.vhdx  --ro /mnt/vhdx/ -m /dev/sda1

