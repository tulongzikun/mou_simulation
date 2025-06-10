import requests
import csv
import time
import random
from bs4 import BeautifulSoup
from fake_useragent import UserAgent

class ThreeKingdomsSpider:
    def __init__(self):
        self.base_url = "https://game.xiaomi.com/gamelist/sanmou/generals"  # 实际目标URL需替换
        self.ua = UserAgent()
        self.headers = {
            "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
            "Accept-Language": "zh-CN,zh;q=0.9",
            "Connection": "keep-alive",
            "Referer": "https://game.xiaomi.com/",
            "Sec-Fetch-Dest": "document",
            "Sec-Fetch-Mode": "navigate"
        }
        self.data_fields = [
            "name", "force", "strength", "intelligence", "command", "initiative",
            "troop_type", "base_skill", "position", "tier"
        ]

    def _get_random_header(self):
        """生成随机请求头"""
        self.headers["User-Agent"] = self.ua.random
        return self.headers
    
    def get_general_list(self):
        url = "https://wiki.biligame.com/sm/%E9%A6%96%E9%A1%B5"
        response = requests.get(
                url,
                headers=self._get_random_header(),
                timeout=15
            )
        print(response.text)

    def fetch_general_data(self, page=1):
        """爬取单页武将数据"""
        try:
            params = {"page": page}
            response = requests.get(
                self.base_url,
                headers=self._get_random_header(),
                params=params,
                timeout=15
            )
            response.raise_for_status()
            
            if "验证码" in response.text:
                raise Exception("触发反爬机制，需要验证码")
                
            return response.text
        except Exception as e:
            print(f"爬取失败: {str(e)}")
            return None

    def parse_general_data(self, html):
        """解析武将数据（需根据实际页面结构调整）"""
        soup = BeautifulSoup(html, 'lxml')
        generals = []
        
        # 示例解析逻辑（实际选择器需调整）
        for card in soup.select('.general-card'):
            try:
                name = card.select_one('.name').text.strip()
                force = card.select_one('.force').text.strip()  # 势力:cite[2]:cite[3]
                
                # 基础属性:cite[1]:cite[2]
                strength = float(card.select_one('.attr-strength').text)
                intelligence = float(card.select_one('.attr-intelligence').text)
                command = float(card.select_one('.attr-command').text)  # 统率
                initiative = float(card.select_one('.attr-initiative').text)  # 先攻
                
                troop_type = card.select_one('.troop-type').text  # 兵种:cite[2]
                base_skill = card.select_one('.base-skill').text  # 自带战法:cite[6]
                
                # 武将定位与强度分级:cite[7]:cite[8]
                position = card.select_one('.position').text if card.select_one('.position') else ""
                tier = card.select_one('.tier-rating')['data-tier'] if card.select_one('.tier-rating') else ""
                
                generals.append({
                    "name": name,
                    "force": force,
                    "strength": strength,
                    "intelligence": intelligence,
                    "command": command,
                    "initiative": initiative,
                    "troop_type": troop_type,
                    "base_skill": base_skill,
                    "position": position,
                    "tier": tier
                })
            except Exception as e:
                print(f"解析错误: {str(e)}")
                continue
                
        return generals

    def save_to_csv(self, data, filename="generals.csv"):
        """保存数据到CSV文件"""
        with open(filename, 'a', newline='', encoding='utf-8-sig') as f:
            writer = csv.DictWriter(f, fieldnames=self.data_fields)
            if f.tell() == 0:  # 文件为空时写入表头
                writer.writeheader()
            writer.writerows(data)

    def run(self, max_pages=10):
        """执行爬虫"""
        print("开始爬取《三国：谋定天下》武将数据...")
        self.get_general_list()
        print("具体数据抓取")
        for page in range(1, max_pages + 1):
            print(f"正在爬取第 {page} 页...")
            html = self.fetch_general_data(page)
            if not html:
                break
                
            generals = self.parse_general_data(html)
            if not generals:
                print(f"第 {page} 页未解析到数据")
                break
                
            self.save_to_csv(generals)
            print(f"已保存 {len(generals)} 名武将数据")
            
            # 随机延迟防止封禁:cite[1]
            time.sleep(random.uniform(1.5, 3.5))
        
        print("爬取完成！数据已保存到 generals.csv")

if __name__ == "__main__":
    spider = ThreeKingdomsSpider()
    spider.run(max_pages=5)  # 测试时减少页数