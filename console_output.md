# Console outputs

I dump all the output that I need.
--------------------------------- 
### 06062023 19.17 VSC Terminal
```
DEVICE ID 0403:6001 on Bus 001 Address 006 =================
 bLength                :   0x12 (18 bytes)
 bDescriptorType        :    0x1 Device
 bcdUSB                 :  0x200 USB 2.0
 bDeviceClass           :    0x0 Specified at interface
 bDeviceSubClass        :    0x0
 bDeviceProtocol        :    0x0
 bMaxPacketSize0        :    0x8 (8 bytes)
 idVendor               : 0x0403
 idProduct              : 0x6001
 bcdDevice              :  0x600 Device 6.0
 iManufacturer          :    0x1 Error Accessing String
 iProduct               :    0x2 Error Accessing String
 iSerialNumber          :    0x3 Error Accessing String
 bNumConfigurations     :    0x1
  CONFIGURATION 1: 90 mA ===================================
   bLength              :    0x9 (9 bytes)
   bDescriptorType      :    0x2 Configuration
   wTotalLength         :   0x20 (32 bytes)
   bNumInterfaces       :    0x1
   bConfigurationValue  :    0x1
   iConfiguration       :    0x0
   bmAttributes         :   0xa0 Bus Powered, Remote Wakeup
   bMaxPower            :   0x2d (90 mA)
    INTERFACE 0: Vendor Specific ===========================
     bLength            :    0x9 (9 bytes)
     bDescriptorType    :    0x4 Interface
     bInterfaceNumber   :    0x0
     bAlternateSetting  :    0x0
     bNumEndpoints      :    0x2
     bInterfaceClass    :   0xff Vendor Specific
     bInterfaceSubClass :   0xff
     bInterfaceProtocol :   0xff
     iInterface         :    0x2 Error Accessing String
      ENDPOINT 0x81: Bulk IN ===============================
       bLength          :    0x7 (7 bytes)
       bDescriptorType  :    0x5 Endpoint
       bEndpointAddress :   0x81 IN
       bmAttributes     :    0x2 Bulk
       wMaxPacketSize   :   0x40 (64 bytes)
       bInterval        :    0x0
      ENDPOINT 0x2: Bulk OUT ===============================
       bLength          :    0x7 (7 bytes)
       bDescriptorType  :    0x5 Endpoint
       bEndpointAddress :    0x2 OUT
       bmAttributes     :    0x2 Bulk
       wMaxPacketSize   :   0x40 (64 bytes)
       bInterval        :    0x0
```
### 06062023 20.08 Zadig Drivers

```
libwdi:debug [wdi_create_list] USBSTOR USB device (4): USB\VID_18A5&PID_0420\WK3B02381
libwdi:debug [wdi_create_list] Device description: 'Portable Drive'
libwdi:debug [wdi_create_list] Hardware ID: USB\VID_0403&PID_6001&REV_0600
libwdi:debug [wdi_create_list] Compatible ID: USB\Class_FF&SubClass_FF&Prot_FF
libwdi:debug [wdi_create_list] Driver version: 2.12.36.4
```

### 06062023 20.14
```
libwdi:debug [wdi_create_list] USBSTOR USB device (4): USB\VID_18A5&PID_0420\WK3B02381
libwdi:debug [wdi_create_list] Device description: 'Portable Drive'
libwdi:debug [wdi_create_list] Hardware ID: USB\VID_0403&PID_6001&REV_0600
libwdi:debug [wdi_create_list] Compatible ID: USB\Class_FF&SubClass_FF&Prot_FF
libwdi:debug [wdi_create_list] Driver version: 6.1.7600.16385
libwdi:debug [wdi_create_list] WinUSB USB device (5): USB\VID_0403&PID_6001\AQ01UBVG
libwdi:debug [wdi_create_list] Device description: 'FT232R USB UART'
libwdi:debug [wdi_create_list] Hardware ID: USB\VID_0C45&PID_760A&REV_0112&MI_00
libwdi:debug [wdi_create_list] Compatible ID: USB\Class_03&SubClass_01&Prot_01
libwdi:debug [wdi_create_list] Driver version: 10.0.19041.2486
```