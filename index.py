import subprocess

dpi = int(input("Enter desired dpi: "))
ps = subprocess.Popen(["echo Xft.dpi: {}".format(dpi)], shell = True, stdout=subprocess.PIPE)
output = subprocess.check_output(('xrdb', '-merge'), stdin=ps.stdout)
ps.wait()
print("DPI changed, you need to restart open apps for the changes to take effect!")
