#!/bin/bash

USERNAME="InputYourUsernameHere"
PASSWORD="InputYourPasswordHere"

htpasswd -c .htpasswd $USERNAME $PASSWORD

echo "Created .htpasswd with user $USERNAME"