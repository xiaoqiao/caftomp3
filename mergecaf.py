# -*- coding:utf-8 -*-
#merge two caf to mp3 directly
#2014.4.27


import subprocess
import os
import glob
import time


def calcTime(filename):
    timestamp = os.path.getmtime(filename)


    return time.strftime("%Y%m%d%H%M%S",time.localtime(timestamp)) 

def mergecafs(featurecode,codeno):
    filename = 'callMic-' + featurecode + '.caf'
    #两个文件都存在的情况
    if codeno == 2:
        outname = filename.split('-')[1] + '_' + calcTime(filename) + '.mp3'
        theCommand = 'ffmpeg.exe -i callMic-'+ featurecode + '.caf -i callSpeaker-' + featurecode + '.caf -filter_complex amix=inputs=2:duration=longest:dropout_transition=3 -ac 2 -ab 64 -f mp3 ' + outname
    #只有一个文件的情况，分别判断是哪一个存在
    if codeno == 1:
        if os.path.exists(filename):
            pass
        else :
            filename = 'callSpeaker-' + featurecode + '.caf'
        outname = filename.split('-')[1] + '_' + calcTime(filename) + '.mp3'
        theCommand = 'ffmpeg.exe -i ' + filename + ' -filter_complex amix=inputs=1:duration=longest:dropout_transition=3 -ac 2 -ab 64 -f mp3 ' + outname
    subprocess.call(theCommand)    

def main():
    files = []
    featuredict = {}
    for filename in glob.glob('*.caf'):
        files.append(filename)
        featurecode = filename.split('-')[1] + '-' +filename.split('-')[2][:-4]
        print featurecode
        featuredict[featurecode] = featuredict.setdefault(featurecode,0)+1
    print featuredict
    for featurecode in featuredict:
        mergecafs(featurecode,featuredict[featurecode])





if __name__ == '__main__':
    main()


