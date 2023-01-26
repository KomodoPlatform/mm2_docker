On launch, the latest coins file & mm2 binary release will be downloaded. The MM2.json and userpass file will be created if not existing.


### Note on Using Docker with UFW:

Docker does not respect UFW - https://www.techrepublic.com/article/how-to-fix-the-docker-and-ufw-security-flaw/

To mitigate this flaw, make sure to do the following:

Got to docker config with `sudo nano /etc/default/docker` and add the following line:

`DOCKER_OPTS="--iptables=false"`

Save and close the file, then restart the docker daemon with `sudo systemctl restart docker`