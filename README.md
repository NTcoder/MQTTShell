# MQTTShell
This is a very simple app which gives one device, command line interface similar to SSH of second device using a MQTT connection.

This program can be used to connect to a remote device to which you dont have access through SSH (becuase of network connectivity/firewalls/Private IP).

To run this app, a Public MQTT server is required or you can use the Public MQTT sandbox of your choice. 


## How To Use :
1. Decide on the MQTT broker you want to use or a Public MQTT broker of your choice.
2. Note the MAC id of the deivce you want to access remotely, since that is the unique ide through which a device is identified.
3. Run the Diagnostice client remotely and enter the device id of the remote device and Enjoy!


## Warning!

Use of this app can be dangerous if :
1. If you fire some deadly command remotely and the Utility is running as a sudo or admin user.
2. If you are using a public MQTT sandbox, this can posses a security risk as your device becomes accessible through mac id and authetication.

## TO - DO

Improve authetication feature, security and reliability.
