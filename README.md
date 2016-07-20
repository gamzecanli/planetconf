# planetconf
"planetconf" uygulaması , www.planetplanet.org ile kurulan planet aracının yapılandırmasını web arayüzünden yapılmasını sağlamaktadır. 
Oluşturulan arayüzde planet_name, planet_directory_name, blogger_name, blogger_link gibi bilgiler alınır.

Virtual Environment Kurulumu

myvenv isimli sanal ortam aşağıdaki gibi kurulabilir;

Windows 
C:\Python34\python -m venv myvenv

GNU/Linux ve OS X
$ python3 -m venv myvenv

Django Kurulumu

Önce sanal ortam aktif edilir;

Windows
myvenv\Script\acvivate

Linux and OS X
$ source myvenv/bin/activate

Sonra django kurulur;
pip install django
