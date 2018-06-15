from urllib import request, parse

url = 'http://fanyi.baidu.com/v2transapi'

data = {
    'from': 'en',
    'query': 'u',
    'sign': '790052.584981',
    'simple_means_flag': 3,
    'to': 'zh',
    'token': '05b7466793e40ef7f8aa23c4cf5526bc',
    'transtype': 'realtime',
}

params = parse.urlencode(data)

header = {
    'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:60.0) Gecko/20100101 '
                      'Firefox/60.0Accept: text/html,application/xhtml+xml,'
                      'application/xml;q=0.9,*/*;q=0.8z',
    'Cookie': 'BAIDUID=D643FE534229AC1D6486D6AF4C74CE6D:FG=1; BIDUPSID=56C0F16F89D026183484D10AE69E7A6F; PSTM=1528608978; BDORZ=B490B5EBF6F3CD402E515D22BCDA1598; BDUSS=lJHeTkzekFCcFhXa2hWNGFXOXlUN2piTG5EWTVKZW5RbFpGRzVkT1hKVjRiRWRiQVFBQUFBJCQAAAAAAAAAAAEAAABkjUJAYWJ1c2V5ZWFyAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAHjfH1t43x9bf; locale=zh; from_lang_often=%5B%7B%22value%22%3A%22zh%22%2C%22text%22%3A%22%u4E2D%u6587%22%7D%2C%7B%22value%22%3A%22en%22%2C%22text%22%3A%22%u82F1%u8BED%22%7D%5D; to_lang_often=%5B%7B%22value%22%3A%22en%22%2C%22text%22%3A%22%u82F1%u8BED%22%7D%2C%7B%22value%22%3A%22zh%22%2C%22text%22%3A%22%u4E2D%u6587%22%7D%5D; REALTIME_TRANS_SWITCH=1; FANYI_WORD_SWITCH=1; HISTORY_SWITCH=1; SOUND_SPD_SWITCH=1; SOUND_PREFER_SWITCH=1; Hm_lvt_64ecd82404c51e03dc91cb9e8c025574=1528856438,1528858116; Hm_lpvt_64ecd82404c51e03dc91cb9e8c025574=1528860905; H_PS_PSSID=1461_21113_26580_22075; BDRCVFR[feWj1Vr5u3D]=I67x6TjHwwYf0; PSINO=1'
}

req = request.Request(url, params.encode(), header)
resp = request.urlopen(req)
print(resp.read().decode())
