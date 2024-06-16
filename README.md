# lucky-prototype

(base) naotookawa@ookawanaoonnoMacBook-Air ~ % cd ~/.ssh
(base) naotookawa@ookawanaoonnoMacBook-Air .ssh % ssh -i ec2key.pem ec2-user@35.170.220.155
   ,     #_
   ~\_  ####_        Amazon Linux 2023
  ~~  \_#####\
  ~~     \###|
  ~~       \#/ ___   https://aws.amazon.com/linux/amazon-linux-2023
   ~~       V~' '->
    ~~~         /
      ~~._.   _/
         _/ _/
       _/m/'
Last login: Sun Jun 16 15:07:53 2024 from 101.110.36.201

[ec2-user@ip-172-31-29-123 ~]$ python3 -m venv myenv
[ec2-user@ip-172-31-29-123 ~]$ source myenv/bin/activate

(myenv) [ec2-user@ip-172-31-29-123 ~]$ cd app

(myenv) [ec2-user@ip-172-31-29-123 app]$ python __init__.py
 * Serving Flask app '__init__'
 * Debug mode: off
WARNING: This is a development server. Do not use it in a production deployment. Use a production WSGI server instead.
 * Running on all addresses (0.0.0.0)
 * Running on http://127.0.0.1:5000
 * Running on http://172.31.29.123:5000
Press CTRL+C to quit
101.110.36.201 - - [16/Jun/2024 15:27:32] "GET / HTTP/1.1" 200 -
