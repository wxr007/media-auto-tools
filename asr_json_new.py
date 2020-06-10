import baidu_interface
import json

# 需要识别的文件
AUDIO_FILE = './audio/16k.pcm'  # 只支持 pcm/wav/amr 格式，极速版额外支持m4a 格式
# 文件格式
FORMAT = AUDIO_FILE[-3:]  # 文件后缀只支持 pcm/wav/amr 格式，极速版额外支持m4a 格式

#毫秒换算 根据需要只到分
def ms2s(ms):
    mspart=ms%1000
    mspart=str(mspart).zfill(3)
    spart=(ms//1000)%60
    spart=str(spart).zfill(2)
    mpart=(ms//1000)//60
    mpart=str(mpart).zfill(2)
    #srt的时间格式
    stype="00:"+mpart+":"+spart+","+mspart
    return stype

'''
def format_time(ms):
    # ms = millisecond%1000
    # second = millisecond/1000
    # hour = millisecond/
    td = datetime.timedelta(milliseconds= ms)
    return str(td).replace('.',',')
'''

def gen_srt(srt_file,sound,timestamp_list,token):
    idx = 0
    text = []
    for i in range(len(timestamp_list)):
        #d = timestamp_list[i][1] - timestamp_list[i][0]
        data = sound[timestamp_list[i][0]:timestamp_list[i][1]].raw_data
        str_rst = baidu_interface.asr_raw(data, token, FORMAT, AUDIO_FILE)
        result = json.loads(str_rst)
        # print("rst is ", result)
        # print("rst is ", rst['err_no'][0])
        
        if result['err_no'] == 0:
            text.append('{0}\n{1} --> {2}\n'.format(idx, ms2s(timestamp_list[i][0]), ms2s(timestamp_list[i][1])))
            text.append( result['result'][0])
            text.append('\n')
            idx = idx + 1
            print(ms2s(timestamp_list[i][0]), "txt is ", result['result'][0])

    with open(srt_file,"r+") as f:
        f.writelines(text)


if __name__ == '__main__':
    token = baidu_interface.fetch_token()

    speech_data = []
    with open(AUDIO_FILE, 'rb') as speech_file:
        speech_data = speech_file.read()

    result_str = baidu_interface.asr_raw(speech_data,token,FORMAT,AUDIO_FILE)

    print(result_str)
    with open("result.txt","w") as of:
        of.write(result_str)
