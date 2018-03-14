import numpy as np
import subprocess


def chunk_test(params, loop_iter):
    hf16_wr = open('test_results/HF_1M_%i_chunking_write.txt' % params[1], 'wb')
    vl16_wr = open('test_results/VL_1M_%i_chunking_write.txt' % params[1], 'wb')

    hf16_re = open('test_results/HF_1M_%i_chunking_read.txt' % params[1], 'wb')
    vl16_re = open('test_results/VL_1M_%i_chunking_read.txt' % params[1], 'wb')


    for i in range(loop_iter):
        print(i)
        vlwr = subprocess.run("./VLWrite /nvme5n1/vldata.h5 %i %i %i" % (params[0], params[1], params[2]), shell=True, stderr=subprocess.PIPE, stdout=subprocess.PIPE)
        subprocess.call('echo 3 | sudo tee /proc/sys/vm/drop_caches', shell=True)
        vlre = subprocess.run("./VLRead /nvme5n1/vldata.h5 %i" % i, shell=True, stderr=subprocess.PIPE, stdout=subprocess.PIPE)


        hfwr = subprocess.run("./HFWrite /nvme5n1/hfdata.h5 %i %i %i" % (params[0], params[1], params[2]), shell=True, stderr=subprocess.PIPE, stdout=subprocess.PIPE)
        subprocess.call('echo 3 | sudo tee /proc/sys/vm/drop_caches', shell=True)
        hfre = subprocess.run("./HFRead /nvme5n1/hfdata.h5 %i" % i, shell=True, stderr=subprocess.PIPE, stdout=subprocess.PIPE)

        vl16_wr.write(vlwr.stdout)
        hf16_wr.write(hfwr.stdout)
        vl16_re.write(vlre.stdout)
        hf16_re.write(hfre.stdout)


    hf16_wr.close()
    vl16_wr.close()
    hf16_re.close()
    vl16_re.close()


loop_iter = 64

params = [10000,16,1000000]
chunk_test(params, loop_iter)

params = [10000,1024,1000000]
chunk_test(params, loop_iter)
