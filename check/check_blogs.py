import csv
import requests
import time
from urllib.parse import urlparse
from concurrent.futures import ThreadPoolExecutor

def check_url(url, max_retries=5, timeout=15):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
        'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8',
        'Connection': 'keep-alive'
    }
    
    for attempt in range(max_retries):
        try:
            # 首先尝试GET请求，因为有些网站可能不支持HEAD请求
            try:
                response = requests.get(url, timeout=timeout, headers=headers, allow_redirects=True, stream=True)
                # 只读取响应头，不下载完整内容
                response.close()
                return response.status_code < 400
            except requests.RequestException:
                # 如果GET请求失败，尝试HEAD请求
                response = requests.head(url, timeout=timeout, headers=headers, allow_redirects=True)
                return response.status_code < 400
        except requests.RequestException as e:
            if attempt == max_retries - 1:
                print(f'请求失败: {str(e)}')
                return False
            time.sleep(2)  # 在重试之前等待2秒
    return False

def main():
    inaccessible_blogs = []
    accessible_blogs = []
    total_blogs = 0
    
    print('开始检查inaccessible_blogs.csv中的博客可访问性...')
    
    # 读取原有的blogs-list.csv内容
    existing_blogs = []
    with open('blogs-list.csv', 'r', encoding='utf-8') as f:
        reader = csv.reader(f)
        header = next(reader)  # 保存标题行
        existing_blogs = list(reader)
    
    # 读取inaccessible_blogs.csv
    with open('inaccessible_blogs.csv', 'r', encoding='utf-8') as f:
        reader = csv.reader(f)
        header = next(reader)  # 保存标题行
        blogs = []
        for row in reader:
            if len(row) >= 2 and row[1].strip():  # 确保至少有两个字段且URL不为空
                blog_name = row[0].strip()
                blog_url = row[1].strip()
                blogs.append((blog_name, blog_url, row))
    
    total_blogs = len(blogs)
    print(f'共发现 {total_blogs} 个待检测博客，开始检测...')
    
    with ThreadPoolExecutor(max_workers=5) as executor:
        futures = []
        for blog_name, url, row in blogs:
            if not (url.startswith('http://') or url.startswith('https://')):
                print(f'警告: {blog_name} 的URL格式不正确: {url}')
                inaccessible_blogs.append(row)
                continue
                
            print(f'正在检查: {blog_name} ({url})')
            future = executor.submit(check_url, url)
            futures.append((blog_name, url, row, future))
        
        for blog_name, url, row, future in futures:
            try:
                is_accessible = future.result()
                if not is_accessible:
                    inaccessible_blogs.append(row)
                    print(f'❌ {blog_name} 无法访问')
                else:
                    print(f'✅ {blog_name} 可以访问')
                    accessible_blogs.append(row)
            except Exception as e:
                inaccessible_blogs.append(row)
                print(f'❌ {blog_name} 检查时发生错误: {str(e)}')
    
    print('\n检查完成！')
    print(f'总计检查了 {total_blogs} 个博客')
    print(f'可访问博客数量: {len(accessible_blogs)}')
    print(f'无法访问博客数量: {len(inaccessible_blogs)}')
    
    if accessible_blogs:
        # 将可访问的博客添加到blogs-list.csv
        with open('blogs-list.csv', 'w', encoding='utf-8', newline='') as f:
            writer = csv.writer(f)
            writer.writerow(header)  # 写入标题行
            writer.writerows(existing_blogs + accessible_blogs)
            print('已将可访问的博客添加回 blogs-list.csv')
    
    # 更新inaccessible_blogs.csv，只保留仍然无法访问的博客
    with open('inaccessible_blogs.csv', 'w', encoding='utf-8', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(header)  # 写入标题行
        writer.writerows(inaccessible_blogs)
        print('已更新 inaccessible_blogs.csv')

if __name__ == '__main__':
    main()