# -*- coding:utf-8 -*-
#convert caf to wav
#merge two wavs
#to mp3

import subprocess
import os
import glob
import time


def calcTime(filename):
    timestamp = os.path.getmtime(filename)


    return time.strftime("%Y%m%d%H%M%S",time.localtime(timestamp)) 

def cafTowav(filename):
    if 'Mic' in filename:
        ftime = filename.split('-')[1] + '_' + calcTime(filename) 
        wavname = filename[:-4] + '.wav'
        print wavname
        #把mic的文件转换好
        theCommand = 'ffmpeg.exe -i ' + filename + ' ' + wavname
        returncode = subprocess.call(theCommand)
        #把Speaker的文件转换好
        filename2 = filename[:4] + 'Speaker' + filename[7:]
        wavname2 = filename2[:-4] + '.wav'

        theCommand = 'ffmpeg.exe -i ' + filename2 + ' ' + wavname2
        print theCommand
        returncode = subprocess.call(theCommand)

        #Audio Recorder软件命名的一个特征码
        featurecode = filename[8:-4]

        return featurecode,ftime
    else :
        return None,None

def mergeTwo(featurecode,ftime):
    if featurecode != None:
        name1 = 'callMic-' + featurecode + '.wav'
        name2 = 'callSpeaker-' + featurecode + '.wav'
        outname = ftime + '.mp3'
        theCommand = 'ffmpeg.exe -i ' + name1 + ' -i ' + name2 + ' -filter_complex amix=inputs=2:duration=longest:dropout_transition=3 -ac 2 -ab 64 -f mp3 '+ outname
        returncode = subprocess.call(theCommand)

    
def clean(filename):
    if 'Mic' in filename:
        deletename1 = filename[:-4] + '.wav'
        deletename2 = filename[:4] + 'Speaker' + filename[7:-4] + '.wav' 
         
        os.remove(deletename1)
        os.remove(deletename2)

def main():
    print 'start'
    for filename in glob.glob('*.caf'):
        #print calcTime(filename)
        print 'process'
        print filename
        featurecode,ftime = cafTowav(filename)
        print 'merging'
        mergeTwo(featurecode,ftime)
        clean(filename)


if __name__ == '__main__':
    main()