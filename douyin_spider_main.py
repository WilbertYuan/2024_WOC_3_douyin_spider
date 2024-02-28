'''




2024  ----  WOC  ----  第3题

本程序实现了对抖音热榜以及所有分区中的一个视频进行爬取的操作

但该程序存在着一些不可避免的系统性瑕疵,一般情况下不能够被完\
全执行,所以可以提取大约3个视频,如出现报错可以重新运行程序。

B23042424---袁浩宽





'''

import requests
import pandas as pd
import datetime
import re
import time

def getvideo (url,headers):

    res2 = ''
    compile_pat = ''
    target = ''
    path = ''
    video = ''

    res2 = requests.get(url, headers=headers).text
    #print(res2)
    compile_pat = re.compile('"url_list":\["http://v3-web.douyinvod.com/(.*?)\\\\')
    time.sleep(3)
    target = compile_pat.search(res2)
    time.sleep(3)
    path = 'http://v3-web.douyinvod.com/' + target.group(1)    #在多次实验中我发现此行代码经常报错，原因不明，在后面加入time.sleep后让它减少了报错的几率，如果你在终端中的报错信息里看到了这句话，请将文件夹内除此python文件以外的文件删除并重新试一次
    time.sleep(8)
    video = requests.get(path, headers=headers).content      
    time.sleep(8)
    return video


headers = {
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko)\
          Chrome/122.0.0.0',
    'Cookie': 'ttwid=1%7Cnj9lCO_qxHljn-9vEhkpNyeyEK7G9Ze1l0cDgGnWTqA%7C1708952656%7Ced24babc95f5f802f4d5659314a827811bd780340d224e5cf75c7ff3ff169231; douyin.com; device_web_cpu_core=20; device_web_memory_size=8; architecture=amd64; IsDouyinActive=true; dy_swidth=1536; dy_sheight=864; stream_recommend_feed_params=%22%7B%5C%22cookie_enabled%5C%22%3Atrue%2C%5C%22screen_width%5C%22%3A1536%2C%5C%22screen_height%5C%22%3A864%2C%5C%22browser_online%5C%22%3Atrue%2C%5C%22cpu_core_num%5C%22%3A20%2C%5C%22device_memory%5C%22%3A8%2C%5C%22downlink%5C%22%3A10%2C%5C%22effective_type%5C%22%3A%5C%224g%5C%22%2C%5C%22round_trip_time%5C%22%3A50%7D%22; csrf_session_id=850bc1dbbc9acfad0b28e8b18a0238b5; FORCE_LOGIN=%7B%22videoConsumedRemainSeconds%22%3A180%7D; strategyABtestKey=%221708952657.842%22; stream_player_status_params=%22%7B%5C%22is_auto_play%5C%22%3A0%2C%5C%22is_full_screen%5C%22%3A0%2C%5C%22is_full_webscreen%5C%22%3A0%2C%5C%22is_mute%5C%22%3A1%2C%5C%22is_speed%5C%22%3A1%2C%5C%22is_visible%5C%22%3A1%7D%22; volume_info=%7B%22isUserMute%22%3Afalse%2C%22isMute%22%3Atrue%2C%22volume%22%3A0.7%7D; passport_csrf_token=edc6d9945c4ea34797ecf272bae07c79; passport_csrf_token_default=edc6d9945c4ea34797ecf272bae07c79; bd_ticket_guard_client_data=eyJiZC10aWNrZXQtZ3VhcmQtdmVyc2lvbiI6MiwiYmQtdGlja2V0LWd1YXJkLWl0ZXJhdGlvbi12ZXJzaW9uIjoxLCJiZC10aWNrZXQtZ3VhcmQtcmVlLXB1YmxpYy1rZXkiOiJCRDhYaU5Gd3VvdzltemVyc1hlSTZObzlMRHV4c2p2eWRJbm1KUVBxMjdHbk1sN0lCYWV5bFlZV2U5VG9ibHFCRUphbFIyZ0dnVWlJQTh1RVlQY29jM0k9IiwiYmQtdGlja2V0LWd1YXJkLXdlYi12ZXJzaW9uIjoxfQ%3D%3D; bd_ticket_guard_client_web_domain=2; msToken=rYrQbsV2SMGaKq3uE0koyuuVjF4VTHk2HdowBc-1kd6tp70oqgYZUTqbd5T1IFTBjrg9x7d1aqCOoWGRGHjfkElyK1g6pAdpHoxD6zXZY2xz2k_2tw==; ttcid=75318070be254f468de87cc041a8e0ae22; tt_scid=1erKKf.pnkeU241xxqW6hht4-hek0FlOCreNOiPVLuAG9MCJPoYUH61Ck4oIaAN-46cd; home_can_add_dy_2_desktop=%221%22; odin_tt=b98172f49b8f4ff8e4606acbb1a4c4233ed00e83dd11700d829ccff1775b4ff3bcee314c3aedff46afcebcdd36f3c00c3972cd5629c0c018eec1b8a3907959ee8b379ce7e8764924901b99d86a125a4e; msToken=D7Ip2pmMTp4KtBKiXPrXMxGy6SEoPTaZS6yUx8szzmAxDqG9PWcJtY-TOrO3uu-juyTEb3-kestL8p-MYBlP65_FJZ9GvsOI5TzHg_E-WmPXFe9yyw==',
    'Accept': 'application/json, text/plain, */*',
    'Accept-Encoding': 'gzip, deflate',
    'Host': 'www.douyin.com',
    'Accept-Language': 'zh-CN,zh-Hans;q=0.9',
    'Referer': 'https://www.douyin.com/hot',
    'Connection': 'keep-alive'
}

headers2 = {
'path':
'/aweme/v1/web/channel/feed/?device_platform=webapp&aid=6383&channel=channel_pc_web&count=16&tag_id=300213&Seo-Flag=0&refresh_index=1&awemePcRecRawData=%7B%22is_client%22:false%7D&pc_client_type=1&version_code=170400&version_name=17.4.0&cookie_enabled=true&screen_width=1536&screen_height=864&browser_language=zh-CN&browser_platform=Win32&browser_name=Edge&browser_version=122.0.0.0&browser_online=true&engine_name=Blink&engine_version=122.0.0.0&os_name=Windows&os_version=10&cpu_core_num=20&device_memory=8&platform=PC&downlink=10&effective_type=4g&round_trip_time=100&webid=7339895700894778892&msToken=QpiSJvOT_M6j17kZqayLaBDrIFQ_vabH_LfxPu8Mi41-RRErCcf6s9U4x1LriAj2Xp5wvXqKgsjVlTc_5fqO0JHYXB8PW824m2WIHEtO1et5Nt7dd989sQ82XlYH&X-Bogus=DFSzswVuQMGANtwbtoYqFmD4OF6f'
,'scheme':
'https'
,'Accept':
'application/json, text/plain, */*'
,'Accept-Language':
'zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6'
,'Cookie':
'ttwid=1%7Cnj9lCO_qxHljn-9vEhkpNyeyEK7G9Ze1l0cDgGnWTqA%7C1708952656%7Ced24babc95f5f802f4d5659314a827811bd780340d224e5cf75c7ff3ff169231; dy_swidth=1536; dy_sheight=864; volume_info=%7B%22isUserMute%22%3Afalse%2C%22isMute%22%3Atrue%2C%22volume%22%3A0.7%7D; passport_csrf_token=edc6d9945c4ea34797ecf272bae07c79; passport_csrf_token_default=edc6d9945c4ea34797ecf272bae07c79; bd_ticket_guard_client_web_domain=2; ttcid=75318070be254f468de87cc041a8e0ae22; pwa2=%220%7C0%7C3%7C0%22; xgplayer_user_id=302488976231; FORCE_LOGIN=%7B%22videoConsumedRemainSeconds%22%3A180%2C%22isForcePopClose%22%3A1%7D; passport_assist_user=CkEfgDT8ShQA4Li1ituh1mwlPlSlkrpQyZ-PfT9gli8vvb8edoAGdDl4xUpXILfUoLXAaJFH_wqt2zlPak1TejfvvRpKCjzOBrDB3wz4-MFZ_kaxxm0jLWjgvejDl_9NvwmAHBaLAUMY0loxTjRoSWvj7kuGfaF5QrtnwkjlWCoUcvoQ8sLKDRiJr9ZUIAEiAQNmF078; n_mh=2Z7slYKYyBcIzrgw4tUlZX0eCuq7YVaKoqsVyXb-imE; sso_uid_tt=b3a38138a6cd506cfab39609041ca648; sso_uid_tt_ss=b3a38138a6cd506cfab39609041ca648; toutiao_sso_user=d1f1ddb0e23d9838aadd2b32a0c22360; toutiao_sso_user_ss=d1f1ddb0e23d9838aadd2b32a0c22360; sid_ucp_sso_v1=1.0.0-KDI0YTE5ZGE5NTlmZDcxNGY2N2VlOTFmNDIwOTVlN2U3ZWEwNTkxMWUKHwjrl4Dnvc3GAxCjtveuBhjvMSAMMMqd960GOAZA9AcaAmxxIiBkMWYxZGRiMGUyM2Q5ODM4YWFkZDJiMzJhMGMyMjM2MA; ssid_ucp_sso_v1=1.0.0-KDI0YTE5ZGE5NTlmZDcxNGY2N2VlOTFmNDIwOTVlN2U3ZWEwNTkxMWUKHwjrl4Dnvc3GAxCjtveuBhjvMSAMMMqd960GOAZA9AcaAmxxIiBkMWYxZGRiMGUyM2Q5ODM4YWFkZDJiMzJhMGMyMjM2MA; passport_auth_status=04359abfc18966fb36e3a6378d65f43c%2C; passport_auth_status_ss=04359abfc18966fb36e3a6378d65f43c%2C; uid_tt=fb6fa787e2bd8a2af60c1576662a92ea; uid_tt_ss=fb6fa787e2bd8a2af60c1576662a92ea; sid_tt=c27b5c82dc5a3e775153b79db2ae0c99; sessionid=c27b5c82dc5a3e775153b79db2ae0c99; sessionid_ss=c27b5c82dc5a3e775153b79db2ae0c99; publish_badge_show_info=%220%2C0%2C0%2C1709038377011%22; LOGIN_STATUS=1; _bd_ticket_crypt_doamin=2; _bd_ticket_crypt_cookie=a2d478b3b43c5408a79e84a49fe6a929; __security_server_data_status=1; store-region=cn-js; store-region-src=uid; douyin.com; device_web_cpu_core=20; device_web_memory_size=8; architecture=amd64; csrf_session_id=850bc1dbbc9acfad0b28e8b18a0238b5; strategyABtestKey=%221709100609.267%22; sid_guard=c27b5c82dc5a3e775153b79db2ae0c99%7C1709100609%7C5121765%7CSat%2C+27-Apr-2024+12%3A52%3A54+GMT; sid_ucp_v1=1.0.0-KDI2MDAwZGM2YjBkNTE3YzY1ODM2Mzc3M2U0MzUyNmYxNGUzNzE5YWIKGwjrl4Dnvc3GAxDBnPuuBhjvMSAMOAZA9AdIBBoCbHEiIGMyN2I1YzgyZGM1YTNlNzc1MTUzYjc5ZGIyYWUwYzk5; ssid_ucp_v1=1.0.0-KDI2MDAwZGM2YjBkNTE3YzY1ODM2Mzc3M2U0MzUyNmYxNGUzNzE5YWIKGwjrl4Dnvc3GAxDBnPuuBhjvMSAMOAZA9AdIBBoCbHEiIGMyN2I1YzgyZGM1YTNlNzc1MTUzYjc5ZGIyYWUwYzk5; xg_device_score=7.6993270604411235; download_guide=%223%2F20240227%2F1%22; stream_player_status_params=%22%7B%5C%22is_auto_play%5C%22%3A0%2C%5C%22is_full_screen%5C%22%3A0%2C%5C%22is_full_webscreen%5C%22%3A0%2C%5C%22is_mute%5C%22%3A1%2C%5C%22is_speed%5C%22%3A1%2C%5C%22is_visible%5C%22%3A1%7D%22; my_rd=2; __ac_nonce=065dee37c000fdc407b0e; __ac_signature=_02B4Z6wo00f01AjAL2AAAIDA.qkmReEk6tgI4CvAAGf1oGYuPME5eRMCt6mW9t5Oj6dtliwXPiWX1r6w46phlGjr7ITpSuLdKSxOMRb555a1nJkhct7ufApJHuphug4Qbiaxxw0SXU9.at7J1c; stream_recommend_feed_params=%22%7B%5C%22cookie_enabled%5C%22%3Atrue%2C%5C%22screen_width%5C%22%3A1536%2C%5C%22screen_height%5C%22%3A864%2C%5C%22browser_online%5C%22%3Atrue%2C%5C%22cpu_core_num%5C%22%3A20%2C%5C%22device_memory%5C%22%3A8%2C%5C%22downlink%5C%22%3A10%2C%5C%22effective_type%5C%22%3A%5C%224g%5C%22%2C%5C%22round_trip_time%5C%22%3A100%7D%22; bd_ticket_guard_client_data=eyJiZC10aWNrZXQtZ3VhcmQtdmVyc2lvbiI6MiwiYmQtdGlja2V0LWd1YXJkLWl0ZXJhdGlvbi12ZXJzaW9uIjoxLCJiZC10aWNrZXQtZ3VhcmQtcmVlLXB1YmxpYy1rZXkiOiJCRDhYaU5Gd3VvdzltemVyc1hlSTZObzlMRHV4c2p2eWRJbm1KUVBxMjdHbk1sN0lCYWV5bFlZV2U5VG9ibHFCRUphbFIyZ0dnVWlJQTh1RVlQY29jM0k9IiwiYmQtdGlja2V0LWd1YXJkLXdlYi12ZXJzaW9uIjoxfQ%3D%3D; home_can_add_dy_2_desktop=%221%22; msToken=iKczAtI413YZ7KiFcOFO-5NFr0LGF_USbdADySlVp7zuVThdDsrhHP0a6s_q5uRySMxkeoiXuKDFt-tNGNG164ZnBUzhFycoCuwB0AzzkHuLPYu13SoX1KXKVp0p; tt_scid=vbYscDJ6G9DMj5PsCFZUgk8uh-pP0t3ltBHbIgkCd47i7J6hG2KsEgkABTq3Ti3Z5495; passport_fe_beating_status=true; odin_tt=e068cd48bf028c56eb30a3fa4d1f4fc5db6ab0e3c4bfa284b74b3020ffb1e47fde1e367224bf91816904f4728e681cb6781eb31975d2f435ea89c9b90dfd0e9e; _tea_utm_cache_1243=undefined; MONITOR_WEB_ID=ed0bdd13-2389-4a4c-9d5f-ea21402ade76; msToken=QpiSJvOT_M6j17kZqayLaBDrIFQ_vabH_LfxPu8Mi41-RRErCcf6s9U4x1LriAj2Xp5wvXqKgsjVlTc_5fqO0JHYXB8PW824m2WIHEtO1et5Nt7dd989sQ82XlYH; IsDouyinActive=true'
,'Referer':
'https://www.douyin.com/channel/300203'
,'User-Agent':
'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36 Edg/122.0.0.0'
}
headers3 = {
    'Referer': 'https://www.douyin.com/channel/300205',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36',
    'Cookie': 'ttwid=1%7CBuhkbYw7_gcVbYvpjZ6DpemgJujaliaArP0V3thgxHo%7C1707911268%7C810aeb71aaaddc9c99b1ae12b82db86c989e6e5415f31cb778bf54ba172f1df3; dy_swidth=1536; dy_sheight=864; volume_info=%7B%22isUserMute%22%3Afalse%2C%22isMute%22%3Atrue%2C%22volume%22%3A0.5%7D; passport_csrf_token=6b6815730c09426eb9d9535e3644add1; passport_csrf_token_default=6b6815730c09426eb9d9535e3644add1; stream_player_status_params=%22%7B%5C%22is_auto_play%5C%22%3A0%2C%5C%22is_full_screen%5C%22%3A0%2C%5C%22is_full_webscreen%5C%22%3A0%2C%5C%22is_mute%5C%22%3A1%2C%5C%22is_speed%5C%22%3A1%2C%5C%22is_visible%5C%22%3A1%7D%22; xgplayer_user_id=481351203845; bd_ticket_guard_client_web_domain=2; ttcid=1286122a90134de18a9e4842dd20002412; FORCE_LOGIN=%7B%22videoConsumedRemainSeconds%22%3A180%2C%22isForcePopClose%22%3A1%7D; n_mh=a3qKpgw_wY4VIjqCQaHfjOESIHAdtV5c86zW4X1cJpU; sso_auth_status=3751f307fe7884eaa185997f31a6b0b7; sso_auth_status_ss=3751f307fe7884eaa185997f31a6b0b7; publish_badge_show_info=%220%2C0%2C0%2C1708002486368%22; LOGIN_STATUS=1; store-region=cn-js; store-region-src=uid; _bd_ticket_crypt_doamin=2; __security_server_data_status=1; my_rd=2; pwa2=%220%7C0%7C3%7C0%22; passport_assist_user=CkFQ1DguP3SQiueS2-i_G8yxRk3nzCT8lsdazX2IwMZMc7NNJVpHdJsuV4Kdurf4ND2DkoS4QUoSIltdf0lJ9pDYUhpKCjwF42mRQ8mV4wzP7WsRuPFCYIELIGdQ0IWaCG4LqV-VE6p5QEKRKoGOfHo-TClQsVK6OGrTa5wwB5FxnL4QnbrJDRiJr9ZUIAEiAQNrpuE5; sso_uid_tt=5d76a41394c86a31085db7de562ca21e; sso_uid_tt_ss=5d76a41394c86a31085db7de562ca21e; toutiao_sso_user=6f5c61e6c5bcd4ab8b145c0f8433b362; toutiao_sso_user_ss=6f5c61e6c5bcd4ab8b145c0f8433b362; sid_ucp_sso_v1=1.0.0-KDI2YjIyMGU1NjBlMDg2MDQ4NmQ1N2YzMjMwM2UyOGUyYzFjNWViODUKHwinmrC3ro2oAxDGr7iuBhjvMSAMMMniuYUGOAZA9AcaAmxxIiA2ZjVjNjFlNmM1YmNkNGFiOGIxNDVjMGY4NDMzYjM2Mg; ssid_ucp_sso_v1=1.0.0-KDI2YjIyMGU1NjBlMDg2MDQ4NmQ1N2YzMjMwM2UyOGUyYzFjNWViODUKHwinmrC3ro2oAxDGr7iuBhjvMSAMMMniuYUGOAZA9AcaAmxxIiA2ZjVjNjFlNmM1YmNkNGFiOGIxNDVjMGY4NDMzYjM2Mg; passport_auth_status=fc93c033e0d3a3bbecee03c78cccc386%2C427e1990404e151de350cdd08cba5123; passport_auth_status_ss=fc93c033e0d3a3bbecee03c78cccc386%2C427e1990404e151de350cdd08cba5123; uid_tt=6e9bbf84ea26c7a66c5fb11ddd33d448; uid_tt_ss=6e9bbf84ea26c7a66c5fb11ddd33d448; sid_tt=44629b269b0c550b5f0b5cbfb23fe3f7; sessionid=44629b269b0c550b5f0b5cbfb23fe3f7; sessionid_ss=44629b269b0c550b5f0b5cbfb23fe3f7; _bd_ticket_crypt_cookie=bab77e18608c83d5ae0a841912e3272f; sid_guard=44629b269b0c550b5f0b5cbfb23fe3f7%7C1708005323%7C5183998%7CMon%2C+15-Apr-2024+13%3A55%3A21+GMT; sid_ucp_v1=1.0.0-KDY4MDA2MjMzMzdlMjFmOWVmZTFmMGUwNjdkZDE5YTFiN2JiMDk4MGEKGwinmrC3ro2oAxDLr7iuBhjvMSAMOAZA9AdIBBoCbGYiIDQ0NjI5YjI2OWIwYzU1MGI1ZjBiNWNiZmIyM2ZlM2Y3; ssid_ucp_v1=1.0.0-KDY4MDA2MjMzMzdlMjFmOWVmZTFmMGUwNjdkZDE5YTFiN2JiMDk4MGEKGwinmrC3ro2oAxDLr7iuBhjvMSAMOAZA9AdIBBoCbGYiIDQ0NjI5YjI2OWIwYzU1MGI1ZjBiNWNiZmIyM2ZlM2Y3; douyin.com; device_web_cpu_core=20; device_web_memory_size=8; architecture=amd64; csrf_session_id=3864ddcfe25c1ff249ffcc8bb7977ffc; FOLLOW_NUMBER_YELLOW_POINT_INFO=%22MS4wLjABAAAADPJGQhEjPphyqJkRwIvIzZDwdmQyEsRbY1LpMt1pGxI7hqKoamK1A-zX6i5eIvQ2%2F1708185600000%2F0%2F1708183151603%2F0%22; strategyABtestKey=%221708183152.173%22; xg_device_score=6.794335695120184; FOLLOW_LIVE_POINT_INFO=%22MS4wLjABAAAADPJGQhEjPphyqJkRwIvIzZDwdmQyEsRbY1LpMt1pGxI7hqKoamK1A-zX6i5eIvQ2%2F1708185600000%2F0%2F1708183155063%2F0%22; tt_scid=lV-y8l.RQP0thpFVkC-b1uhoxtkIKc5TEZkX.2L4V9KoimKeedXvEoTAiJfSeYiR9f39; download_guide=%223%2F20240217%2F1%22; __ac_nonce=065d0cec7001dd5b6f2ae; __ac_signature=_02B4Z6wo00f01y2EMOgAAIDAEC0qdX.WF3stpDRAAK68EQFQWSthN4tqN9EIw.qWoeg0R4hVz3AOXFvNNj-VGBx.555zY4cTY.2a3xlGgWF5NiByZMu3f7jlRuwGNPZ7pqMCU44n9Mjr1Uibd3; SEARCH_RESULT_LIST_TYPE=%22single%22; odin_tt=8b24a8020edb289f49677cfdfe1199d89a171065c41830d57df274d51750414d115e35672bf5f8e53361f3caf7a59ae6; IsDouyinActive=true; stream_recommend_feed_params=%22%7B%5C%22cookie_enabled%5C%22%3Atrue%2C%5C%22screen_width%5C%22%3A1536%2C%5C%22screen_height%5C%22%3A864%2C%5C%22browser_online%5C%22%3Atrue%2C%5C%22cpu_core_num%5C%22%3A20%2C%5C%22device_memory%5C%22%3A8%2C%5C%22downlink%5C%22%3A1.5%2C%5C%22effective_type%5C%22%3A%5C%224g%5C%22%2C%5C%22round_trip_time%5C%22%3A50%7D%22; bd_ticket_guard_client_data=eyJiZC10aWNrZXQtZ3VhcmQtdmVyc2lvbiI6MiwiYmQtdGlja2V0LWd1YXJkLWl0ZXJhdGlvbi12ZXJzaW9uIjoxLCJiZC10aWNrZXQtZ3VhcmQtcmVlLXB1YmxpYy1rZXkiOiJCTThwbXExU2dUM1ZDWXpxZnhEbjViUmhGdnFXTWdpNzdZN1IwejE1S2hWajZqZlJrTmhTamN6QldWeHgwSGd0YTBHR3JvMzYzTzB0aUlkN2hDVW9JQ009IiwiYmQtdGlja2V0LWd1YXJkLXdlYi12ZXJzaW9uIjoxfQ%3D%3D; passport_fe_beating_status=true; home_can_add_dy_2_desktop=%221%22; msToken=yPoIvIY4_YaT5iY99h8XJ_raQ8PB1gKxKb38N8sTRk6J_SKq0XlLiIu8cWm0QdKn5qu-Ed7gZjgRx36lw7Y5FjrhKzG5rt5SxDwzbJHo48ZHPWXDOiJDL0LsTNA=; msToken=aYGxNWM9yPc4e1MaHVOuIWbn9Gvmi-g2nJM4dU4Bn1jG52eXbXeH9HpfOdbbLX58vXssoXx1An_0eGRpLWqmpuGwEVH2vf61vGfuvAAEhDGL0IWVmg=='
}
url = 'https://www.douyin.com/aweme/v1/web/hot/search/list/?device_platform=webapp&aid=6383&channel=channel_pc_web&detail_list=1&source=6&board_type=0&board_sub_type=&pc_client_type=1&version_code=170400&version_name=17.4.0&cookie_enabled=true&screen_width=1707&screen_height=1067&browser_language=zh-CN&browser_platform=Win32&browser_name=Chrome&browser_version=122.0.0.0&browser_online=true&engine_name=Blink&engine_version=122.0.0.0&os_name=Windows&os_version=10&cpu_core_num=32&device_memory=8&platform=PC&downlink=10&effective_type=4g&round_trip_time=250&webid=7329394854488032822&msToken=xbT-knmOtL2HBfyB9Y_km6Bvpq64TcjRwy59p-KnrW7K7Ssx7TmazwqBw0R0kd1ARSJ_VewvjqVHKKCrTH1YZpTkbPNGqwJkwupi0k9BQSIYXLyGRFskPwaUaTYUgw==&X-Bogus=DFSzswVuRa2ANCPStoXmMvB9Piz2'
res = requests.get(url,headers=headers)

position_list = []
title_list = []
hot_url = []
time_list = []
hot_value_list = []

json_data = res.json()
data_list = json_data['data']['word_list']

for data in data_list:
    position = data.get('position',0)
    if position == 0:
        continue
    position_list.append(position)
    title = data.get('word', '')
    title_list.append(title)
    hot_value = data.get('hot_value', '')
    hot_value_list.append(hot_value)
    event_time = data.get('event_time', '')
    if event_time:
        timestamp = float(event_time)
        dt_object = datetime.datetime.fromtimestamp(timestamp)
        formatted_date = dt_object.strftime("%Y-%m-%d %H:%M:%S")
        time_list.append(formatted_date)
    else:
        time_list.append('')
    hot_url.append('https://www.douyin.com/hot/' + data.get('sentence_id', ''))

'''热榜生成'''
df = pd.DataFrame(
    {
        '热榜排名': position_list,
        '热榜标题': title_list,
        '热榜时间': time_list,
        '热度值': hot_value_list,
        '链接': hot_url,
    }
)
df.to_excel('抖音热榜.xlsx', index=False)
print("\n\n抖音热榜表格已生成！")


'''以下的url来自于网页抓包中的xhr文件,值得注意的是这里的getvideo函数将通过两次网络请求返回video的二进制文件'''

url1 = 'https://www.douyin.com/aweme/v1/web/channel/feed/?device_platform=webapp&aid=6383&channel=channel_pc_web&count=16&tag_id=300213&Seo-Flag=0&refresh_index=1&awemePcRecRawData=%7B%22is_client%22:false%7D&pc_client_type=1&version_code=170400&version_name=17.4.0&cookie_enabled=true&screen_width=1536&screen_height=864&browser_language=zh-CN&browser_platform=Win32&browser_name=Edge&browser_version=122.0.0.0&browser_online=true&engine_name=Blink&engine_version=122.0.0.0&os_name=Windows&os_version=10&cpu_core_num=20&device_memory=8&platform=PC&downlink=10&effective_type=4g&round_trip_time=50&webid=7339895700894778892&msToken=D7qlw5QtRjAbcBscdzzexEFikJiRh3nwGuu1xmZGR8wmnDyq6olvO9Oi3wsSlfdLCHk4_4ipXVq_jTD71wIus6PV3fMjalObf2CZmDJWJZNX-RfYJtGRqLDL2e_6&X-Bogus=DFSzswVYjcTANxTQtoFIiCD4OF6p'
url2 = 'https://www.douyin.com/aweme/v1/web/channel/feed/?device_platform=webapp&aid=6383&channel=channel_pc_web&count=10&tag_id=300205&Seo-Flag=0&refresh_index=1&awemePcRecRawData=%7B%22is_client%22:false%7D&pc_client_type=1&version_code=170400&version_name=17.4.0&cookie_enabled=true&screen_width=1536&screen_height=864&browser_language=zh-CN&browser_platform=Win32&browser_name=Edge&browser_version=122.0.0.0&browser_online=true&engine_name=Blink&engine_version=122.0.0.0&os_name=Windows&os_version=10&cpu_core_num=20&device_memory=8&platform=PC&downlink=10&effective_type=4g&round_trip_time=50&webid=7339895700894778892&msToken=DP0YpPpbSjaqWwf64RSLayLFF9ONSjBjt3fnZZkub3cVBq7GfSRIxbMFKpdnnE75XUwqanyQ1FSUfbhXvrj5SHkf3aPNDPGthKBnk6GHAvTCQHS0oFeAVsB0oXrJ&X-Bogus=DFSzswVuSbzANtwbtoF2SmD4OF1W'
url3 = 'https://www.douyin.com/aweme/v1/web/channel/feed/?device_platform=webapp&aid=6383&channel=channel_pc_web&count=10&tag_id=300206&Seo-Flag=0&refresh_index=1&awemePcRecRawData=%7B%22is_client%22:false%7D&pc_client_type=1&version_code=170400&version_name=17.4.0&cookie_enabled=true&screen_width=1536&screen_height=864&browser_language=zh-CN&browser_platform=Win32&browser_name=Edge&browser_version=122.0.0.0&browser_online=true&engine_name=Blink&engine_version=122.0.0.0&os_name=Windows&os_version=10&cpu_core_num=20&device_memory=8&platform=PC&downlink=10&effective_type=4g&round_trip_time=50&webid=7339895700894778892&msToken=iFiWIUGty0CUIxZcxJImhqeQZGkEC8NNk_ou4BscyUF4HMFbN55kPj6aNEH1Zt3jLsvzxBGxFUu6vKn25i_bIQ3sWd9k7_MXAjgciiMJ2-bvryuL9cA=&X-Bogus=DFSzswVLcI2ANcq/toF5dCD4OF6A'
url4 = 'https://www.douyin.com/aweme/v1/web/channel/feed/?device_platform=webapp&aid=6383&channel=channel_pc_web&count=10&tag_id=300209&Seo-Flag=0&refresh_index=1&awemePcRecRawData=%7B%22is_client%22:false%7D&pc_client_type=1&version_code=170400&version_name=17.4.0&cookie_enabled=true&screen_width=1536&screen_height=864&browser_language=zh-CN&browser_platform=Win32&browser_name=Edge&browser_version=122.0.0.0&browser_online=true&engine_name=Blink&engine_version=122.0.0.0&os_name=Windows&os_version=10&cpu_core_num=20&device_memory=8&platform=PC&downlink=10&effective_type=4g&round_trip_time=50&webid=7339895700894778892&msToken=8Cn7UakVBUDEW6C7gqXdXCx7vbI7_0nYWGAvx1iXJxmsjQ5kBOUsKqxTCnxwgwNveUv-t3DLNFNwMN9l-hIXGC3EH3wXFVi3RDrrojmAAV_LUp5F54w=&X-Bogus=DFSzswVLw60ANcq/toF5TmD4OF69'
url5 = 'https://www.douyin.com/aweme/v1/web/channel/feed/?device_platform=webapp&aid=6383&channel=channel_pc_web&count=10&tag_id=300204&Seo-Flag=0&refresh_index=1&awemePcRecRawData=%7B%22is_client%22:false%7D&pc_client_type=1&version_code=170400&version_name=17.4.0&cookie_enabled=true&screen_width=1536&screen_height=864&browser_language=zh-CN&browser_platform=Win32&browser_name=Edge&browser_version=122.0.0.0&browser_online=true&engine_name=Blink&engine_version=122.0.0.0&os_name=Windows&os_version=10&cpu_core_num=20&device_memory=8&platform=PC&downlink=10&effective_type=4g&round_trip_time=50&webid=7339895700894778892&msToken=JmBBzhiKCHz1S_a0W7G0Bd0l2gpAu61XYu0spToHmXRS0oFoYAMcoifX-37SM35LpsNKPRdRJj7au-dLnsbDY3xVATJTQSpmz3BohRXCdo3NGpAaB5Y=&X-Bogus=DFSzswVLqSiANcq/toF-RCD4OFIF'



'''视频提取'''

with open('music_video.mp4', 'wb') as f:
    f.write(getvideo(url4,headers2))
    print("\n\n抖音音乐栏视频提取成功！")
time.sleep(10)
with open('food_video.mp4', 'wb') as f:
    f.write(getvideo(url5,headers2))
    print("\n\n抖音美食栏视频提取成功！")
time.sleep(10)

with open('knowledge_video.mp4', 'wb') as f:
    f.write(getvideo(url1,headers2))
    print("\n\n抖音知识栏视频提取成功！")
time.sleep(10)
with open('game_video.mp4', 'wb') as f:
    f.write(getvideo(url2,headers2))
    print("\n\n抖音游戏栏视频提取成功！")
time.sleep(10)
with open('ACG_video.mp4', 'wb') as f:
    f.write(getvideo(url3,headers2))
    print("\n\n抖音二次元栏视频提取成功！")
time.sleep(10)
