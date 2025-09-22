from flask import Flask, render_template, url_for, request, jsonify
from datetime import datetime
import os
import json
import requests

app = Flask(__name__)

def is_private_ip(ip):
    """检查是否为私有IP地址"""
    try:
        # 将IP地址转换为整数
        ip_num = sum(int(part) << (8 * (3 - i)) 
                for i, part in enumerate(ip.split('.')))
        
        # 检查私有IP范围:
        # 10.0.0.0/8, 172.16.0.0/12, 192.168.0.0/16
        return (
            (ip_num >> 24 == 10) or
            (ip_num >> 20 == 0xAC1) or  # 172.16.0.0/12
            (ip_num >> 16 == 0xC0A8)    # 192.168.0.0/16
        )
    except:
        return False

def get_ip_country(ip):
    """获取IP所属国家代码"""
    try:
        app.logger.debug(f"开始检测IP: {ip}")
        
        # 如果是私有IP，直接返回中国
        if is_private_ip(ip):
            app.logger.debug("检测到私有IP，默认使用中国地图")
            return 'CN'
            
        
        # 1. 优先使用本地IP库检测
        try:
            from qqwry import QQwry
            q = QQwry('qqwry.dat')
            result = q.lookup(ip)
            app.logger.debug(f"纯真IP库检测结果: {result}")
            if result and '中国' in result[1]:
                app.logger.debug("纯真IP库确认是中国IP")
                return 'CN'  # 中国国家代码
        except ImportError as e:
            app.logger.debug(f"纯真IP库不可用: {str(e)}")
        except Exception as e:
            app.logger.error(f"纯真IP库检测错误: {str(e)}")
        
        # 2. 使用ip-api.com检测国家
        headers = {'User-Agent': 'Mozilla/5.0'}
        try:
            app.logger.debug("正在使用ip-api.com检测...")
            response = requests.get(
                f"http://ip-api.com/json/{ip}?fields=countryCode&lang=zh-CN",
                headers=headers,
                timeout=2
            )
            if response.status_code == 200:
                data = response.json()
                app.logger.debug(f"ip-api.com返回: {data}")
                if data.get('countryCode'):
                    return data['countryCode']  # 返回实际国家代码
        except requests.RequestException as e:
            app.logger.error(f"ip-api.com请求失败: {str(e)}")
            
        # 3. 默认返回中国(安全默认值)
        app.logger.debug("无法确定IP国家，默认使用中国地图")
        return 'CN'
        
    except Exception as e:
        app.logger.error(f"IP检测错误: {str(e)}，默认使用中国地图")
        return 'CN'

def is_china_ip(ip):
    """判断是否为中国的IP"""
    return get_ip_country(ip) == 'CN'

@app.route('/')
def home():
    with open('static/data/countdown.json', 'r', encoding='utf-8') as f:
        countdown_data = json.load(f)
    return render_template('index.html', countdown_data=countdown_data)

@app.route('/gallery')
def gallery():
    image_dir = os.path.join(app.static_folder, 'images')
    image_files = [f for f in os.listdir(image_dir) if f.lower().endswith(('.png', '.jpg', '.jpeg'))]
    return render_template('gallery.html', image_files=image_files)

@app.route('/timeline')
def timeline():
    with open('static/data/timeline.json', 'r', encoding='utf-8') as f:
        timeline_data = json.load(f)
    return render_template('timeline.html', timeline_data=timeline_data)

@app.route('/map') 
def map():
    with open('static/data/locations.json', 'r', encoding='utf-8') as f:
        locations_data = json.load(f)
    country = get_ip_country(request.remote_addr)
    is_china = country == 'CN'
    print(f"IP检测结果: 国家={country}, IP={request.remote_addr}")
    # 默认使用高德地图，除非明确检测到国外IP
    use_amap = is_china
    return render_template('map.html',
                         locations_data=locations_data,
                         use_amap=use_amap)

@app.route('/wishlist')
def wishlist():
    with open('static/data/wishlist.json', 'r', encoding='utf-8') as f:
        wishlist_data = json.load(f)
    return render_template('wishlist.html', wishlist_data=wishlist_data['items'])

@app.route('/update_wishlist', methods=['POST'])
def update_wishlist():
    data = request.get_json()
    with open('static/data/wishlist.json', 'r+', encoding='utf-8') as f:
        wishlist_data = json.load(f)
        for item in wishlist_data['items']:
            if item['id'] == data['id']:
                item['completed'] = data['completed']
                break
        f.seek(0)
        json.dump(wishlist_data, f, ensure_ascii=False, indent=2)
        f.truncate()
    return jsonify({'status': 'success'})

@app.route('/timers')
def timers():
    with open('static/data/timers.json', 'r', encoding='utf-8') as f:
        timers_data = json.load(f)
    
    # 计算每个计时器的天数
    now = datetime.now()
    for timer in timers_data['timers']:
        target_date = datetime.strptime(timer['target_date'], '%Y-%m-%d')
        if timer['is_countdown']:
            delta = target_date - now
        else:
            delta = now - target_date
        timer['days'] = max(0, delta.days)
    
    return render_template('timers.html', timers_data=timers_data)

if __name__ == '__main__':
    # 设置更详细的日志级别
    import logging
    logging.basicConfig(level=logging.DEBUG)
    app.logger.setLevel(logging.DEBUG)
    app.run(debug=True, host='0.0.0.0', port=520)
