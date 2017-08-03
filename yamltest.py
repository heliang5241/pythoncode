- hosts: all
  remote_user: root
  gather_facts:True
  tasks:
- name: install apache on CentOS
    yum: name=httpd state=present
    when: ansible_os_family =="CentOS"
- name: install apache on Debian
    yum: name=apache2 state=present
    when: ansible_os_family =="Debian"


