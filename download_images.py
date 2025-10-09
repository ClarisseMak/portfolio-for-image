#!/usr/bin/env python3
"""
B站图床图片下载脚本
用于批量下载 example.json 中的图片到本地，解决防盗链问题
"""

import os
import json
import requests
from pathlib import Path
from urllib.parse import urlparse

# 配置
JSON_FILE = 'src/assets/projects/example.json'
OUTPUT_DIR = 'public/images/projects'
BACKUP_JSON = 'src/assets/projects/example.backup.json'

# 请求头（模拟B站访问）
HEADERS = {
    'Referer': 'https://www.bilibili.com',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
    'Accept': 'image/avif,image/webp,image/apng,image/*,*/*;q=0.8',
}

def ensure_dir(directory):
    """确保目录存在"""
    Path(directory).mkdir(parents=True, exist_ok=True)

def download_image(url, save_path):
    """
    下载单张图片
    :param url: 图片URL
    :param save_path: 保存路径
    :return: 是否成功
    """
    try:
        print(f"  下载: {url}")
        response = requests.get(url, headers=HEADERS, timeout=30)
        
        if response.status_code == 200:
            with open(save_path, 'wb') as f:
                f.write(response.content)
            print(f"  ✅ 成功: {save_path}")
            return True
        else:
            print(f"  ❌ 失败: HTTP {response.status_code}")
            return False
    except Exception as e:
        print(f"  ❌ 错误: {str(e)}")
        return False

def get_file_extension(url):
    """从URL获取文件扩展名"""
    parsed = urlparse(url)
    _, ext = os.path.splitext(parsed.path)
    return ext if ext else '.jpg'

def process_json():
    """处理JSON文件，下载图片并更新路径"""
    
    # 读取JSON文件
    print("📖 读取JSON文件...")
    try:
        with open(JSON_FILE, 'r', encoding='utf-8') as f:
            data = json.load(f)
    except FileNotFoundError:
        print(f"❌ 文件不存在: {JSON_FILE}")
        return
    except json.JSONDecodeError:
        print(f"❌ JSON格式错误: {JSON_FILE}")
        return
    
    # 备份原文件
    print(f"💾 备份原文件到: {BACKUP_JSON}")
    with open(BACKUP_JSON, 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=2)
    
    # 确保输出目录存在
    ensure_dir(OUTPUT_DIR)
    
    # 统计
    total_images = 0
    success_count = 0
    
    # 遍历项目
    projects = data.get('projects', [])
    for project in projects:
        project_id = project.get('id')
        project_title = project.get('title', 'untitled')
        print(f"\n📦 处理项目 {project_id}: {project_title}")
        
        main_items = project.get('main', [])
        for idx, item in enumerate(main_items):
            image_url = item.get('image', '')
            
            # 跳过本地路径
            if not image_url.startswith('http'):
                print(f"  ⏭️  跳过本地图片: {image_url}")
                continue
            
            total_images += 1
            
            # 生成文件名
            ext = get_file_extension(image_url)
            filename = f"project{project_id}_item{idx}{ext}"
            save_path = os.path.join(OUTPUT_DIR, filename)
            
            # 下载图片
            if download_image(image_url, save_path):
                # 更新JSON中的路径
                new_path = f"/images/projects/{filename}"
                item['image'] = new_path
                success_count += 1
            else:
                print(f"  ⚠️  保留原URL")
    
    # 保存更新后的JSON
    if success_count > 0:
        print(f"\n💾 保存更新后的JSON...")
        with open(JSON_FILE, 'w', encoding='utf-8') as f:
            json.dump(data, f, ensure_ascii=False, indent=2)
        print(f"✅ JSON文件已更新")
    
    # 输出统计
    print(f"\n" + "="*50)
    print(f"📊 下载完成！")
    print(f"   总图片数: {total_images}")
    print(f"   成功下载: {success_count}")
    print(f"   失败数量: {total_images - success_count}")
    print(f"   保存位置: {OUTPUT_DIR}")
    print(f"   备份文件: {BACKUP_JSON}")
    print("="*50)

def main():
    """主函数"""
    print("="*50)
    print("🚀 B站图床图片下载工具")
    print("="*50)
    
    process_json()
    
    print("\n💡 提示:")
    print("   1. 图片已保存到 public/images/projects/ 目录")
    print("   2. example.json 已自动更新为本地路径")
    print("   3. 原文件备份在 example.backup.json")
    print("   4. 如果有失败的图片，请检查网络或手动下载")

if __name__ == '__main__':
    main()

