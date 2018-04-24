 --------------------------------------------------------
|                        VSR(ACTOR 1)                    |
|                                                        |
|  1.1.1.1/24(ospf)   2.2.2.2/24(ospf)  10.0.0.1/24(MAN) |              
 --------------------------------------------------------
      |                     |                     |
      |                     |                     |
     +++                   +++                   +++  
 (vsreth0out)         (vsreth1out)           (vsreth2out)


 --------------------------------------------------------
|                        FRR(ACTOR 2  ubuntu16)          |
|                                                        |
|  3.3.3.3/24(ospf)   4.4.4.4/24(ospf)                   |              
 --------------------------------------------------------
      |                     |
      |                     |                   
     +++                   +++                   
 (frreth0out)         (frreth1out)  


 --------------------------------------------------------
|                        FRR(ACTOR 3 centos7)            |
|                                                        |
|  5.5.5.5/24(ospf)   6.6.6.6/24(ospf)                   |              
 --------------------------------------------------------
      |                     |
      |                     |                   
     +++                   +++                   
 (frreth2out)         (frreth3out)          




(Run as ROOT)
-------------------------------------------------------------------
1.Package install (for ubuntu)
-------------------------------------------------------------------

###install kvm and qemu
```

~ apt-get install kvm qemu

```
###install libvirt and virt-manager
```

~ apt-get install virtinst python-libvirt virt-viewer virt-manager

```

-------------------------------------------------------------------
2.Setup environment
-------------------------------------------------------------------
### create network interface for VSR(ACTOR 1)
```

ip link add vsreth0 type veth peer name vsreth0out
ip link add vsreth1 type veth peer name vsreth1out
ip link add vsreth2 type veth peer name vsreth2out
ip link set vsreth0 up
ip link set vsreth0out up
ip link set vsreth1 up
ip link set vsreth1out up
ip link set vsreth2 up
ip link set vsreth2out up

```
### create network interface for FRR(ACTOR 2)
```

ip link add frreth0 type veth peer name frreth0out
ip link add frreth1 type veth peer name frreth1out
ip link set frreth0 up
ip link set frreth0out up
ip link set frreth1 up
ip link set frreth1out up

```

### create network interface for FRR(ACTOR 3)
```
ip link add frreth2 type veth peer name frreth2out
ip link add frreth3 type veth peer name frreth3out
ip link set frreth2 up
ip link set frreth2out up
ip link set frreth3 up
ip link set frreth3out up
```
-------------------------------------------------------------------
3.Modify config and install VMs
-------------------------------------------------------------------
#### VSR1000.xml

    <disk type='file' device='disk'>
      <driver name='qemu' type='qcow2'/>
      ---<source file='/home/cx/images/VSR1000-1.qcow2'/>
      +++<source file='/Your DIR/VSR1000-1.qcow2'/>
      <target dev='vda' bus='virtio'/>
      <address type='pci' domain='0x0000' bus='0x00' slot='0x07' function='0x0'/>
    </disk>

#### ubuntu16.04.xml
```

    <disk type='file' device='disk'>
      <driver name='qemu' type='qcow2'/>
      ---<source file='/home/cx/images/ubuntu16.04-x86-frr.qcow2'/>
      +++<source file='/Your DIR/ubuntu16.04-x86-frr.qcow2'/>
      <target dev='vda' bus='virtio'/>
      <address type='pci' domain='0x0000' bus='0x00' slot='0x07' function='0x0'/>
    </disk>

```	

### centos7.xml
```

    <disk type='file' device='disk'>
      <driver name='qemu' type='qcow2'/>
      ---<source file='/home/cx/images/Centos7.0-x86_64-frr.qcow2'/>
      +++<source file='/Your DIR/Centos7.0-x86_64-frr.qcow2'/>
      <target dev='vda' bus='virtio'/>
      <address type='pci' domain='0x0000' bus='0x00' slot='0x06' function='0x0'/>
    </disk>
	
```	

### then run in Your DIR
```

virsh define VSR1000.xml
virsh define ubuntu16.04.xml
virsh define centos7.xml

```

### now you can access above two ACTORs from the virtual interface, such as vsreth0out, frreth0out...
---------------------------------------------------------------------
```

ACTOR2:
username:root
password:
ACTOR3:
username:root
password:

```



