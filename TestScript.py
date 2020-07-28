import pickle
import base64
import sys
import subprocess
import time

YOUR_BASEPATH = ''

def info(s):
    print('[Info] {}'.format(s))

def fatal(s):
    print('[FATAL ERROR] {}'.format(s))
    sys.exit(0)

def judge(testcase):
    process = subprocess.Popen(['make', 'build'], cwd=YOUR_BASEPATH, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL, stdin=subprocess.PIPE)
    build_timeout = 5
    testname, inputctx, retcode, inputcode = testcase
    process.communicate(inputcode)
    start_time = time.time()
    while process.poll() is not None and time.time() - start_time < build_timeout:
        pass
    try:
        process.terminate()
    except Exception as identifier:
        info('Terminating processing with following error: {}'.format(identifier))
    process = subprocess.Popen(['make', 'simulate'], cwd=YOUR_BASEPATH, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL, stdin=subprocess.PIPE)
    simulating_timeout = 10
    process.communicate(inputctx + '\n')
    start_time = time.time()
    while process.poll() is not None and time.time() - start_time < simulating_timeout:
        pass
    try:
        process.terminate()
    except Exception as identifier:
        info('Terminating processing with following error: {}'.format(identifier))
    user_ret = process.returncode
    if user_ret == retcode:
        print('[PASS] {}'.format(testname))
        return True
    else:
        print('[FAIL] {}'.format(testname))
        return False
    

testdata = "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PSBiICsgMTsgYiA8PSBOCjE5ICBMRVQgYyA9IDEKMjAgICAgRk9SIGMgPSBjICsgMTsgYyA8PSBOCjIxICAgICAgTEVUIGQgPSAxCjIyICAgICAgRk9SIGQgPSBkICsgMTsgZCA8PSBOCjIzICAgICAgICBMRVQgZSA9IDEKMjQgICAgICAgIEZPUiBlID0gZSArIDE7IGUgPD0gTgoyNSAgICAgICAgICBMRVQgZiA9IDEKMjYgICAgICAgICAgRk9SIGYgPSBmICsgMTsgZiA8PSBOCjI3ICAgICAgICAgICAgSUYgKGE9PWIgfHwgYT09YyB8fCAgYT09ZCB8fCAgYT09ZSB8fCAgYT09ZiB8fCAgYT09aCB8fCAgYT09aSB8fCAgYT09aiB8fCAgYT09ayB8fCAgYj09YyB8fCAgYj09ZCB8fCAgYj09ZSB8fCAgYj09ZiB8fCAgYj09aCB8fCAgYj09aSB8fCAgYj09aiB8fCAgYj09ayB8fCAgYz09ZCB8fCAgYz09ZSB8fCAgYz09ZiB8fCAgYz09aCB8fCAgYz09aSB8fCAgYz09aiB8fCAgYz09ayB8fCAgZD09ZSB8fCAgZD09ZiB8fCAgZD09aCB8fCAgZD09aSB8fCAgZD09aiB8fCAgZD09ayB8fCAgZT09ZiB8fCAgZT09aCB8fCAgZT09aSB8fCAgZT09aiB8fCAgZT09ayB8fCAgZj09aCB8fCAgZj09aSB8fCAgZj09aiB8fCAgZj09ayB8fCAgaT09aiB8fCAgaD09aykgVEhFTiAyNAoyOCAgICAgICAgICAgIExFVCB0b3RhbCA9IHRvdGFsICsgMQoyOSAgICAgICAgICBFTkQgRk9SCjMwICAgICAgICBFTkQgRk9SCjMxICAgICAgRU5EIEZPUiAKMzIgICAgRU5EIEZPUgozMyAgRU5EIEZPUgozNCBFTkQgRk9SCjM1IEVYSVQgdG90YWwKcSd0cSgoWA0AAABjb250cm9sXzIudHh0cSlYAQAAADZxKksGWHcAAAAxIFJFTSBjb250cm9sXzIudHh0CjIgUkVNIGlucHV0OiA2CjMgUkVNIHJldHVybiB2YWx1ZTogNgo1IElOUFVUIG4KNyBJRiBuID4gNSBUSEVOIDExCjggTEVUIG4gPSA1CjEwIEVYSVQgbgoxMSBH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QSArIEIpICsgKEMgLSBBICsgQikpIC0gKEEgKyBCKSkgKyAoKChDIC0gQSArIEIpIC0gKEEgKyBCKSkgKyAoQyAtIEEgKyBCKSkpIC0gKCgoKEEgKyBCKSArIChDIC0gQSArIEIpKSAtIChBICsgQikpICsgKCgoQyAtIEEgKyBCKSAtIChBICsgQikpICsgKEMgLSBBICsgQikpKSkpKSAtICgoKCgoKChBICsgQikgKyAoQyAtIEEgKyBCKSkgLSAoKEEgKyBCKSArIChDIC0gQSArIEIpKSkgLSAoKChBICsgQikgKyAoQyAtIEEgKyBCKSkgLSAoQSArIEIpKSkgKyAoKCgoQyAtIEEgKyBCKSAtIChBICsgQikpICsgKEMgLSBBICsgQikpIC0gKCgoQSArIEIpICsgKEMgLSBBICsgQikpIC0gKEEgKyBCKSkpKSArICgoKCgoQyAtIEEgKyBCKSAtIChBICsgQikpICsgKEMgLSBBICsgQikpIC0gKCgoQSArIEIpICsgKEMgLSBBICsgQikpIC0gKEEgKyBCKSkpICsgKCgoKEMgLSBBICsgQikgLSAoQSArIEIpKSArIChDIC0gQSArIEIpKSAtICgoKEEgKyBCKSArIChDIC0gQSArIEIpKSAtIChBICsgQikpKSkpICsgKCgoKCgoQyAtIEEgKyBCKSAtIChBICsgQikpICsgKChDIC0gQSArIEIpIC0gKEEgKyBCKSkpICsgKCgoQyAtIEEgKyBCKSAtIChBICsgQikpICsgKEMgLSBBICsgQikpKSAtICgoKChBICsgQikgKyAoQyAtIEEgKyBCKSkgLSAoQSArIEIpKSArICgoKEMgLSBBICsgQikgLSAoQSArIEIpKSArIChDIC0gQSArIEIpKSkpIC0gKCgoKChBICsgQikgKyAoQyAtIEEgKyBCKSkgLSAoQSArIEIpKSArICgoKEMgLSBBICsgQikgLSAoQSArIEIpKSArIChDIC0gQSArIEIpKSkgLSAoKCgoQSArIEIpICsgKEMgLSBBICsgQikpIC0gKEEgKyBCKSkgKyAoKChDIC0gQSArIEIpIC0gKEEgKyBCKSkgKyAoQyAtIEEgKyBCKSkpKSkpKQo4IEVYSVQgQQpxPXRxPihYCAAAAG9wXzMudHh0cT9YAwAAADQgNnFA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"

test_cases = pickle.loads(base64.b64decode(testdata.encode()))
info('Test cases count: {}'.format(len(test_cases)))
if len(YOUR_BASEPATH) == 0:
    fatal('Base path error.')

for i in test_cases:
    result = judge(i)
    if not result:
        print('TEST FAILED')
        sys.exit(0)

print('PASSED ALL')